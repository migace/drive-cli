from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

class GoogleDrive:
    SCOPES = 'https://www.googleapis.com/auth/drive.metadata.readonly'

    def __init__(self):
        store = file.Storage('token.json')
        creds = store.get()

        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets('credentials.json', GoogleDrive.SCOPES)
            creds = tools.run_flow(flow, store)

        self.service = build('drive', 'v3', http=creds.authorize(Http()))
        self.nextPageToken = ''

    def getFilesList(self, nextPageToken = '', pageSize=12):
        results = self.service.files().list(
            pageSize=pageSize,
            pageToken=nextPageToken,
            fields="nextPageToken, files(id, name, kind, mimeType, owners(displayName), parents, webContentLink)").execute()
        self.nextPageToken = results.get('nextPageToken', '')
        items = results.get('files', [])
        result = []

        for item in items:
            result.append(item['name'])

        return result

    def getNextPageToken(self):
        return self.nextPageToken

    def create(self, file):
        return self.service.files().create(media_body=file)
