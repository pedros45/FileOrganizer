import os
import platform
import time
import shutil


# get the home directory path of the user
directory = os.path.expanduser("~")

# what OS is the user using?
currentOs = platform.system()

# adjust the path to OneDrive folder appropriately depending on user OS
if currentOs == "Windows":
    directory = directory + "\\OneDrive"
elif currentOs == "Darwin":
    directory = directory + "/OneDrive/Pictures"
else:
    print("Currently doesn't support Linux distributions...")

print("Processing files. Please wait....")

onlyFiles = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

# Create Directories in OneDrive Folder for each month and then moves the file into the appropriate folder
for file in onlyFiles:

    fileData = ""

    # Turn timestamp into MetaData String depending on OS
    if currentOs == "Windows":
        fileData = time.ctime(os.path.getctime(os.path.join(directory, file))).split(" ")
    elif currentOs == "Darwin":
        fileData = time.ctime(os.stat(os.path.join(directory, file)).st_birthtime).split(" ")

    # Path for possible newDir
    newDir = os.path.join(directory, fileData[1] + fileData[len(fileData)-1])

    # Path for the current file being processed
    currFile = os.path.join(directory, file)

    # If the proper directory does not exist, make it
    if not os.path.exists(newDir):
        os.mkdir(newDir)

    # Move the file into its appropriate directory
    shutil.move(currFile, newDir)


print("Files processed. Check your One Drive folder!")