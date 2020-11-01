from google_api_helpers import auth
from google_api_helpers import drive
from test.utils import drive as test_drive
from test.utils import auth as test_auth

import pytest


@pytest.fixture(scope="session", autouse=True)
def getTestCredentials():
    return test_auth.getTestCredentials()


class TestDrive(test_drive.WithDriveCleaningFixture):

    def test_list_empty(self):
        contents = drive.list()
        assert contents == []

    def test_createBlank(self):
        testName = "testing_created_blank"
        createdSheetId = drive.createBlank(testName, [], drive.MimeTypes.sheet)

        contents = drive.list()
        createdSheet = {'id': createdSheetId, 'name': testName}

        assert contents == [createdSheet]

    def test_createBlankSheet(self):
        testName = "testing_created_blank_sheet"
        createdSheetId = drive.createBlankSheet(testName, [])

        contents = drive.list()
        createdSheet = {'id': createdSheetId, 'name': testName}

        assert contents == [createdSheet]

    def test_list_filtered(self):
        testName1 = "testing_created_1"
        createdSheetId1 = drive.createBlank(
            testName1, [], drive.MimeTypes.sheet)

        testName2 = "testing_created_2"
        createdSheetId2 = drive.createBlank(
            testName2, [], drive.MimeTypes.sheet)

        testName3 = "testing_created_3"
        createdSheetId3 = drive.createBlank(
            testName3, [], drive.MimeTypes.sheet)

        matchedContents = drive.list("name = 'testing_created_2'")

        assert matchedContents == [
            {'id': createdSheetId2, 'name': testName2}
        ]
