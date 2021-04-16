# Sample "Malicious" Python Web Application Using Azure AD

## About this sample

> This sample has been modified from the Python quickstart for the Microsoft identity platform:
[Quickstart: Add sign-in with Microsoft to a Python web app]("https://docs.microsoft.com/azure/active-directory/develop/quickstart-v2-python-webapp")

### Overview

This sample is a demo Python web application that signs-in users with the Microsoft identity platform and calls the Microsoft Graph to list the directory. This can be used to show an application consent phishing attack.

1. The python web application uses the Microsoft Authentication Library (MSAL) to obtain a JWT access token from the Microsoft identity platform.
2. The access token is used as a bearer token to authenticate the user when calling the Microsoft Graph.
3. The first page of results of the directory query is shown.

## How to run this sample

To run this sample, you'll need:

> - [Python 3+](https://www.python.org/downloads/release/python-364/)
> - An Azure Active Directory (Azure AD) tenant. For more information on how to get an Azure AD tenant, see [how to get an Azure AD tenant.](https://docs.microsoft.com/azure/active-directory/develop/quickstart-create-new-tenant). Or sign up for a free developer tenant with sample data [here](https://developer.microsoft.com/en-us/microsoft-365/dev-program).

### Step 1:  Clone or download this repository

From your shell or command line:

```Shell
git clone https://github.com/MarkMorow/AppConsentPhishingSamplePublic.git
```

or download and extract the repository .zip file.

### Step 2:  Register the sample application with your Azure Active Directory tenant

To register it, you can:

- follow the steps [Step 2: Register the sample with your Azure Active Directory tenant](#step-2-register-the-sample-with-your-azure-active-directory-tenant) and [Step 3:  Configure the sample to use your Azure AD tenant](#choose-the-azure-ad-tenant-where-you-want-to-create-your-applications)

#### Choose the Azure AD tenant where you want to create your applications

As a first step you'll need to:

1. Sign in to the [Azure portal](https://portal.azure.com) using either a work or school account or a personal Microsoft account.
1. If your account is present in more than one Azure AD tenant, select your profile at the top right corner in the menu on top of the page, and then **switch directory**.
   Change your portal session to the desired Azure AD tenant.

#### Register the Sample "Malicious" Python Webapp

> Note: if you are using this application outside of a demo use certificates in step 7

1. Navigate to the Microsoft identity platform for developers [App registrations](https://go.microsoft.com/fwlink/?linkid=2083908) page.
1. Select **New registration**.
1. When the **Register an application page** appears, enter your application's registration information:
   - In the **Name** section, enter a name that will be displayed to users of the app. For example `python-webapp` if you are trying demonstate what an end user has access to. You might get more tricky if you are trying to actually try and phish someone internally.
   - Change **Supported account types** to **Accounts in any organizational directory (Any Azure AD directory - Multitenant)**.
   - In the Redirect URI (optional) section, select **Web** in the combo-box and enter the following redirect URIs: `http://localhost:5000/getAToken`.
1. Select **Register** to create the application.
1. On the app **Overview** page, find the **Application (client) ID** value and record it for later. You'll need it for the `app_config.py` file.
1. Select **Save**.
1. From the **Certificates & secrets** page, in the **Client secrets** section, choose **New client secret**:
   - Type a key description (of instance `app secret`),
   - Use the default key duration of **6 months** or choose a different one. Shorter is better.
   - When you press the **Add** button, the key **value** will be displayed, copy, and save the value in a safe location. Make sure to copy the **Value** field, not the ID.
   - You'll need this key later to configure the `app_config.py` file.. This key value will not be displayed again, nor retrievable by any other means,
     so record it as soon as it is visible from the Azure portal.
1. Select the **API permissions** section
   - Click the **Add a permission** button and then,
   - Ensure that the **Microsoft APIs** tab is selected
   - In the *Commonly used Microsoft APIs* section, click on **Microsoft Graph**
   - In the **Delegated permissions** section, ensure that the right permissions are checked: **User.ReadBasic.All**. Use the search box if necessary.
   - Select the **Add permissions** button

### Step 3:  Configure the sample to use your Azure AD tenant

In the steps below, "ClientID" is the same as "Application ID" or "AppId".

#### Configure the pythonwebapp

1. Open the `app_config.py` file
1. You saved your application secret during the creation of the `python-webapp` app in the Azure portal.
   Now you can set the secret in the variable `CLIENT_SECRET`.
1. Find the `CLIENT_ID` key and replace the existing `Enter_the_Application_Id_here` value with the application ID (clientId) of the `python-webapp` application copied from the Azure portal.

### Step 4: Run the sample

- You will need to install dependencies using pip as follows:

```Shell
pip install -r requirements.txt
```

Run app.py from shell or command line. Note that the host and port values need to match what you've set up in your redirect_uri:

```Shell
python3 app.py
```

## More information

For more information, see MSAL.Python's [conceptual documentation]("https://github.com/AzureAD/microsoft-authentication-library-for-python/wiki"):

For more information about web apps scenarios on the Microsoft identity platform see [Scenario: Web app that calls web APIs](https://docs.microsoft.com/en-us/azure/active-directory/develop/scenario-web-app-call-api-overview)

For more information about how OAuth 2.0 protocols work in this scenario and other scenarios, see [Authentication Scenarios for Azure AD](http://go.microsoft.com/fwlink/?LinkId=394414).
