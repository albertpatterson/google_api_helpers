import pickle
import os.path
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os
from googleapiclient.errors import HttpError

dirname = os.path.dirname(__file__)
storedTokenLocation = os.path.join(dirname, 'not_shared/token.pickle')
storedCredentialsLocation = os.path.join(
    dirname, 'not_shared/credentials.json')


def _getExistingCreds():
    existingCreds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(storedTokenLocation):
        with open(storedTokenLocation, 'rb') as token:
            existingCreds = pickle.load(token)

    return existingCreds


def _storeCreds(creds):
    with open(storedTokenLocation, 'wb') as token:
        pickle.dump(creds, token)


def getCreds(scopes, resetScopes=False, credentialsLocation=storedCredentialsLocation):

    allScopes = list(scopes)

    creds = _getExistingCreds()

    if creds and not resetScopes:
        allScopes += list(set(creds.scopes))

    # cred exist for all required scope but are expired
    if creds and creds.has_scopes(allScopes):
        if creds.expired and creds.refresh_token:
            creds.refresh(Request())
        # else do nothing, old creds are ok
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            credentialsLocation, allScopes)
        creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        _storeCreds(creds)

    return creds


# def _hasAllScopes(creds, scopes):
    # hasAll = True
    # print(creds)
    # for scope in scopes:
    #     hasAll = hasAll and creds.has_scopes(scopes)
    #     if not hasAll:
    #         break
    # return hasAll


# def retyWithExpandedScope(operation, requiredScopes):
#     try:
#         return operation()
#     except HttpError as httpError:
#         if httpError.resp['www-authenticate'].find('insufficient_scope') != -1:
#             getCreds(requiredScopes)
#             return operation()
#         else:
#             raise httpError


def clearToken():
    os.remove(storedTokenLocation)
