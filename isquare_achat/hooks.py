app_name = "isquare_achat"
app_title = "ISquare Achat"
app_publisher = "ISquare SARL"
app_description = "Module Achat ISquare SARL"
app_email = "admin@isquare.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "isquare_achat",
# 		"logo": "/assets/isquare_achat/logo.png",
# 		"title": "ISquare Achat",
# 		"route": "/isquare_achat",
# 		"has_permission": "isquare_achat.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/isquare_achat/css/isquare_achat.css"
# app_include_js = "/assets/isquare_achat/js/isquare_achat.js"

# include js, css files in header of web template
# web_include_css = "/assets/isquare_achat/css/isquare_achat.css"
# web_include_js = "/assets/isquare_achat/js/isquare_achat.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "isquare_achat/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "isquare_achat/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# automatically load and sync documents of this doctype from downstream apps
# importable_doctypes = [doctype_1]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "isquare_achat.utils.jinja_methods",
# 	"filters": "isquare_achat.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "isquare_achat.install.before_install"
# after_install = "isquare_achat.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "isquare_achat.uninstall.before_uninstall"
# after_uninstall = "isquare_achat.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "isquare_achat.utils.before_app_install"
# after_app_install = "isquare_achat.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "isquare_achat.utils.before_app_uninstall"
# after_app_uninstall = "isquare_achat.utils.after_app_uninstall"

# Build
# ------------------
# To hook into the build process

# after_build = "isquare_achat.build.after_build"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "isquare_achat.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"isquare_achat.tasks.all"
# 	],
# 	"daily": [
# 		"isquare_achat.tasks.daily"
# 	],
# 	"hourly": [
# 		"isquare_achat.tasks.hourly"
# 	],
# 	"weekly": [
# 		"isquare_achat.tasks.weekly"
# 	],
# 	"monthly": [
# 		"isquare_achat.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "isquare_achat.install.before_tests"

# Extend DocType Class
# ------------------------------
#
# Specify custom mixins to extend the standard doctype controller.
# extend_doctype_class = {
# 	"Task": "isquare_achat.custom.task.CustomTaskMixin"
# }

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "isquare_achat.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "isquare_achat.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["isquare_achat.utils.before_request"]
# after_request = ["isquare_achat.utils.after_request"]

# Job Events
# ----------
# before_job = ["isquare_achat.utils.before_job"]
# after_job = ["isquare_achat.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"isquare_achat.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []


# Fixtures
# --------
fixtures = [
    {
        "doctype": "DocType",
        "filters": [["name", "in", [
            "Demande Achat ISQ",
            "Demande Achat ISQ Article",
            "Fournisseur ISQ",
            "Fournisseur Article ISQ",
            "Bon de Commande ISQ",
            "BC ISQ Item",
            "Bon de Reception ISQ",
            "BR ISQ ART",
            "Demande de Devis ISQ",
            "DD ISQ Article",
            "DD ISQ Fournisseur",
            "DD ISQ Synthese",
            "Bon de Reglement ISQ",
            "Bon Execution ISQ",
            "Client ISQ"
        ]]]
    },
    "Workflow",
    "Workflow State",
    "Workflow Action Master",
    "Custom Field",
    "Property Setter",
    "Client Script",
    "Server Script",
    "Workspace",
    "Role"
]
