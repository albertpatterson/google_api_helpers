from main import auth
from main import sheets
from googleapiclient.discovery import build
from main import drive

SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
creds = auth.getCreds(SCOPES)
service = build('sheets', 'v4', credentials=creds)

ANIME_TITLES_SPREADSHEET_ID = '1JAa5lpck1-jq1hi3q9Z04QPpJ3WeNhljFwbPOzPGhAw'

# data = sheets.getValues(service, ANIME_TITLES_SPREADSHEET_ID, "A:A")
data = sheets.get(service, ANIME_TITLES_SPREADSHEET_ID)

print('fetched data', data)

# # id = sheets.create(service, [['pickle', 'apple'], [
# #     'junk', 'derp', 'dirt']])

# # print('created ', id)


# SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']
# creds = auth.getCreds(SCOPES)
# service = build('drive', 'v3', credentials=creds)
# drive.list(
#     service, q="mimeType='application/vnd.google-apps.spreadsheet' and trashed=false and name contains 'flashcard'")


# id = drive.createBlankSheet('testing', ['1XpeKvLANuIoeG1278eZQZITQB8N-O6oS'])
# print('created ', id)
