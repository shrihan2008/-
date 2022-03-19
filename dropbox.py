import dropbox
class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token


    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)
        f=open(file_from,"rb")
        dbx.files_upload(f.read(),file_to)

def main():
    access_token='sl.BEF5J3uKz-CFxCmjLm6Gyy_tnQTB5pHsuYPz-CLxTOHgTAtDafoK4JlSPNKdJetVK-E7fAvOHWNMc_aXt6HllESZeZLrsHk1wjlAbHwSpncR8jVZ5RXEnyHi8x6HMgNhyDhdd7lU9fOn'
    transferData=TransferData(access_token)
    file_from=input("Enter a path ")
    file_to=input("Enter complete path to upload to dropbox ")
    transferData.upload_file(file_from,file_to)
    print("Transfer complete ")

main()