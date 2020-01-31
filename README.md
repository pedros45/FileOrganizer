# FileOrganizer (Not Complete)

A Python script turned command line tool that automates file organization based on the creation date of the files. Using the terminal, the user is able to change into the directory of their choice and then provide a list of directories whose files will be organized. 

## Getting Started

In order to get started, clone the project from my GitHub into any location you'd like on your computer.
### Prerequisites

Make sure to have at least Python 3.7 installed. Nothing beyond the standard libraries are used so as long as you have the correct version of Python the program should run correctly.

### Installing

After doing so, go to the cloned repository from your terminal and run the Initializer.py file as such
 ```
python Initializer.py
``` 
or 
```
python3 Initializer.py
```
After doing so, the current working directory should be added as one of your PATH environment variables. After doing so the FileOrganizer.py file will be executable from any directory you wish to run from. 

### Example

Let's say you wanted to organize your OneDrive directory.
Change into that directory: 
```
cd OneDrive
```

Once you are in that directory, call the FileOrganizer.py file along with a list of sub-directories, delimited by a space, that exist inside the OneDrive directory that need to be organized as such:

```
python FileOrganizer.py Pictures OtherPictures 
```

Once run you should get a confirmation message stating that the folders were organized successfully. Checking the directories you should see new folders within it that now hold the pictures.
## Authors

* **Pedro Suazo** -- Github: [pedros45](https://github.com/pedros45)

## Acknowledgments

* Thank you to my girlfriend for giving me the idea for this project and for inspiring me to make it as cool and as useful as possible! I hope this ends up being useful not only to her, but to others who may be interested in using it!