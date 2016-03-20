#!usr/bin/python3

import os
import subprocess
import time


# request the filepath for the images

def requestFilepath():
    print("Please input the file path for your images:")
    fpath = input()

    while not os.path.exists(fpath):

        print("The file path you have entered does not exist.")
        print("Do you want to create this folder or input again?")
        print("[Y/N]")

        while True:
            decision = input().upper()

            if decision == 'Y':
                os.mkdir(fpath)
                print("The path has been created at ", fpath)
                break

            elif decision == 'N':
                print("Please input the file path for your images:")
                fpath = input()
                break

            else:
                print("Invalid input, try again")

    return fpath


def scanFolder(pathToFolder):
    scriptPath = os.path.join(pathToFolder, 'ImgClassif.py')
    while True:
        fileList = os.listdir(pathToFolder)
        time.sleep(0.2)
        newFileList = os.listdir(pathToFolder)

        if not fileList == newFileList:
            newImg = set(newFileList) - set(fileList)
            print("new instance has been launched")
            subprocess.Popen(['python', scriptPath, os.path.join(pathToFolder, newImg[0])])
            fileList = newFileList

        else:
            continue



path = requestFilepath()
os.chdir(path)
scanFolder(path)
