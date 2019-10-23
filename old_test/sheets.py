from main import sheets

createdId = ''


def create():
    print()
    print('create:')

    global createdId
    data = [['1', '2'], ['apple', '0', 'pickle']]
    createdId = sheets.create(data)
    print('created ', createdId)


def getValues():
    print()
    print('getValues:')

    data = sheets.getValues(createdId, "A:C")
    print('fetched data', data)


def get():
    print()
    print('get:')

    data = sheets.get(createdId, "A:A")
    print('fetched data id', data['spreadsheetId'])
    print('fetched data name', data['properties']['title'])


def batchUpdate():
    print()
    print('batchUpdate:')
    newData = [['newA'], ['newB'], ['newC']]
    sheets.batchUpdate(createdId, "A:A", newData)
    data = sheets.getValues(createdId, "A:C")
    print('new data', data)


print('exercising sheets')
create()
getValues()
get()
batchUpdate()
