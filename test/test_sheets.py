from google_api_helpers import auth
from google_api_helpers import drive
from google_api_helpers import sheets as spreadsheets
from test.utils import drive as test_drive
from test.utils import auth as test_auth

import pytest


@pytest.fixture(scope="session", autouse=True)
def getTestCredentials():
    return test_auth.getTestCredentials()


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

    def test_batchUpdate(self):
        testName = 'testing_create_sheet'
        testData = [[]]
        createdSheetId = spreadsheets.create(testData, testName)

        testData = [['apple', 'banana'], ['carrot']]

        spreadsheets.batchUpdate(createdSheetId, 'A:C', testData)

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

    def test_batchUpdate_and_create_new_sheet(self):
        testName = 'testing_create_sheet'
        testData = [[]]
        createdSheetId = spreadsheets.create(testData, testName)

        newSheetName = 'new_sheet'

        spreadsheets.addSheet(createdSheetId, newSheetName)

        spreadsheet = spreadsheets.get(createdSheetId, False)

        assert len(spreadsheet['sheets']) == 2
        assert spreadsheet['sheets'][-1]['properties']['title'] == newSheetName
