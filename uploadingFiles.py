import os
import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token =  access_token
#
    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        for root, dirs, files in os.walk(file_from):

            for filename in files:
                print(filename)
                local_path = os.path.join(root, filename)
                print(local_path)

                relative_path = os.path.relpath(local_path, file_from)
                print(relative_path)
                dropbox_path = os.path.join(file_to, relative_path)
                print(dropbox_path)
                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=dropbox.files.WriteMode.overwrite)

def main():
    access_token = 'C5Wb_n9d8cgAAAAAAAAAAW5HHXOIvbZIzk5Gv6k8peL25xRGWuUuT-9tQYA_iHcw'
    transferData = TransferData(access_token)

    file_from = input("Enter the folder path to transfer : ")
    print(" ")
    file_to = input("Enter the full path to upload to dropbox: ") 

    transferData.upload_file(file_from,file_to)
    print("Your file has been moved successfully.")

main()