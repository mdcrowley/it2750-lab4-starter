# IT 2750 - Scripting Fundamentals for Cybersecurity
## Lab 4 - Manipulating Data with Lists and Dictionaries

### 🗒  Description
This repository contains the Python script for Lab 4 of the course IT 2750 - Scripting Fundamentals for Cybersecurity. There are two problems in this lab.

This lab encompasses two problems, each focusing on different aspects of data manipulation and extraction using Python. In the first problem, students are challenged to create a script for cracking ZIP files. This task involves developing a program that iterates through a predefined list of passwords to unlock an encrypted ZIP file, testing each password and indicating its success or failure. The second problem shifts focus to extracting data from CSV files. Students are required to construct a script that reads and parses a CSV file into a list of dictionaries, each representing a row with columns for name, phone, and email. The core task is to enable users to search for records using email addresses, displaying the corresponding name for each search, and allowing repeated searches until the user decides to stop. This lab aims to enhance students' practical skills in handling common data structures in Python, vital for cybersecurity applications.

#### Problem 1 - Cracking ZIP Files
Problem 1 focuses on creating a Python program that acts as a ZIP password cracker. In this lab, students are required to develop a script capable of attempting multiple password combinations to unlock a ZIP file. The ZIP file contains encrypted data, and the objective is to find the correct password from a predefined list of passwords. The lab begins by defining a list of passwords that the program will use for cracking. It then prompts the user to specify the ZIP file they want to unlock. The script proceeds to iterate through the list of passwords, attempting to extract the ZIP file's contents using each password. For each attempt, it prints whether the password attempt was successful or failed.

#### Problem 2 - Extracting Data from CSV Files
Problem 2 involves working with CSV data and creating a Python program to extract information from a CSV file. In this lab, students are tasked with building a script that interacts with a CSV file containing records with three columns: name, phone, and email. The program first prompts the user for the filename of the CSV data they want to analyze. It then uses the provided function, `csv_sample_data_as_list`, to read and parse the CSV file into a list of dictionaries, where each dictionary represents a row of data with keys for name, phone, and email. The main part of the lab involves allowing users to search for people using their email addresses. The program repeatedly asks the user for an email address to look up, and it displays the corresponding name from the CSV data. Users can continue searching until they enter "STOP" to exit the application.

### 📝  Requirements
This lab requires you to write code that adheres to the following requirements:

#### Problem 1
In Problem 1, you will edit the script template to perform the following tasks:

- Part A: Creates a list variable called `passwords` containing a list of common passwords.
- Part B: Asks the user for the filename of a zip file they want to crack (e.g., "lab4_data_problem1.zip").
- Part C: Iterates through the `passwords` list and attempts to open the zip file using each password. It prints "Password XXXXXX: Success!" if the password is correct and "Password XXXXXX: Failed" if the password is incorrect, where XXXXXX is the password attempted.

#### Problem 2
In Problem 2, you will edit the script template to perform the following tasks:

- Part A: Asks the user for the filename of a CSV file they want to analyze (e.g., "lab4_data_problem2.csv").
- Part B: Uses the `csv_sample_data_as_list` function to read and extract data from the CSV file, storing it in a list of lists.
- Part C: Converts the list of lists to a list of dictionaries, where each dictionary represents a row of data with keys for name, phone, and email.
- Part D: Allows the user to search for people using email addresses. The user can keep searching until they enter "STOP." The script iterates over the list of dictionaries to find a match and prints the name if found, or "Not found" if not.

#### Additional Requirements
In order to receive credit for this lab, you must replace `YOUR_NAME_HERE` with your name and `YOUR_EMAIL_HERE` with your Tri-C email address in the code file headers for all script files in the template. Students who do not perform this action will receive a zero score.

### 🚀  Usage
To run the script, execute the script file with Python. Each part of the lab problem is commented, and you should replace the placeholder text with your own information. From the code directory of this lab, you can run the various problems using the following commands:

- Problem 1: `python lab4_problem1.py`
- Problem 2: `python lab4_problem2.py`

### 🎯  Testing
The problems in this lab are tested using code that can be found in the corresponding `tests_*.py` file for each problem. You can use these tests to check if your code runs properly and to specifications. You can run these tests on your local machine by setting your working directory to the problem folder and running `pytest` with the `tests_*.py` file for the problem. From the code directory of this lab, you can run tests using the following commands:

- Problem 1: `pytest tests_lab4_problem1.py`
- Problem 2: `pytest tests_lab4_problem2.py`

### 🏆  Grading
This lab is worth 40 points in total using the following breakdown by problem:

- Problem 1 is worth 20 points
- Problem 2 is worth 20 points

You are awarded these points if all assertions in the test file pass successfully for a problem. There is no partial credit for lab problems.

### 💻  Academic Integrity and Copyright
This lab was created by the course professor (Matthew Crowley) and he asserts copyright over all material. You are not permitted to share the labs, tests, or solutions with anyone without express written consent. Breaches of this assertion may result in both academic and legal sanctions.