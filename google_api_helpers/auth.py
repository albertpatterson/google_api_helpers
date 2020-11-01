import pickle
import os.path
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os
from googleapiclient.errors import HttpError
from pathlib import Path

dirname = os.path.dirname(__file__)
storedTokenLocation = None
storedCredentialsLocation = None


def setStoredCredentialsLocation(location):
    global storedCredentialsLocation
    global storedTokenLocation
    storedCredentialsLocation = location
    storedTokenLocation = None if location == None else _getStoredTokenLocation(
        location)


def clearStoredCredentialsLocation(location):
    setStoredCredentialsLocation(None)


def _getExistingCreds():

    if(storedTokenLocation == None):
        return None

    existingCreds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(storedTokenLocation):
        with open(storedTokenLocation, 'rb') as token:
            existingCreds = pickle.load(token)

    return existingCreds


def _storeCreds(creds):
    if(storedTokenLocation == None):
        raise Exception("stored token locaion not set")

    with open(storedTokenLocation, 'wb') as token:
        pickle.dump(creds, token)


def getCreds(scopes, resetScopes=False):

    if(storedCredentialsLocation == None):
        raise Exception("stored credential locaion not set")

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
            storedCredentialsLocation, allScopes)
        creds = flow.run_local_server(port=0)
        # Save the credentials for the next run

        _storeCreds(creds)

    return creds


def _getStoredTokenLocation(storedCredentialsLocation):
    return os.path.join(Path(storedCredentialsLocation).parent, 'token.pickle')


def clearStoredToken():
    storedTokenLocation = _getStoredTokenLocation(
        storedCredentialsLocation)
    os.remove(storedTokenLocation)
