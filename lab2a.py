# !/usr/bin/env python3
# Author Id: Rvanniyasingam
# A function that uses command line arguments. This function will print two variables used, the script and then the script AND variables.

import sys

def print_script_and_variables():
    # Get the script name
    script_name = sys.argv[0]

    # Print the script name
    print("Script name:", script_name)

    # Check if there are additional arguments
    if len(sys.argv) == 3:
        # Concatenate the script name with the provided arguments
        script_and_variables = script_name + " " + ' '.join(sys.argv[1:])
        # Print the script name and variables
        print("Script and variables used:", script_and_variables)
    else:
        print("Please provide only three arguments including script name.")

# Add NEW function
def helloWorld():
        print(‘Hello World’)


if __name__ == '__main__':
    print_script_and_variables()

    helloWorld()
