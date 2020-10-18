from . import auth
from googleapiclient.discovery import build


def _getService(scopes):
    creds = auth.getCreds(scopes)
    return build('gmail', 'v1', credentials=creds)


def getReadonlyService():
    return _getService(['https://www.googleapis.com/auth/gmail.readonly'])


def getProfile():
    service = getReadonlyService()
    usersService = service.users()

    request = usersService.getProfile(userId='me')
    profile = request.execute()

    return profile
