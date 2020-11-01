from google_api_helpers import auth
from google_api_helpers import drive
from google_api_helpers import email
from test.utils import auth as test_auth
import os
import pytest
from pathlib import Path


def cleanDrive():
    allContents = drive.list()
    for item in allContents:
        drive.delete(item['id'])


class WithDriveCleaningFixture(test_auth.WithUserAssertingFixture):
    @pytest.fixture(autouse=True)
    def cleanDriveBeforeAndAfter(self):
        cleanDrive()
        yield
        cleanDrive()
