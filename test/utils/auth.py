from google_api_helpers import auth
from google_api_helpers import email
from test.constants import TEST_USER_EMAIL_ADDRESS
import os
import pytest
from pathlib import Path


def getTestCredentials():
    maindir = Path(os.path.dirname(__file__)).parent.parent
    testCredentialsLocation = storedCredentialsLocation = os.path.join(
        maindir, 'not_shared/test_credentials.json')
    auth.setStoredCredentialsLocation(testCredentialsLocation)


class WithUserAssertingFixture:
    @pytest.fixture(autouse=True)
    def assertTestUser(self):
        profile = email.getProfile()
        print(profile)
        if(profile['emailAddress'] != TEST_USER_EMAIL_ADDRESS):
            pytest.fail(
                'tests must be run using %s.' % TEST_USER_EMAIL_ADDRESS)
