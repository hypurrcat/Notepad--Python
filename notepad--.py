# Program Version Number
PROG_VERSION = 1.0

def main():    
    # Print opening title
    print("======================================================")
    print("eeeee eeeee eeeee eeee eeeee eeeee eeeee")
    print("8   8 8  88   8   8    8   8 8   8 8   8")
    print("8e  8 8   8   8e  8eee 8eee8 8eee8 8e  8   #### #### ")
    print("88  8 8   8   88  88   88    88  8 88  8")
    print("88  8 8eee8   88  88ee 88    88  8 88ee8")
    print("======================================================")
    print("                                                 v" + str(PROG_VERSION))
    print()
    print("Please enter the word START to start having extreme amounts of fun.")
    print("You can't type start. This is case sensitive. This is by design. Feature not bug.")
    print()

    # Start prompting to start program
    start_Program = input("Do you want to start?: ")
    # Check initially whether the input is EXACTLY "START" or not. If not, loop until it is.
    if start_Program == "START":
        typingProg()
    else:
        while start_Program != "START":
            print("THAT IS NOT 'START'!!!! TYPE IT RIGHT OR YOU WONT EVER GET TO SEE YOUR FAMILY AGAIN.")
            start_Program = input("Do you want to start?: ")
        typingProg()

def typingProg():
    # Empty list to store text entered for each line
    file = []

    # Print break case
    print()
    print()
    print()
    print("You can now start typing. To finish your file, please type this exact phrase (excluding quotation marks):")
    print('"Notepad--, please exit this program. I am done typing my file now."')
    print()
    print()

    # Prime loop
    text_Data = input()

    # Start typing
    while text_Data != "Notepad--, please exit this program. I am done typing my file now.":
        file.append(text_Data)
        text_Data = input()

    # Enter file name
    print()
    print()
    file_name = input("Enter file name to output to (ENDING IN YOUR FILE EXTENSION): ")

    # Output to file
    with open(file_name, "a+") as file_writing:
        iter = 0
        total_lines = len(file)

        line_to_write = file[iter] + "\n"
        file_writing.write(line_to_write)

        while iter < total_lines - 1:
            iter += 1
            line_to_write = file[iter] + "\n"
            file_writing.write(line_to_write)

# Call main
main()
