from django_rq import job
from django_rq.decorators import job

from tunga.settings import SLACK_STAFF_INCOMING_WEBHOOK, SLACK_STAFF_PROFILES_CHANNEL, SLACK_ATTACHMENT_COLOR_GREEN, \
    SLACK_ATTACHMENT_COLOR_BLUE, SLACK_STAFF_HUBSPOT_CHANNEL
from tunga_utils import slack_utils, hubspot_utils
from tunga_utils.helpers import clean_instance
from tunga_utils.models import InviteRequest


@job
def notify_new_invite_request_slack(invite_request):
    invite_request = clean_instance(invite_request, InviteRequest)

    slack_msg = "@domieck {} wants to join Tunga".format(
        invite_request.name
    )

    attachments = [
        {
            slack_utils.KEY_TITLE: invite_request.name,
            slack_utils.KEY_TITLE_LINK: invite_request.cv_url,
            slack_utils.KEY_TEXT: '*Name:* {}\n*Email:* {}\n*Country*: {}\n<{}|Download CV>'.format(
                invite_request.name,
                invite_request.email,
                invite_request.country.name,
                invite_request.cv_url
            ),
            slack_utils.KEY_MRKDWN_IN: [slack_utils.KEY_TEXT],
            slack_utils.KEY_COLOR: SLACK_ATTACHMENT_COLOR_GREEN,
        },
        {
            slack_utils.KEY_TITLE: 'Motivation',
            slack_utils.KEY_TEXT: invite_request.motivation,
            slack_utils.KEY_MRKDWN_IN: [slack_utils.KEY_TEXT],
            slack_utils.KEY_COLOR: SLACK_ATTACHMENT_COLOR_BLUE,
        }
    ]

    slack_utils.send_incoming_webhook(
        SLACK_STAFF_INCOMING_WEBHOOK,
        {
            slack_utils.KEY_TEXT: slack_msg,
            slack_utils.KEY_ATTACHMENTS: attachments,
            slack_utils.KEY_CHANNEL: SLACK_STAFF_PROFILES_CHANNEL
        }
    )


@job
def notify_hubspot_deal_changes_slack(deal_id, changes, event_ids=None):
    deal_url = None
    final_subscription_type = None

    deal_details = hubspot_utils.get_deal(deal_id)

    deal_properties = None
    deal_property_changes = []
    deal_name = None

    if deal_details and deal_details.get('properties', None):
        deal_properties = deal_details['properties']
        deal_name = deal_properties.get(hubspot_utils.KEY_DEALNAME, {})['value'] or ''

    for payload in changes:
        if deal_id != payload.get(hubspot_utils.KEY_OBJECT_ID):
            # Ignore changes from other deals
            continue

        subscription_type = payload.get(hubspot_utils.KEY_SUBSCRIPTION_TYPE)
        if subscription_type in [
            hubspot_utils.KEY_VALUE_DEAL_CREATED,
            hubspot_utils.KEY_VALUE_DEAL_DELETION,
            hubspot_utils.KEY_VALUE_DEAL_PROPERTY_CHANGE
        ]:
            if subscription_type != hubspot_utils.KEY_VALUE_DEAL_PROPERTY_CHANGE or not final_subscription_type:
                final_subscription_type = subscription_type

            if not deal_url:
                deal_url = 'https://app.hubspot.com/sales/{}/deal/{}/'.format(
                    payload.get(hubspot_utils.KEY_PORTAL_ID),
                    deal_id
                )

            if deal_properties and subscription_type == hubspot_utils.KEY_VALUE_DEAL_PROPERTY_CHANGE:
                deal_property_name = payload.get(hubspot_utils.KEY_PROPERTY_NAME, '')
                deal_property_value = payload.get(hubspot_utils.KEY_PROPERTY_VALUE, '')
                if deal_property_name:
                    deal_property_changes.append(
                        '*{}:* {}'.format(deal_property_name, deal_property_value or '')
                    )

    if deal_url and final_subscription_type:
        slack_utils.send_incoming_webhook(
            SLACK_STAFF_INCOMING_WEBHOOK,
            {
                slack_utils.KEY_CHANNEL: SLACK_STAFF_HUBSPOT_CHANNEL,
                slack_utils.KEY_TEXT: '{} in HubSpot | <{}|View details>'.format(
                    final_subscription_type == hubspot_utils.KEY_VALUE_DEAL_CREATED and 'New deal created' or (
                        'Deal {}'.format(final_subscription_type == hubspot_utils.KEY_VALUE_DEAL_DELETION and 'deleted' or 'updated')
                    ),
                    deal_url
                ),
                slack_utils.KEY_ATTACHMENTS: [
                    {
                        slack_utils.KEY_TITLE: deal_name,
                        slack_utils.KEY_TITLE_LINK: deal_url,
                        slack_utils.KEY_TEXT: '*Deal stage:* {}{}'.format(
                            deal_properties.get(hubspot_utils.KEY_DEALSTAGE, {})['value'] or 'Unknown',
                            deal_property_changes and '\n\n*Updates*:\n{}'.format('\n'.join(deal_property_changes)) or ''
                        ),
                        slack_utils.KEY_MRKDWN_IN: [slack_utils.KEY_TEXT],
                        slack_utils.KEY_COLOR: SLACK_ATTACHMENT_COLOR_GREEN
                    }
                ]
            }
        )
