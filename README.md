# google_api_helpers
Python helpers for using google apis

# install
pip install apatterson189-google-api-helpers

# Setup
1) Create a GCP project
2) Create a set of credentials
3) download the credentials (as credentials.json for example)

The first step of using these tools should be to provide the credentials of the GCP project that will be used to access the data, via "google_api_helpers.auth.setStoredCredentialsLocation".

# usage 
import google_api_helpers

# Build
python3 setup.py sdist bdist_wheel

# Upload
python3 -m twine upload dist/*

# Test
python setup.py pytest

# Notes
* IMPORTANT: Run tests only with accounts for which important data is not stored in drive. The data may be lost.
* based on https://packaging.python.org/tutorials/packaging-projects/ and https://medium.com/analytics-vidhya/how-to-create-a-python-library-7d5aea80cc3f