from google_api_helpers import email
import pytest

from test.utils import auth as test_auth


@pytest.fixture(scope="session", autouse=True)
def getTestCredentials():
    return test_auth.getTestCredentials()


class TestEmail(test_auth.WithUserAssertingFixture):
    def testGetProfile(self):
        profile = email.getProfile()
        print(profile)
        assert profile['emailAddress'] == 'apatterson189.test@gmail.com'
