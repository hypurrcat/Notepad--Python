# Notepad-- Python
A rudimentary "text editor" created entirely as a joke. Programmed in [Python](https://www.python.org/).


This project was created to act as a rudimentary text editor in the Python terminal/shell. Using base Python3, this program supports file writing, but does not currently support reading and editing already existing files. Supports the output of any text-based file extension. Does not support editing an already "entered"/committed line. 

## How to Run
The Python3 version of Notepad-- should run in any Python shell that runs Python3. If Python is installed on your system, opening a terminal window in the same directory as the Notepad-- file should allow you to run the program.

Once the terminal window has been opened in that directory, the following command will run Notepad--:
```
python3 notepad--.py
```
This program does not require any additional Python packages/dependencies.

## How to Use Notepad--
Upon running the program successfully, the user will be greeted with an ASCII title screen and instructions following the title. Typing "START" (case sensitive) will allow the user to start creating/writing their file in the program.

Now, any text the user types will be committed to the file until the user types the sentinel value (exit statement) to stop writing the file's text. To stop writing text to a file, the user must type "Notepad--, please exit this program. I am done typing my file now."

Once this sentence has been typed, the user will be prompted to enter the name of the file they want to save to, followed by the file's extension (i.e. .py, .c, .txt, .csv, etc.).

## Credits
[Python](https://www.python.org/) for programming language.
