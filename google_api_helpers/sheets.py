from . import auth
from googleapiclient.discovery import build


def _getService(scopes):
    creds = auth.getCreds(scopes)
    return build('sheets', 'v4', credentials=creds)


def getReadonlyService():
    return _getService(['https://www.googleapis.com/auth/spreadsheets.readonly'])


def getService():
    return _getService(['https://www.googleapis.com/auth/spreadsheets'])


def getValues(spreadsheetId, range):
    service = getReadonlyService()
    valuesService = service.spreadsheets().values()
    request = valuesService.get(spreadsheetId=spreadsheetId,
                                range=range)
    response = request.execute()

    values = response.get('values', [])
    return values


def get(spreadsheetId, includeGridData=False):
    service = getReadonlyService()
    spreadsheetsService = service.spreadsheets()
    request = spreadsheetsService.get(
        spreadsheetId=spreadsheetId, includeGridData=includeGridData)
    response = request.execute()

    return response


def batchUpdate(spreadsheetId, range, data):
    service = getService()
    batch_update_values_request_body = {
        'value_input_option': 'RAW',
        'data': [
            {
                'range': range,
                'majorDimension': 'ROWS',
                'values': data
            }
        ],
    }
    valuesService = service.spreadsheets().values()
    request = valuesService.batchUpdate(
        spreadsheetId=spreadsheetId, body=batch_update_values_request_body)

    response = request.execute()
    return response


def addSheet(spreadsheetId, sheetName):

    requests = []

    requests.append({
        "addSheet": {
            "properties": {
                "title": sheetName,
            }
        }
    })

    body = {
        'requests': requests
    }

    service = getService()
    spreadsheetsService = service.spreadsheets()
    request = spreadsheetsService.batchUpdate(
        spreadsheetId=spreadsheetId, body=body)
    response = request.execute()

    return response


def create(data, title='api generated', startRow=0, startColumn=0):
    service = getService()

    rowData = []
    for row in data:
        rowDataCols = []
        for point in row:
            value = {
                "userEnteredValue": {
                    "stringValue": point,
                },
            }
            rowDataCols.append(value)
        rowDataRow = {
            "values": rowDataCols,
        }
        rowData.append(rowDataRow)

    body = {
        "properties": {
            "title": title
        },
        "sheets": [
            {
                "data": {
                    "rowData": rowData,
                    "startRow": startRow,
                    "startColumn": startColumn
                }
            },
        ]
    }
    spreadsheetsService = service.spreadsheets()
    request = spreadsheetsService.create(body=body)
    response = request.execute()
    return response['spreadsheetId']
