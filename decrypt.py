from cryptography.fernet import Fernet
import os
def decrypt(filename):

    fernet = Fernet(key)
    with open(filename,'rb') as enc_file:
        encrypted = enc_file.read()

    decrypted = fernet.decrypt(encrypted)

    with open(filename,'wb') as dec_file:
        dec_file.write(decrypted)


def inside_folder(folder_path):

    for filename in os.listdir(folder_path):
        full_path = os.path.join(folder_path,filename)
        if(os.path.isdir(full_path)):
            inside_folder(full_path)
        else:
            print("Decrypting....", filename)
            decrypt(full_path)
            print("Done")

def main_decrypt(path):
    with open('filekey.key','rb') as key_file:
            global key 
            key = key_file.read()
    folder_path = path
    if(os.path.isfile(folder_path)):
        print("Decrypting...",folder_path)
        decrypt(folder_path)
        print("Done")
        exit(1)
    inside_folder(folder_path)


