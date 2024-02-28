## File Organizer Python3 Script

This script helps to organize files in a specified directory by moving matched files to a target directory.
It was initially designed to handle organization of macOS screenshots by name pattern, as I for some reason didn't realize macOS already has this feature built in.
Still a fun mini-project and it can easily be adapted to other file types or file name patterns by implementing a new regular expression.

### Prerequisite
You will need to have Python 3 installed on your computer.

### Usage
To run the script, navigate to the directory where the script is located using the command line (Terminal on macOS and Linux, Command Prompt on Windows), then run it with Python, specifying target source and location directory, like so:

```
$ python3 organize_files.py /Source/Directory/... /Target/Directory/...
```
Replace "/Source/Directory/..." with the path to the directory containing the files you want to organize, and
"/Target/Directory/..." with the path where you want to move matched files.

**Note**: This command line will move all files that match the file name pattern.

### Customization
To change the type of files being organized, modify the regular expression in the validate_file_name function in the script.
