import os
import platform
import time
import shutil
import argparse


def moveFiles(currentDirectory, currentOs, onlyFiles):

    # Create Directories in current folder for each month and then moves the file into the appropriate folder
    for file in onlyFiles:
        fileData = ""

        # Turn timestamp into MetaData String depending on OS
        if currentOs == "Windows":
            fileData = time.ctime(os.path.getctime(os.path.join(currentDirectory, file))).split(" ")
        elif currentOs == "Darwin":
            fileData = time.ctime(os.stat(os.path.join(currentDirectory, file)).st_birthtime).split(" ")

        # Path for possible newDir
        newDir = os.path.join(currentDirectory, fileData[1] + fileData[len(fileData) - 1])

        # Path for the current file being processed
        currFile = os.path.join(currentDirectory, file)

        # If the proper directory does not exist, make it
        if not os.path.exists(newDir):
            os.mkdir(newDir)

        # Move the file into its appropriate directory
        shutil.move(currFile, newDir)


def organize(orgDir):
    # get the path to the user home directory
    start = os.path.expanduser("~")

    # what OS is the user using?
    currentOs = platform.system()

    for folder in orgDir:
        currentDirectory = os.path.join(start, folder)

        onlyDirectories = [d for d in os.listdir(currentDirectory) if os.path.isdir(os.path.join(currentDirectory, d))]

        if len(onlyDirectories) != 0:
            for dir in onlyDirectories:
                subDir = os.path.join(currentDirectory, dir)
                subDirFiles = [f for f in os.listdir(subDir) if os.path.isfile(os.path.join(subDir, f))]
                moveFiles(subDir, currentOs, subDirFiles)

        # Organize files in the base directory
        onlyFiles = [f for f in os.listdir(currentDirectory) if os.path.isfile(os.path.join(currentDirectory, f))]
        moveFiles(currentDirectory, currentOs, onlyFiles)

    print("The following directories " + str(orgDir) + " have been organized!")


# Create ArgumentParser object to hold all the information to parse from the command line
parser = argparse.ArgumentParser(description="Organize the files in a folder")

# Add an argument to the command line tool
parser.add_argument("List of Directories", metavar="directories", nargs="+", type=str, help="A list of the directories you would "
                                                                                 "like to organize")

# Parse the arguments passed to the command line
args = parser.parse_args()

orgDir = vars(args)["List of Directories"]

# Call the organize function that will do the actual organizing
organize(orgDir)

