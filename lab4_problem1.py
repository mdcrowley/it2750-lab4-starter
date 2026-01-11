# ==================================================
# IT 2750 - Scripting Fundamentals for Cybersecurity
# Cuyahoga Community College
# Lab 4 – Problem 1
# ==================================================
# Student Name: YOUR_NAME_HERE
# Student Email: YOUR_EMAIL_HERE
# ==================================================

import string  # DO NOT EDIT THIS LINE
import zipfile  # DO NOT EDIT THIS LINE

# Open a zip file with a given password
def open_zip(file, password=''):  # DO NOT EDIT THIS METHOD
    # Create a new zip file object and open
    # the zip file
    zip = zipfile.ZipFile(file)

    # Attempt to extract all contents of the zip file
    # to the current directory. Return True if success
    # and False if failure
    try:
        if password == '':
            zip.extractall()
        else:
            zip.extractall(pwd=bytes(password, 'utf-8'))
        return True
    except Exception as e:
        return False

# PART A
# ======
# Create a new list variable called passwords containing the following passwords. 
# All of these # items should be treated as string literals. The items in the 
# list must be in the order they appear here (and do not add or remove any items):
#
#     123456
#     123456789
#     qwerty
#     password
#     1111111
#     12345678
#     abc123
#     1234567
#     password1
#     12345
#     1234567890
#     123123
#     000000
#     Iloveyou
#     1234
#     1q2w3e4r5t
#     Qwertyuiop
#     123
#     Monkey
#     Dragon

## YOUR CODE HERE ##

def main():  # DO NOT EDIT THIS LINE

    print("Welcome to the ZIP Password Cracker!")

    # PART B
    # ======
    # Create a variable and set its value to the response from an input call asking
    # for a filename of a zip file ("What file would you like to crack?"). To test your
    # code, you should enter the name of the zip file in the repository, which is
    # lab4_data_problem1.zip

    ## YOUR CODE HERE ##
    
    # PART C
    # ======
    # Create a loop that iterates through each item in the list in order. Pass the zip 
    # file and password into the open_zip() function. The zip file will open for a 
    # correct password.
    #
    # If the zip file was opened with the password, print the following output, replacing
    # XXXXXX with the password attempted:
    #
    #     Password XXXXXX: Success!
    #
    # If the zip file was unable to be opened with the password, print the following 
    # output, replacing XXXXXX with the password attempted:
    #
    #     Password XXXXXX: Failed

    ## YOUR CODE HERE ##

    return  # DO NOT EDIT THIS LINE

if __name__ == "__main__":  # DO NOT EDIT THIS LINE
    main()                  # DO NOT EDIT THIS LINE