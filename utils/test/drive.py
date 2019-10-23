from main import auth
from main import drive
import os
import pytest


def cleanDrive():
    allContents = drive.list()
    for item in allContents:
        print(item)
        drive.delete(item['id'])


def getTestCredentials():
    dirname = os.path.dirname(__file__)
    testCredentialsLocation = storedCredentialsLocation = os.path.join(
        dirname, 'not_shared/test_credentials.json')
    creds = auth.getCreds([drive.Scopes.drive],
                          True, testCredentialsLocation)
    return creds


class WithDriveCleaningFixture:
    @pytest.fixture(autouse=True)
    def cleanDriveBeforeAndAfter(self):
        cleanDrive()
        yield
        cleanDrive()
