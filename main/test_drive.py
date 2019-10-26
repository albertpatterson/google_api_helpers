from . import auth
from . import drive
from .utils.test import drive as test_drive
import pytest


@pytest.fixture(scope="session", autouse=True)
def getTestCredentials():
    return test_drive.getTestCredentials()


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
