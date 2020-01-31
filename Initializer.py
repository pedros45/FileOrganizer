"""
This file is used for the purpose of adding the script folder as a PATH Environment variable so that the FileOrganizer
script can be used from any directory the user wishes to organize. Initializer MUST be run first before the
FileOrganizer can be used properly.
"""

import os

# Adds current working directory (Wherever the user decides to download the program to) to the PATH
os.environ["PATH"] += os.pathsep + os.getcwd()

print("The program directory has been added to the PATH environment variables on your computer.")
