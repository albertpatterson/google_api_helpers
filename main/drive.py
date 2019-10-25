from enum import Enum
from . import auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


class Scopes:
    drive_metadata_readonly = 'https://www.googleapis.com/auth/drive.metadata.readonly'
    drive_metadata = 'https://www.googleapis.com/auth/drive.metadata'
    drive_readonly = 'https://www.googleapis.com/auth/drive.readonly'
    drive = 'https://www.googleapis.com/auth/drive'


class MimeTypes:
    sheet = 'application/vnd.google-apps.spreadsheet'


def _getService(scopes):
    creds = auth.getCreds(scopes)
    return build('drive', 'v3', credentials=creds)


def getMetadataReadonlyService():
    return _getService(['https://www.googleapis.com/auth/drive.metadata.readonly'])


def getMetadataService():
    return _getService(['https://www.googleapis.com/auth/drive.metadata'])


def getReadonlyService():
    return _getService(['https://www.googleapis.com/auth/drive.readonly'])


def getService():
    return _getService(['https://www.googleapis.com/auth/drive'])


def getMetadataReadonlyService():
    return _getService(['https://www.googleapis.com/auth/drive.metadata.readonly'])


def list(q=""):
    service = getMetadataReadonlyService()
    filesService = service.files()

    files = []
    page_token = None
    while True:
        response = filesService.list(q=q,
                                     spaces='drive',
                                     fields='nextPageToken, files(id, name, description)',
                                     pageToken=page_token).execute()
        files += response['files']

        page_token = response.get('nextPageToken', None)
        if page_token is None:
            break
    return files


def createBlank(name, parents, mimeType):
    body = {
        'name': name,
        'parents': parents,
        'mimeType': mimeType,
    }
    response = getService().files().create(body=body).execute()
    return response['id']


def createBlankSheet(name, parents):
    return createBlank(name, parents, 'application/vnd.google-apps.spreadsheet')


def delete(id):
    return getService().files().delete(fileId=id).execute()
