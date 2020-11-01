# google_api_helpers
Python helpers for using google apis

# Build
python3 setup.py sdist bdist_wheel

# install
pip install /path/to/wheelfile.whl

# upload
python3 -m twine upload dist/*

# test
python setup.py pytest

# Notes
* IMPORTANT: Run tests only with accounts for which important data is not stored in drive. The data may be lost.
* based on https://packaging.python.org/tutorials/packaging-projects/ and https://medium.com/analytics-vidhya/how-to-create-a-python-library-7d5aea80cc3f