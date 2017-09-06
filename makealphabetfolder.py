import string
import os


def make_folders():
    alphabet = list(string.ascii_uppercase)

    for index, item in enumerate(alphabet):
        print index, item
        item += ' - '
        alphabet[index] = item


    #os.chdir('C:/Users/2dgam/Desktop/world flags/library')



    for folder in alphabet:
        os.mkdir(os.path.join("",str(folder)))



if __name__ == "__main__":
    # call your code here
    make_folders()
