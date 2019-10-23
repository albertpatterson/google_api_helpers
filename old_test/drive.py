from main import drive


def list():
    print()
    print('list:')
    results = drive.list(
        q="mimeType='application/vnd.google-apps.spreadsheet' and trashed=false")
    print('results ', results)


def createBlankSheet():
    print()
    print('creacreateBlankSheette:')
    id = drive.createBlankSheet(
        'testing', ['1XpeKvLANuIoeG1278eZQZITQB8N-O6oS'])

    print('created ', id)


createBlankSheet()
list()
