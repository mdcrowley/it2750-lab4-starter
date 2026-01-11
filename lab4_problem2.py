# ==================================================
# IT 2750 - Scripting Fundamentals for Cybersecurity
# Cuyahoga Community College
# Lab 4 – Problem 2
# ==================================================
# Student Name: YOUR_NAME_HERE
# Student Email: YOUR_EMAIL_HERE
# ==================================================

import csv  # DO NOT EDIT THIS LINE

def csv_sample_data_as_list(file):
    with open(file, "r") as infile:
        reader = csv.reader(infile)
        next(reader, None) # Skip headers
        output = []
        for row in reader:
            output_column = []
            for column in row:
                output_column.append(column)
            output.append(output_column)
        return output

def main():  # DO NOT EDIT THIS LINE

    print("Welcome to the CSV Data Extractor!")

    # PART A
    # ======
    # Create a variable and set its value to the response from an input call asking
    # for a filename of a csv file to open ("What data would you like to analyze?").
    # To test your code, you should enter the name of the csv file in the repository,
    # which is lab4_data_problem2.csv

    ## YOUR CODE HERE ##

    # PART B
    # ======
    # The CSV file has three columns: name, phone, and email. Pass the filename to
    # the csv_sample_data_as_list function. It will return a list of lists with each
    # row of data, with each row as a list ordered as name, phone, and email.
    # Save the list to a new variable

    ## YOUR CODE HERE ##

    # PART C
    # ======
    # Convert this list of lists to a list of dictionaries and save in a new variable.
    # Each dictionary should have the following keys: name, phone, email

    ## YOUR CODE HERE ##
    
    # PART D
    # ======
    # We will let the user search for people using email addresses. They should be allowed
    # to keep searching until they enter STOP. Ask the user "What email would you like 
    # to look up? (STOP to exit)" and save the response into a variable. If the user enters
    # stop, exit the application. If the user enters in anything besides STOP, iterate over
    # the list of dictionaries to find the dictionary that matches the email. If found,
    # print the value for the name key (and nothing else, only the name), otherwise 
    # print "Not found"
    #
    # Hint: You can ask a user multiple times by putting the search logic into a loop and
    # checking the input, exiting the loop if the user enters STOP
    
    ## YOUR CODE HERE ##

    return  # DO NOT EDIT THIS LINE

if __name__ == "__main__":  # DO NOT EDIT THIS LINE
    main()                  # DO NOT EDIT THIS LINE