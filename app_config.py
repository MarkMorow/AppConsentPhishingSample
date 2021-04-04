import os

CLIENT_ID = "Enter_the_Application_Id_here" # Application (client) ID of app registration

CLIENT_SECRET = "Enter_CLIENT_SECRET_here"  # Placeholder - for use ONLY during testing.
# In a production app, I recommend you use a more secure method of storing your secret,
# like Azure Key Vault. Or, use an environment variable as described in Flask's documentation:
# https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
# CLIENT_SECRET = os.getenv("CLIENT_SECRET")
# if not CLIENT_SECRET:
#     raise ValueError("Need to define CLIENT_SECRET environment variable")

AUTHORITY = "https://login.microsoftonline.com/organizations"  # For multi-tenant app
# AUTHORITY = "https://login.microsoftonline.com/Enter_the_Tenant_Name_Here" # Update for single-tenant app

REDIRECT_PATH = "/getAToken"  # Used for forming an absolute URL to your redirect URI.
                              # The absolute URL must match the redirect URI you set
                              # in the app's registration in the Azure portal.

# You can find more Microsoft Graph API endpoints from Graph Explorer
# https://developer.microsoft.com/en-us/graph/graph-explorer
ENDPOINT = 'https://graph.microsoft.com/v1.0/users'  # This resource requires no admin consent
# ENDPOINTMAIL = 'https://graph.microsoft.com/v1.0/me/messages'  # Uncomment this with below additional scope to also let the sample app read mail. 

# You can find the proper permission names from this document
# https://docs.microsoft.com/en-us/graph/permissions-reference
SCOPE = ["User.ReadBasic.All"]
# SCOPE = ["User.ReadBasic.All Mail.Read"] #Additional permissions updated to also query the mail for the user. Uncomment this or add to the orginal SCOPE

SESSION_TYPE = "filesystem"  # Specifies the token cache should be stored in server-side session
