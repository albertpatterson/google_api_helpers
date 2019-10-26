from ... import auth
from ... import drive
import os
import pytest
from pathlib import Path


def cleanDrive():
    allContents = drive.list()
    for item in allContents:
        drive.delete(item['id'])


def getTestCredentials():
    maindir = Path(os.path.dirname(__file__)).parent.parent
    testCredentialsLocation = storedCredentialsLocation = os.path.join(
        maindir, 'not_shared/test_credentials.json')
    auth.setStoredCredentialsLocation(testCredentialsLocation)


class WithDriveCleaningFixture:
    @pytest.fixture(autouse=True)
    def cleanDriveBeforeAndAfter(self):
        cleanDrive()
        yield
        cleanDrive()
