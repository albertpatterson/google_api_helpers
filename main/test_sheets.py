from . import auth
from . import drive
from . import sheets as spreadsheets
from .utils.test import drive as test_drive
import pytest


@pytest.fixture(scope="session", autouse=True)
def getTestCredentials():
    return test_drive.getTestCredentials()


class TestDrive(test_drive.WithDriveCleaningFixture):
    def test_create(self):
        testName = 'testing_create_sheet'
        testData = [[]]
        createdSheetId = spreadsheets.create(testData, testName)

        contents = drive.list()
        createdSheet = {'id': createdSheetId, 'name': testName}

        assert contents == [createdSheet]

    def test_get(self):
        testName = 'testing_create_sheet'
        testData = [['apple', 'banana'], ['carrot']]
        createdSheetId = spreadsheets.create(testData, testName)

        spreadsheet = spreadsheets.get(createdSheetId, True)

        assert spreadsheet != None
        assert spreadsheet['spreadsheetId'] == createdSheetId
        assert spreadsheet['properties']['title'] == testName
        sheets = spreadsheet['sheets']

        assert len(sheets) == 1

        gridData = []
        sheetDataRows = sheets[0]['data'][0]['rowData']
        for row in sheetDataRows:
            rowDataValues = row['values']
            rowRawValues = []
            for rowDataValue in rowDataValues:
                stringValue = rowDataValue['userEnteredValue']['stringValue']
                rowRawValues.append(stringValue)
            gridData.append(rowRawValues)

        assert gridData == testData
s = {
    'spreadsheetId': '1RmHZF1xnhTKqPJlivzW9xUjkN6KfvX48w1TE0DsMpI8', 
    'properties': {
        'title': 'testing_create_sheet', 
        'locale': 'en_US', 
        'autoRecalc': 'ON_CHANGE', 
        'timeZone': 'Etc/GMT', 
        'defaultFormat': {
            'backgroundColor': {'red': 1, 'green': 1, 'blue': 1}, 
            'padding': {'top': 2, 'right': 3, 'bottom': 2, 'left': 3}, 
            'verticalAlignment': 'BOTTOM', 
            'wrapStrategy': 
            'OVERFLOW_CELL', 
            'textFormat': {
                'foregroundColor': {}, 
                'fontFamily': 'arial,sans,sans-serif', 
                'fontSize': 10, 
                'bold': False, 
                'italic': False, 
                'strikethrough': False, 
                'underline': False
                }
            }
        }, 
        'sheets': [
            {
                'properties': {
                    'sheetId': 196789550, 
                    'title': 'Sheet1', 
                    'index': 0, 
                    'sheetType': 'GRID', 
                    'gridProperties': {
                        'rowCount': 1000, 
                        'columnCount': 26
                    }
                }, 
                'data': [
                    {
                        'rowData': [
                            {
                                'values': [
                                    {
                                        'userEnteredValue': {'stringValue': 'apple'}, 
                                        'effectiveValue': {'stringValue': 'apple'}, 
                                        'formattedValue': 'apple', 
                                        'effectiveFormat': {
                                            'backgroundColor': {'red': 1, 'green': 1, 'blue': 1}, 
                                            'padding': {'top': 2, 'right': 3, 'bottom': 2, 'left': 3}, 
                                            'horizontalAlignment': 'LEFT', 
                                            'verticalAlignment': 'BOTTOM', 
                                            'wrapStrategy': 'OVERFLOW_CELL', 
                                            'textFormat': {
                                                'foregroundColor': {}, 
                                                'fontFamily': 'Arial', 
                                                'fontSize': 10, 
                                                'bold': False, 
                                                'italic': False, 
                                                'strikethrough': False, 
                                                'underline': False
                                            }, 
                                            'hyperlinkDisplayType': 'PLAIN_TEXT'
                                        }
                                    }, 
                                    {
                                        'userEnteredValue': {'stringValue': 'banana'}, 
                                        'effectiveValue': {'stringValue': 'banana'}, 
                                        'formattedValue': 'banana', 
                                        'effectiveFormat': {
                                            'backgroundColor': {'red': 1, 'green': 1, 'blue': 1}, 'padding': {'top': 2, 'right': 3, 'bottom': 2, 'left': 3}, 
                                            'horizontalAlignment': 'LEFT', 'verticalAlignment': 'BOTTOM', 'wrapStrategy': 'OVERFLOW_CELL', 
                                            'textFormat': {'foregroundColor': {}, 'fontFamily': 'Arial', 'fontSize': 10, 'bold': False, 'italic': False, 'strikethrough': False, 'underline': False}, 
                                            'hyperlinkDisplayType': 'PLAIN_TEXT'
                                        }
                                    }
                                ]
                            }, 
                            {
                                'values': [
                                    {
                                        'userEnteredValue': {'stringValue': 'carrot'}, 
                                        'effectiveValue': {'stringValue': 'carrot'}, 
                                        'formattedValue': 'carrot', 
                                        'effectiveFormat': {'backgroundColor': {'red': 1, 'green': 1, 'blue': 1}, 'padding': {'top': 2, 'right': 3, 'bottom': 2, 'left': 3}, 'horizontalAlignment': 'LEFT', 'verticalAlignment': 'BOTTOM', 'wrapStrategy': 'OVERFLOW_CELL', 'textFormat': {'foregroundColor': {}, 'fontFamily': 'Arial', 'fontSize': 10, 'bold': False, 'italic': False, 'strikethrough': False, 'underline': False}, 'hyperlinkDisplayType': 'PLAIN_TEXT'
                                        }
                                    }
                                ]
                            }
                        ], 
                        'rowMetadata': [{'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}, {'pixelSize': 21}], 'columnMetadata': [{'pixelSize': 100}, {'pixelSize': 100}, {'pixelSize': 100}, {'pixelSize': 100}, {'pixelSize': 100}, {'pixelSize': 100}, {'pixelSize': 100}, {'pixelSize': 100}, {'pixelSize': 100}, {'pixelSize': 100}, {'pixelSize': 100}, {'pixelSize': 100}, {'pixelSize': 100}, {'pixelSize': 100}, {'pixelSize': 100}, {'pixelSize': 100}, {'pixelSize': 100}, {'pixelSize': 100}, {'pixelSize': 100}, {'pixelSize': 100}, {'pixelSize': 100}, {'pixelSize': 100}, {'pixelSize': 100}, {'pixelSize': 100}, {'pixelSize': 100}, {'pixelSize': 100}]}]}], 'spreadsheetUrl': 'https://docs.google.com/spreadsheets/d/1RmHZF1xnhTKqPJlivzW9xUjkN6KfvX48w1TE0DsMpI8/edit'}                                                                                                                                                            