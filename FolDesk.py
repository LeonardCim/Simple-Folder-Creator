import os

quest = input("Choose the name of the folder: ")


def create_folder():
    '''function to create folder'''
    
    path = r"C:\Users\Utente\Desktop"
    uni = os.path.join(path, quest)
    
    try:
        os.mkdir(uni)
        print("folder '{}' created ".format(uni))
        print("Well done! Enjoy your new folder!")
    
    except FileExistsError:
        print("The folder <({})> already exist, try with another name.".format(quest))
        
        
create_folder()
