import os

quest = input("Choose the name of the folder: ")


def create_folder():
    '''function to create folder'''
    global quest
    
    path = os.getcwd()
    uni = os.path.join(path, quest)
    
    if not os.path.exists(quest):
        os.mkdir(uni)
        
        print("folder '{}' created ".format(uni))
        print("Well done! Enjoy your new folder!")
    
    else:
        
        print("The folder <({})> already exist, try with another name.".format(quest))

       
def create_file():
    '''fucntion to create file'''
    global quest

    with open(os.path.join(quest, "Provafile.txt"), "w+") as newfile:
        newfile.write("Hi guys, i hope you like it.")
        newfile.close()


def main():
    create_folder()
    create_file()
    

if __name__=="__main__":
    main()
        

   

    

