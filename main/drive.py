# def list(service, q=""):
#     filesService = service.files()
#     results = filesService.list(
#         pageSize=10, fields="nextPageToken, files(id, name)").execute()

#     print(results)

#     items = results.get('files', [])

#     if not items:
#         print('No files found.')
#     else:
#         print('Files:')
#         for item in items:
#             print(u'{0} ({1})'.format(item['name'], item['id']))
from enum import Enum
from main import auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# SCOPES = {
#     'drive.metadata.readonly': 'https://www.googleapis.com/auth/drive.metadata.readonly',
#     'drive.metadata': 'https://www.googleapis.com/auth/drive.metadata',
#     'drive.readonly': 'https://www.googleapis.com/auth/drive.readonly',
#     'drive': 'https://www.googleapis.com/auth/drive,'
# }


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
        # for file in response.get('files', []):
        #     # Process change
        #     print 'Found file: %s (%s)' % (file.get('name'), file.get('id'))
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


# def _retryInsuffientScope(function):
#     try:
#         return function()
#     except HttpError as httpError:
#         if httpError.resp['www-authenticate'].find('insufficient_scope') != -1:
#             auth.clearToken()
#             print('clear token and retry')
#             return function()
#         else:
#             raise httpError


def createBlankSheet(name, parents):
    return createBlank(name, parents, 'application/vnd.google-apps.spreadsheet')


def delete(id):
    return getService().files().delete(fileId=id).execute()
