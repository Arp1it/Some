import os

def soler(folder_name, file_name, format_name):
    os.chdir(folder_name)
    
    if file_name == "this.txt" or file_name == "that.txt" or file_name == "normal.txt":
        print("no changes")

    # elif os.path.join(folder_name, file_name):

    else:
        a = os.path.isfile(folder_name + file_name)
        if a == False:
            print("no such file found")
        if  a == True:
            os.rename(file_name, file_name.capitalize())

    try:
        i = 1
        file_names = os.listdir(folder_name)
        for file_name in file_names:
            if os.path.splitext(file_name)[1] == format_name:
                os.rename(file_name, f"{i}{format_name}")
                i += 1
    except Exception as e:
        print(e)
        


folder = input("enter folder name: ")
file = input("enter file name: ")
format = input("enter format name of any  file which was adjust like jpg, wav etc: ")

soler(folder, file, format)