from django.template.defaultfilters import floatformat
from django_rq import job

from tunga.settings import TUNGA_URL, SLACK_STAFF_INCOMING_WEBHOOK, SLACK_STAFF_LEADS_CHANNEL, \
    SLACK_ATTACHMENT_COLOR_TUNGA, SLACK_ATTACHMENT_COLOR_GREEN, SLACK_STAFF_UPDATES_CHANNEL, SLACK_ATTACHMENT_COLOR_RED, \
    SLACK_ATTACHMENT_COLOR_NEUTRAL, SLACK_ATTACHMENT_COLOR_BLUE, SLACK_STAFF_PAYMENTS_CHANNEL
from tunga_payments.models import Invoice
from tunga_projects.models import Project, ProgressReport
from tunga_utils import slack_utils
from tunga_utils.constants import PROGRESS_EVENT_PM, PROGRESS_EVENT_INTERNAL, PROGRESS_EVENT_CLIENT, \
    PROGRESS_EVENT_MILESTONE, INVOICE_TYPE_SALE
from tunga_utils.helpers import clean_instance, convert_to_text


@job
def notify_new_project_slack_admin(project):
    project = clean_instance(project, Project)
    project_url = '{}/projects/{}/'.format(TUNGA_URL, project.id)

    summary = "New project created by {} | <{}|View on Tunga>".format(
        project.user.display_name.encode('utf-8'),
        project_url
    )

    attachments = [
        {
            slack_utils.KEY_TITLE: project.title,
            slack_utils.KEY_TITLE_LINK: project_url,
            slack_utils.KEY_TEXT: project.description or project.title,
            slack_utils.KEY_MRKDWN_IN: [slack_utils.KEY_TEXT],
            slack_utils.KEY_COLOR: SLACK_ATTACHMENT_COLOR_TUNGA
        }
    ]

    extra_details = ''
    if project.type:
        extra_details += '*Type*: {}\n'.format(project.get_type_display())
    if project.expected_duration:
        extra_details += '*Expected duration*: {}\n'.format(project.get_expected_duration_display())
    if project.skills:
        extra_details += '*Skills*: {}\n'.format(str(project.skills))
    if project.deadline:
        extra_details += '*Deadline*: {}\n'.format(project.deadline.strftime("%d %b, %Y"))
    if project.budget:
        extra_details += '*Fee*: EUR {}\n'.format(floatformat(project.budget, arg=-2))

    if extra_details:
        attachments.append({
            slack_utils.KEY_TEXT: extra_details,
            slack_utils.KEY_MRKDWN_IN: [slack_utils.KEY_TEXT],
            slack_utils.KEY_COLOR: SLACK_ATTACHMENT_COLOR_GREEN
        })

    slack_utils.send_incoming_webhook(SLACK_STAFF_INCOMING_WEBHOOK, {
        slack_utils.KEY_TEXT: summary,
        slack_utils.KEY_CHANNEL: SLACK_STAFF_LEADS_CHANNEL,
        slack_utils.KEY_ATTACHMENTS: attachments
    })


def create_progress_report_slack_message(progress_report, updated=False, to_client=False):
    is_pm_report = progress_report.event.type in [PROGRESS_EVENT_PM, PROGRESS_EVENT_INTERNAL] or \
                   (progress_report.event.type == PROGRESS_EVENT_MILESTONE and progress_report.user.is_project_manager)
    is_client_report = progress_report.event.type == PROGRESS_EVENT_CLIENT or \
                       (progress_report.event.type == PROGRESS_EVENT_MILESTONE and progress_report.user.is_project_owner)
    is_pm_or_client_report = is_pm_report or is_client_report
    is_dev_report = not is_pm_or_client_report

    report_url = '{}/projects/{}/events/{}/'.format(TUNGA_URL, progress_report.event.project_id, progress_report.event_id)
    slack_msg = "{} {} a {} | {}".format(
        progress_report.user.display_name.encode('utf-8'),
        updated and 'updated' or 'submitted',
        is_client_report and "Progress Survey" or "Progress Report",
        '<{}|View on Tunga>'.format(report_url)
    )

    slack_text_suffix = ''
    if not is_client_report:
        slack_text_suffix += '*Status:* {}\n*Percentage completed:* {}{}'.format(
            progress_report.get_status_display(), progress_report.percentage, '%')
    if not to_client:
        if progress_report.last_deadline_met is not None:
            slack_text_suffix += '\n*Was the last deadline met?:* {}'.format(
                progress_report.last_deadline_met and 'Yes' or 'No'
            )
        if progress_report.next_deadline:
            slack_text_suffix += '\n*Next deadline:* {}'.format(progress_report.next_deadline.strftime("%d %b, %Y"))
    if is_client_report:
        if progress_report.deliverable_satisfaction is not None:
            slack_text_suffix += '\n*Are you satisfied with the deliverables?:* {}'.format(
                progress_report.deliverable_satisfaction and 'Yes' or 'No'
            )
    if is_dev_report:
        if progress_report.stuck_reason:
            slack_text_suffix += '\n*Reason for being stuck:*\n {}'.format(
                convert_to_text(progress_report.get_stuck_reason_display())
            )
    attachments = [
        {
            slack_utils.KEY_TITLE: progress_report.event.project.title,
            slack_utils.KEY_TITLE_LINK: report_url,
            slack_utils.KEY_TEXT: slack_text_suffix,
            slack_utils.KEY_MRKDWN_IN: [slack_utils.KEY_TEXT],
            slack_utils.KEY_COLOR: SLACK_ATTACHMENT_COLOR_BLUE
        }
    ]

    if not to_client:
        if progress_report.deadline_miss_communicated is not None:
            attachments.append({
                slack_utils.KEY_TITLE: '{} promptly about not making the deadline?'.format(
                    is_client_report and 'Did the project manager/ developer(s) inform you' or 'Did you inform the client'),
                slack_utils.KEY_TEXT: '{}'.format(progress_report.deadline_miss_communicated and 'Yes' or 'No'),
                slack_utils.KEY_MRKDWN_IN: [slack_utils.KEY_TEXT],
                slack_utils.KEY_COLOR: SLACK_ATTACHMENT_COLOR_RED
            })

    if progress_report.deadline_report:
        attachments.append({
            slack_utils.KEY_TITLE: 'Report about the last deadline:',
            slack_utils.KEY_TEXT: convert_to_text(progress_report.deadline_report),
            slack_utils.KEY_MRKDWN_IN: [slack_utils.KEY_TEXT],
            slack_utils.KEY_COLOR: SLACK_ATTACHMENT_COLOR_RED
        })

    if is_client_report:
        if progress_report.rate_deliverables:
            attachments.append({
                slack_utils.KEY_TITLE: 'How would you rate the deliverables on a scale from 1 to 5?',
                slack_utils.KEY_TEXT: '{}/5'.format(progress_report.rate_deliverables),
                slack_utils.KEY_MRKDWN_IN: [slack_utils.KEY_TEXT],
                slack_utils.KEY_COLOR: SLACK_ATTACHMENT_COLOR_BLUE
            })
        if progress_report.pm_communication:
            attachments.append({
                slack_utils.KEY_TITLE: 'Is the communication between you and the project manager/developer(s) going well?',
                slack_utils.KEY_TEXT: '{}'.format(progress_report.pm_communication and 'Yes' or 'No'),
                slack_utils.KEY_MRKDWN_IN: [slack_utils.KEY_TEXT],
                slack_utils.KEY_COLOR: SLACK_ATTACHMENT_COLOR_GREEN
            })
    else:
        # Status
        if progress_report.stuck_details:
            attachments.append({
                slack_utils.KEY_TITLE: 'Explain Further why you are stuck/what should be done:',
                slack_utils.KEY_TEXT: convert_to_text(progress_report.stuck_details),
                slack_utils.KEY_MRKDWN_IN: [slack_utils.KEY_TEXT],
                slack_utils.KEY_COLOR: SLACK_ATTACHMENT_COLOR_GREEN
            })

        if progress_report.started_at and not to_client:
            attachments.append({
                slack_utils.KEY_TITLE: 'When did you start this sprint/project?',
                slack_utils.KEY_TEXT: progress_report.started_at.strftime("%d %b, %Y"),
                slack_utils.KEY_MRKDWN_IN: [slack_utils.KEY_TEXT],
                slack_utils.KEY_COLOR: SLACK_ATTACHMENT_COLOR_BLUE
            })

        # Last
        if progress_report.accomplished:
            attachments.append({
                slack_utils.KEY_TITLE: 'What has been accomplished since last update?',
                slack_utils.KEY_TEXT: convert_to_text(progress_report.accomplished),
                slack_utils.KEY_MRKDWN_IN: [slack_utils.KEY_TEXT],
                slack_utils.KEY_COLOR: SLACK_ATTACHMENT_COLOR_GREEN
            })
        if progress_report.rate_deliverables and not to_client:
            attachments.append({
                slack_utils.KEY_TITLE: 'Rate Deliverables:',
                slack_utils.KEY_TEXT: '{}/5'.format(progress_report.rate_deliverables),
                slack_utils.KEY_MRKDWN_IN: [slack_utils.KEY_TEXT],
                slack_utils.KEY_COLOR: SLACK_ATTACHMENT_COLOR_RED
            })

        # Current
        if progress_report.todo:
            attachments.append({
                slack_utils.KEY_TITLE: is_dev_report and 'What do you intend to achieve/complete today?' or 'What are the next next steps?',
                slack_utils.KEY_TEXT: convert_to_text(progress_report.todo),
                slack_utils.KEY_MRKDWN_IN: [slack_utils.KEY_TEXT],
                slack_utils.KEY_COLOR: SLACK_ATTACHMENT_COLOR_GREEN
            })

        if not to_client:
            # Next
            if progress_report.next_deadline:
                attachments.append({
                    slack_utils.KEY_TITLE: 'When is the next deadline?',
                    slack_utils.KEY_TEXT: progress_report.next_deadline.strftime("%d %b, %Y"),
                    slack_utils.KEY_MRKDWN_IN: [slack_utils.KEY_TEXT],
                    slack_utils.KEY_COLOR: SLACK_ATTACHMENT_COLOR_RED
                })

            # Keep information about failures to meet deadlines internal
            if progress_report.next_deadline_meet is not None:
                attachments.append({
                    slack_utils.KEY_TITLE: 'Do you anticipate to meet this deadline?',
                    slack_utils.KEY_TEXT: '{}'.format(progress_report.next_deadline_meet and 'Yes' or 'No'),
                    slack_utils.KEY_MRKDWN_IN: [slack_utils.KEY_TEXT],
                    slack_utils.KEY_COLOR: SLACK_ATTACHMENT_COLOR_GREEN
                })
            if progress_report.next_deadline_fail_reason:
                attachments.append({
                    slack_utils.KEY_TITLE: 'Why will you not be able to make the next deadline?',
                    slack_utils.KEY_TEXT: convert_to_text(progress_report.next_deadline_fail_reason),
                    slack_utils.KEY_MRKDWN_IN: [slack_utils.KEY_TEXT],
                    slack_utils.KEY_COLOR: SLACK_ATTACHMENT_COLOR_RED
                })

        if progress_report.obstacles:
            attachments.append({
                slack_utils.KEY_TITLE: 'What obstacles are impeding your progress?',
                slack_utils.KEY_TEXT: convert_to_text(progress_report.obstacles),
                slack_utils.KEY_MRKDWN_IN: [slack_utils.KEY_TEXT],
                slack_utils.KEY_COLOR: SLACK_ATTACHMENT_COLOR_RED
            })
        if progress_report.obstacles_prevention:
            attachments.append({
                slack_utils.KEY_TITLE: 'What could have been done to prevent this from happening?',
                slack_utils.KEY_TEXT: convert_to_text(progress_report.obstacles_prevention),
                slack_utils.KEY_MRKDWN_IN: [slack_utils.KEY_TEXT],
                slack_utils.KEY_COLOR: SLACK_ATTACHMENT_COLOR_GREEN
            })

    if is_pm_report:
        if progress_report.team_appraisal:
            attachments.append({
                slack_utils.KEY_TITLE: 'Team appraisal:',
                slack_utils.KEY_TEXT: convert_to_text(progress_report.team_appraisal),
                slack_utils.KEY_MRKDWN_IN: [slack_utils.KEY_TEXT],
                slack_utils.KEY_COLOR: SLACK_ATTACHMENT_COLOR_NEUTRAL
            })

    if progress_report.remarks:
        attachments.append({
            slack_utils.KEY_TITLE: 'Other remarks or questions',
            slack_utils.KEY_TEXT: convert_to_text(progress_report.remarks),
            slack_utils.KEY_MRKDWN_IN: [slack_utils.KEY_TEXT],
            slack_utils.KEY_COLOR: SLACK_ATTACHMENT_COLOR_NEUTRAL
        })

    return slack_msg, attachments


@job
def notify_new_progress_report_slack(progress_report, updated=False):
    progress_report = clean_instance(progress_report, ProgressReport)

    is_pm_report = progress_report.event.type in [PROGRESS_EVENT_PM, PROGRESS_EVENT_INTERNAL] or \
                   (progress_report.event.type == PROGRESS_EVENT_MILESTONE and progress_report.user.is_project_manager)
    is_client_report = progress_report.event.type == PROGRESS_EVENT_CLIENT or \
                       (progress_report.event.type == PROGRESS_EVENT_MILESTONE and progress_report.user.is_project_owner)
    is_pm_or_client_report = is_pm_report or is_client_report
    is_dev_report = not is_pm_or_client_report

    # All reports go to Tunga #updates Slack
    slack_msg, attachments = create_progress_report_slack_message(progress_report, updated=updated)
    slack_utils.send_incoming_webhook(SLACK_STAFF_INCOMING_WEBHOOK, {
        slack_utils.KEY_TEXT: slack_msg,
        slack_utils.KEY_CHANNEL: SLACK_STAFF_UPDATES_CHANNEL,
        slack_utils.KEY_ATTACHMENTS: attachments
    })

    if is_dev_report:
        # Re-create report for clients
        # TODO: Respect client's settings
        slack_msg, attachments = create_progress_report_slack_message(progress_report, updated=updated, to_client=True)
        slack_utils.send_project_message(progress_report.event.project, message=slack_msg, attachments=attachments)


@job
def notify_new_invoice_slack_admin(invoice):
    invoice = clean_instance(invoice, Invoice)

    if invoice.legacy_id:
        # ignore legacy invoices
        return

    if invoice.type != INVOICE_TYPE_SALE:
        # Only notify about client invoices
        return

    project_url = '{}/projects/{}/'.format(TUNGA_URL, invoice.project.id)
    payment_url = '{}/pay'.format(project_url)
    client_url = '{}/network/{}/'.format(TUNGA_URL, invoice.user.username)
    invoice_url = '{}/api/invoices/{}/download/?format=pdf'.format(TUNGA_URL, invoice.id)
    slack_msg = '{} generated an invoice'.format(
        invoice.created_by.display_name.encode('utf-8')
    )

    invoice_summary = 'Client: <{}|{}>\nProject: <{}|{}>\nTitle: {}\nFee: EUR {}\n<{}|Download invoice>'.format(
        client_url, invoice.user.display_name.encode('utf-8'),
        project_url, invoice.project.title,
        invoice.title,
        invoice.amount,
        invoice_url
    )

    attachments = [
        {
            slack_utils.KEY_TITLE: invoice.title,
            slack_utils.KEY_TITLE_LINK: payment_url,
            slack_utils.KEY_TEXT: invoice_summary,
            slack_utils.KEY_MRKDWN_IN: [slack_utils.KEY_TEXT],
            slack_utils.KEY_COLOR: SLACK_ATTACHMENT_COLOR_BLUE
        },
    ]

    slack_utils.send_incoming_webhook(
        SLACK_STAFF_INCOMING_WEBHOOK,
        {
            slack_utils.KEY_TEXT: slack_msg,
            slack_utils.KEY_ATTACHMENTS: attachments,
            slack_utils.KEY_CHANNEL: SLACK_STAFF_PAYMENTS_CHANNEL
        }
    )