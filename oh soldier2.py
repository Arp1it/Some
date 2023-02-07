import os

def army(folder, file, format):
    os.chdir(folder)

    filelist = os.listdir(folder)

    with open(file) as filename:
        filenames = filename.read().split("\n")

    i = 1
    for files in filelist:
        if files not in filenames:
            os.rename(files, files.capitalize())

            if os.path.splitext(files)[1] == format:
                os.rename(files, f"{i}{format}")
                i += 1

folder_name = input("enter folder name: ")
file_name = input("enter file name: ")
format_name = input("enter format or extension of a file name whiuch was you change as a number: ")

army(folder_name, file_name, format_name)