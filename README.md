# FileOrganizer

A Python script turned command line tool that automates file organization based on the creation date of the files. Using the terminal, the user is able to provide a list of paths to the directories whose files or subdirectories will be organized. 

## Getting Started

In order to get started, clone the project from my GitHub into any location you'd like on your computer.
### Prerequisites

Make sure to have at least Python 3.7 installed. 

### Example

Let's say you wanted to organize your OneDrive directory and some other folder.
Change into the cloned repository on your computer.
Once there, you can call the script. The arguments that get passed with the script
are paths relative to your HOME DIRECTORY e.g ``` /User/(your username)/``` for MacOs or ``` C:\Users\(your username)\ ``` for Windows.
Call the FileOrganizer.py file along with a list of the relative paths of the directories, delimited by a space, that you would like organized.

```
python FileOrganizer.py OneDrive path/to/another/folder
```

Once run you should get a confirmation message stating that the folders were organized successfully. Checking the directories you should see new folders within it that now hold the pictures.
It should be noted that the script also checks the directory for subdirectories and organizes them as well following the same criteria.
## Authors

* **Pedro Suazo** -- Github: [pedros45](https://github.com/pedros45)

## Acknowledgments

* Thank you to my girlfriend for giving me the idea for this project and for inspiring me to make it as cool and as useful as possible! I hope this ends up being useful not only to her, but to others as well!