# User Types
USER_TYPE_DEVELOPER = 1
USER_TYPE_PROJECT_OWNER = 2
USER_TYPE_PROJECT_MANAGER = 3

# User Source
USER_SOURCE_DEFAULT = 1
USER_SOURCE_TASK_WIZARD = 2
USER_SOURCE_MANUAL = 3

# Source
TASK_SOURCE_DEFAULT = 1
TASK_SOURCE_NEW_USER = 2

# Currencies
CURRENCY_BTC = 'BTC'
CURRENCY_EUR = 'EUR'
CURRENCY_USD = 'USD'
CURRENCY_UGX = 'UGX'
CURRENCY_TZS = 'TZS'
CURRENCY_NGN = 'NGN'

CURRENCY_CHOICES_EUR_ONLY = (
    (CURRENCY_EUR, 'EUR'),
)

# BTC Wallets
BTC_WALLET_PROVIDER_COINBASE = 'coinbase'

# App Integrations
APP_INTEGRATION_PROVIDER_GITHUB = 'github'
APP_INTEGRATION_PROVIDER_SLACK = 'slack'
APP_INTEGRATION_PROVIDER_HARVEST = 'harvest'

# Developer Payment Methods
PAYMENT_METHOD_BTC_WALLET = 'btc_wallet'
PAYMENT_METHOD_BTC_ADDRESS = 'btc_address'
PAYMENT_METHOD_MOBILE_MONEY = 'mobile_money'

# Task Types
TASK_TYPE_WEB = 1
TASK_TYPE_MOBILE = 2
TASK_TYPE_OTHER = 3

# Task scope
TASK_SCOPE_TASK = 1
TASK_SCOPE_ONGOING = 2
TASK_SCOPE_PROJECT = 3

# Task Coders
TASK_CODERS_NEEDED_ONE = 1
TASK_CODERS_NEEDED_MULTIPLE = -1

# Billing Type
TASK_BILLING_METHOD_FIXED = 1
TASK_BILLING_METHOD_HOURLY = 2

# Task Payment Methods
PAYMENT_METHOD_BITONIC = 'bitonic'
PAYMENT_METHOD_BITCOIN = 'bitcoin'
PAYMENT_METHOD_BANK = 'bank'
PAYMENT_METHOD_STRIPE = 'stripe'
PAYMENT_METHOD_AYDEN = 'ayden'
PAYMENT_METHOD_PAYONEER = 'payoneer'

# Transaction and Action Statuses
STATUS_INITIAL = 'initial'
STATUS_PENDING = 'pending'
STATUS_INITIATED = 'initiated'
STATUS_SUBMITTED = 'submitted'
STATUS_PROCESSING = 'processing'
STATUS_COMPLETED = 'completed'
STATUS_FAILED = 'failed'
STATUS_ACCEPTED = 'accepted'
STATUS_REJECTED = 'rejected'
STATUS_APPROVED = 'approved'
STATUS_DECLINED = 'declined'
STATUS_CANCELED = 'canceled'
STATUS_RETRY = 'retry'
STATUS_INTERESTED = 'interested'
STATUS_UNINTERESTED = 'uninterested'

REQUEST_STATUS_CHOICES = (
    (STATUS_INITIAL, 'Initial'),
    (STATUS_ACCEPTED, 'Accepted'),
    (STATUS_REJECTED, 'Rejected')
)

# Request Statuses
REQUEST_STATUS_INITIAL = 0
REQUEST_STATUS_ACCEPTED = 1
REQUEST_STATUS_REJECTED = 2

# Channel Types
CHANNEL_TYPE_DIRECT = 1
CHANNEL_TYPE_TOPIC = 2
CHANNEL_TYPE_SUPPORT = 3
CHANNEL_TYPE_DEVELOPER = 4

# Task Visibility
VISIBILITY_DEVELOPER = 1
VISIBILITY_MY_TEAM = 2
VISIBILITY_CUSTOM = 3
VISIBILITY_ONLY_ME = 4

# Support Visibility
VISIBILITY_ALL = 'all'
VISIBILITY_DEVELOPERS = 'developers'
VISIBILITY_PROJECT_OWNERS = 'project-owners'

# Update Schedule Periods
UPDATE_SCHEDULE_HOURLY = 1
UPDATE_SCHEDULE_DAILY = 2
UPDATE_SCHEDULE_WEEKLY = 3
UPDATE_SCHEDULE_MONTHLY = 4
UPDATE_SCHEDULE_QUATERLY = 5
UPDATE_SCHEDULE_ANNUALLY = 6

# Progress Event Types
LEGACY_PROGRESS_EVENT_TYPE_DEFAULT = 1
LEGACY_PROGRESS_EVENT_TYPE_PERIODIC = 2
LEGACY_PROGRESS_EVENT_TYPE_MILESTONE = 3
LEGACY_PROGRESS_EVENT_TYPE_SUBMIT = 4
LEGACY_PROGRESS_EVENT_TYPE_COMPLETE = 5
LEGACY_PROGRESS_EVENT_TYPE_PM = 6
LEGACY_PROGRESS_EVENT_TYPE_CLIENT = 7
LEGACY_PROGRESS_EVENT_TYPE_MILESTONE_INTERNAL = 8
LEGACY_PROGRESS_EVENT_TYPE_CLIENT_MID_SPRINT = 9

# Progress Report Status
LEGACY_PROGRESS_REPORT_STATUS_ON_SCHEDULE = 1
LEGACY_PROGRESS_REPORT_STATUS_BEHIND = 2
LEGACY_PROGRESS_REPORT_STATUS_STUCK = 3
LEGACY_PROGRESS_REPORT_STATUS_BEHIND_BUT_PROGRESSING = 4
LEGACY_PROGRESS_REPORT_STATUS_BEHIND_AND_STUCK = 5

# Progress Report Stuck Reason
LEGACY_PROGRESS_REPORT_STUCK_REASON_ERROR = 1
LEGACY_PROGRESS_REPORT_STUCK_REASON_POOR_DOC = 2
LEGACY_PROGRESS_REPORT_STUCK_REASON_HARDWARE = 3
LEGACY_PROGRESS_REPORT_STUCK_REASON_UNCLEAR_SPEC = 4
LEGACY_PROGRESS_REPORT_STUCK_REASON_PERSONAL = 5
LEGACY_PROGRESS_REPORT_STUCK_REASON_OTHER = 6

# Integration Types
INTEGRATION_TYPE_REPO = 1
INTEGRATION_TYPE_ISSUE = 2

# Rating Criteria
RATING_CRITERIA_CODING = 1
RATING_CRITERIA_COMMUNICATION = 2
RATING_CRITERIA_SPEED = 3

# Months
MONTHS = (
    (1, 'Jan'),
    (2, 'Feb'),
    (3, 'Mar'),
    (4, 'Apr'),
    (5, 'May'),
    (6, 'Jun'),
    (7, 'Jul'),
    (8, 'Aug'),
    (9, 'Sep'),
    (10, 'Oct'),
    (11, 'Nov'),
    (12, 'Dec')
)

# Country Codes
COUNTRY_CODE_UGANDA = '256'
COUNTRY_CODE_TANZANIA = '255'
COUNTRY_CODE_NIGERIA = '234'


# Contact request item
CONTACT_REQUEST_ITEM_DO_IT_YOURSELF = "self_guided"
CONTACT_REQUEST_ITEM_ONBOARDING = "onboarding"
CONTACT_REQUEST_ITEM_ONBOARDING_SPECIAL = "onboarding_special"
CONTACT_REQUEST_ITEM_PROJECT = "project"

SESSION_VISITOR_EMAIL = 'visitor_email'

HEADER_EDIT_TOKEN = 'HTTP_X_EDIT_TOKEN'

# Transaction and Action Statuses
SKILL_TYPE_LANGUAGE = 'language'
SKILL_TYPE_FRAMEWORK = 'framework'
SKILL_TYPE_PLATFORM = 'platform'
SKILL_TYPE_LIBRARY = 'library'
SKILL_TYPE_STORAGE = 'storage'
SKILL_TYPE_API = 'api'
SKILL_TYPE_OTHER = 'other'

SKILL_TYPE_CHOICES = (
    (SKILL_TYPE_LANGUAGE, 'Language'),
    (SKILL_TYPE_FRAMEWORK, 'Framework'),
    (SKILL_TYPE_PLATFORM, 'Platform'),
    (SKILL_TYPE_LIBRARY, 'Library'),
    (SKILL_TYPE_STORAGE, 'Storage Engine'),
    (SKILL_TYPE_API, 'API'),
    (SKILL_TYPE_OTHER, 'Other')
)

# Document types
DOC_ESTIMATE = 'estimate'
DOC_PROPOSAL = 'proposal'
DOC_PLANNING = 'planning'
DOC_REQUIREMENTS = 'requirements'
DOC_WIREFRAMES = 'wireframes'
DOC_TIMELINE = 'timeline'
DOC_OTHER = 'other'

PROJECT_DOCUMENT_CHOICES = (
    (DOC_ESTIMATE, 'Estimate'),
    (DOC_PROPOSAL, 'Proposal'),
    (DOC_PLANNING, 'Planning'),
    (DOC_REQUIREMENTS, 'Requirements Document'),
    (DOC_WIREFRAMES, 'Wireframes'),
    (DOC_TIMELINE, 'Timeline'),
    (DOC_OTHER, 'Other')
)


# VAT Locations
VAT_LOCATION_NL = 'NL'
VAT_LOCATION_EUROPE = 'europe'
VAT_LOCATION_WORLD = 'world'

# Project Types
PROJECT_TYPE_WEB = 'web'
PROJECT_TYPE_MOBILE = 'mobile'
PROJECT_TYPE_OTHER = 'other'

PROJECT_TYPE_CHOICES = (
    (PROJECT_TYPE_WEB, 'Web'),
    (PROJECT_TYPE_MOBILE, 'Mobile'),
    (PROJECT_TYPE_OTHER, 'Other')
)

# Project Types
PROJECT_DURATION_2_WEEKS = '2w'
PROJECT_DURATION_6_MONTHS = '6m'
PROJECT_DURATION_PERMANENT = 'permanent'

PROJECT_EXPECTED_DURATION_CHOICES = (
    (PROJECT_DURATION_2_WEEKS, '2 Weeks'),
    (PROJECT_DURATION_6_MONTHS, '6 Months'),
    (PROJECT_DURATION_PERMANENT, 'Permanent')
)

INVOICE_TYPE_CLIENT = 'client'
INVOICE_TYPE_DEVELOPER = 'developer'
INVOICE_TYPE_TUNGA = 'tunga'
INVOICE_TYPE_SALE = 'sale'
INVOICE_TYPE_PURCHASE = 'purchase'

INVOICE_TYPE_CHOICES = (
    (INVOICE_TYPE_SALE, 'Sales Invoice'),
    (INVOICE_TYPE_PURCHASE, 'Purchase Invoice'),
    (INVOICE_TYPE_CLIENT, 'Client'),
    (INVOICE_TYPE_TUNGA, 'Tunga'),
    (INVOICE_TYPE_DEVELOPER, 'Developer'),
)

PAYMENT_TYPE_SALE = 'sale'
PAYMENT_TYPE_PURCHASE = 'purchase'

PROGRESS_EVENT_DEVELOPER = 'developer'
PROGRESS_EVENT_PM = 'pm'
PROGRESS_EVENT_CLIENT = 'client'
PROGRESS_EVENT_MILESTONE = 'milestone'
PROGRESS_EVENT_INTERNAL = 'internal'

PROGRESS_EVENT_TYPE_CHOICES = (
    (PROGRESS_EVENT_DEVELOPER, 'Developer Update'),
    (PROGRESS_EVENT_PM, 'PM Report'),
    (PROGRESS_EVENT_CLIENT, 'Client Survey'),
    (PROGRESS_EVENT_MILESTONE, 'Milestone'),
    (PROGRESS_EVENT_INTERNAL, 'Internal Milestone')
)

# Progress Report Status
PROGRESS_REPORT_STATUS_ON_SCHEDULE = 'on_schedule'
PROGRESS_REPORT_STATUS_BEHIND = 'behind'
PROGRESS_REPORT_STATUS_STUCK = 'stuck'
PROGRESS_REPORT_STATUS_BEHIND_BUT_PROGRESSING = 'behind_progressing'
PROGRESS_REPORT_STATUS_BEHIND_AND_STUCK = 'behind_stuck'

# Progress Report Stuck Reason
PROGRESS_REPORT_STUCK_REASON_ERROR = 'resolving_error'
PROGRESS_REPORT_STUCK_REASON_POOR_DOC = 'poor_doc'
PROGRESS_REPORT_STUCK_REASON_HARDWARE = 'hardware_problem'
PROGRESS_REPORT_STUCK_REASON_UNCLEAR_SPEC = 'unclear_spec'
PROGRESS_REPORT_STUCK_REASON_PERSONAL = 'personal_issue'
PROGRESS_REPORT_STUCK_REASON_OTHER = 'other'


PROGRESS_REPORT_STATUS_CHOICES = (
    (PROGRESS_REPORT_STATUS_ON_SCHEDULE, 'On schedule'),
    (PROGRESS_REPORT_STATUS_BEHIND, 'Behind'),
    (PROGRESS_REPORT_STATUS_STUCK, 'Stuck'),
    (PROGRESS_REPORT_STATUS_BEHIND_BUT_PROGRESSING, 'Behind but Progressing'),
    (PROGRESS_REPORT_STATUS_BEHIND_AND_STUCK, 'Behind and Stuck')
)

PROGRESS_REPORT_STUCK_REASON_CHOICES = (
    (PROGRESS_REPORT_STUCK_REASON_ERROR, 'Resolving an Error'),
    (PROGRESS_REPORT_STUCK_REASON_POOR_DOC, 'Poor Documentation'),
    (PROGRESS_REPORT_STUCK_REASON_HARDWARE, 'Hardware problem'),
    (PROGRESS_REPORT_STUCK_REASON_UNCLEAR_SPEC, 'Unclear specifications'),
    (PROGRESS_REPORT_STUCK_REASON_PERSONAL, 'Personal Circumstances'),
    (PROGRESS_REPORT_STUCK_REASON_OTHER, 'Other'),
)

INVOICE_PAYMENT_METHOD_CHOICES = (
    (None, 'Any'),
    (PAYMENT_METHOD_STRIPE, 'Pay with Stripe'),
    (PAYMENT_METHOD_BITONIC, 'Pay with iDeal / mister cash'),
    (PAYMENT_METHOD_BITCOIN, 'Pay with BitCoin'),
    (PAYMENT_METHOD_BANK, 'Pay by bank transfer')
)

NOTIFICATION_TYPE_PROFILE = 'profile'
NOTIFICATION_TYPE_ACTIVITY = 'activity'

NOTIFICATION_TYPE_CHOICES = (
    (NOTIFICATION_TYPE_PROFILE, 'Profile'),
    (NOTIFICATION_TYPE_ACTIVITY, 'Activity')
)

# Project Stages
PROJECT_STAGE_OPPORTUNITY = 'opportunity'
PROJECT_STAGE_ACTIVE = 'active'

PROJECT_STAGE_CHOICES = (
    (PROJECT_STAGE_OPPORTUNITY, 'Opportunity'),
    (PROJECT_STAGE_ACTIVE, 'Active')
)

EVENT_SOURCE_HUBSPOT = 'hubspot'
