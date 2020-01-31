import os
import platform
import time
import shutil
import argparse


def organize(orgDir):
    # get the current directory from which the user is running the script
    currentDirectory = os.getcwd()

    # what OS is the user using?
    currentOs = platform.system()

    for folder in orgDir:

        # adjust the path to OneDrive folder appropriately depending on user OS
        if currentOs == "Windows":
            currentDirectory = currentDirectory + "\\" + folder
        elif currentOs == "Darwin":
            currentDirectory = currentDirectory + "/" + folder
        else:
            print("Currently doesn't support Linux distributions...")

        print("Processing files. Please wait....")

        onlyFiles = [f for f in os.listdir(currentDirectory) if os.path.isfile(os.path.join(currentDirectory, f))]

        # Create Directories in OneDrive Folder for each month and then moves the file into the appropriate folder
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

    print("The following directories " + orgDir + " have been organized!")


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

