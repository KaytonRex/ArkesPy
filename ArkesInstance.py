from exchangelib import DELEGATE, Account, Credentials, Configuration
import ArkesUtility as AU
import os
import datetime
import json

with open(os.path.join(os.getcwd(),"Config.json")) as f:
    ArkesConfig = json.load(f)

def ExchangeAccountSetup():
    # Connect to Exchange
    if ArkesConfig.get("ExchangeType").upper() == "ON-PREMISE LOCAL":
        AU.LoggingFile("TRACE", f"Exchange Setup: Connecting to On-Premise (Local)")
        credentials = Credentials(username='MYWINDOMAIN\\myuser', password='topsecret')
    elif ArkesConfig.get("ExchangeType").upper() == "ON-PREMISE DOMAIN":
        AU.LoggingFile("TRACE", f"Exchange Setup Connecting to On-Premise (Domain)")
    elif ArkesConfig.get("ExchangeType").upper() == "OFFICE365 BASIC":
        AU.LoggingFile("TRACE", f"Exchange Setup Connecting to Office365 (Basic)")
        # Outlook Options On-Premise Local, On-Premise Domain, Office365 Basic, Office365 oAuth
        credentials = Credentials(
            username = ArkesConfig.get("EmailAddress"),
            password = ArkesConfig.get("EmailPassword"))
        config = Configuration(server='outlook.office365.com', credentials=credentials)
        account = Account(primary_smtp_address=ArkesConfig.get("EmailAddress"), config=config,
                    autodiscover=False, access_type=DELEGATE)
        return account
    elif ArkesConfig.get("ExchangeType").upper() == "OFFICE365 OAUTH":
        AU.LoggingFile("TRACE", f"Exchange Setup Connecting to Office365 (oAuth)")
    else:
        print("Issue")
        exit()

def ExchangeFolderConfig(ExchangeAccount):
    try:
        if ArkesConfig.get("ExchangeParentFolder").upper() == "INBOX":
            ExchangeParentFolder = ExchangeAccount.inbox
        else:
            ExchangeParentFolder = ExchangeAccount.inbox / ArkesConfig.get("ExchangeParentFolder")
        if ArkesConfig.get("ExchangeAwaitingFolder") == ArkesConfig.get("ExchangeParentFolder"):
            ExchangeAwaitingFolder = ExchangeParentFolder
        else:
            ExchangeAwaitingFolder = ExchangeParentFolder / ArkesConfig.get("ExchangeAwaitingFolder")
        ExchangeSuccessfulFolder = ExchangeParentFolder / ArkesConfig.get("ExchangeSuccessfulFolder")
        ExchangeFailedFolder = ExchangeParentFolder / ArkesConfig.get("ExchangeFailedFolder")

        return ExchangeAwaitingFolder, ExchangeSuccessfulFolder, ExchangeFailedFolder
    except Exception as e:
            AU.LoggingFile("ERROR",f"Exchange Folder Selections Failed. Following error message reported: {e}")
            exit()

def ExchangeEmailProcessing(ExchangeAwaitingFolder, ExchangeSuccessfulFolder, ExchangeFailedFolder):
    AwaitingEmails = ExchangeAwaitingFolder.all()[:100]
    for email in AwaitingEmails:
        if email.has_attachments:
            # Download Email Attachments
            try:
                print(email.sender.email_address, email.subject)
                for attachment in email.attachments:
                    local_path = f"C:\\Users\\Kayto\\Documents\\GitHub\\ArkesPy\\Temp\\{email.sender.email_address} {email.subject} {attachment.name}"
                    with open(local_path, 'wb') as f:
                        f.write(attachment.content)
            except Exception as e:
                AU.LoggingFile("ERROR",f"Exchange Folder Selections Failed. Following error message reported: {e}")
        else:
            # No Email, move email to failed folder
            try:
                email.move(ExchangeFailedFolder)
                AU.LoggingFile("TRACE",f"The following email, has no attachments: {email.sender.email_address} {email.subject}")
            except Exception as e:
                AU.LoggingFile("ERROR",f"Exchange Folder Selections Failed. Following error message reported: {e}")
