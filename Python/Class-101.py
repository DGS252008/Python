import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = '70hluWGRoF0AAAAAAAAAAa2R5LIQ0qsGoMk85vp4MkHX8J53oL9Q3vh8h1TvZwb8'
    transferData = TransferData(access_token)

    file_from = 'textedit.rtf'
    file_to = '/test.rtf'  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)
    print('File upload succesful.')

main()
