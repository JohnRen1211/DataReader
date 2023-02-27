# # Creating a program that will read students data
# #importing all files
# import pandas as pd
# import numpy as np
# import time
# studentDetails = pd.read_csv("D:\\Downloads\\Py_reader\\DataReader\\studentDetails.csv")  # loading dataset

# def startFeature():
#     print("Select the student level: For Graduate type G for undergraduate type U For both type BO")
#     student_level = input()  # input of student level
#     if student_level == 'G' or student_level == 'B':
#         print("Master: M or Doctrate: D or Both ")
#         inp = input()
#         print("Enter stdID")
#         inp = int(input())
#         if inp not in studentDetails['stdID'].values:  # for invalid input id
#             print("Enter valid studentid")
#             time.sleep(5)  # wait for few seconds
#             return  # exit the function if input is invalid
#         # proceed with the rest of the function if input is valid

# def menuFeature():  # menuscript as details provided
#     print("Student Transcript Generation System")
#     print("===========================================================")
#     print("1. Student Details")
#     print("2. Statistics")
#     print("3. Transcript based on major courses")
#     print("4. Transcript based on minor courses")
#     print("5. Full Transcript")
#     print("6. Previous Transcript Request")
#     print("7. Select another student")
#     print("8. Terminate the system")
#     print("===========================================================")
#     print("Enter your feature")
#     i = int(input())  # feature input
#     if i == 1:  # if option 1 is selected call details feature
#         inp = int(input("Enter student ID: "))
#         detailsFeature(inp)


# def detailsFeature(inp):  # here inp is input student id
#     studentDetails.set_index("stdID", inplace=True)  # set dataset index as stdId
#     student_data = studentDetails.loc[inp]
#     print("Name:", student_data['Name'])
#     print("stdID:", inp)
#     print("Level(s):", student_data['Level'])
#     print("Number of terms:", student_data['Terms'])
#     print("College(s):", student_data['College'])
#     print("Departments:", student_data['Department'])

# startFeature()
# # Need more fucntions

import pandas as pd
import numpy as np
import time

studentDetails = pd.read_csv("D:\\Downloads\\Py_reader\\DataReader\\studentDetails.csv")  # loading dataset


def startFeature():
    print("Select the student level: For Graduate type G for undergraduate type U For both type BO")
    student_level = input()  # input of student level
    if student_level == 'G' or student_level == 'B':
        print("Master: M or Doctrate: D or Both ")
        inp = input()
        inp = int(input("Enter student ID: "))
        if inp not in studentDetails.stdID:  # for invalid input id
            print("Enter valid studentid")
            time.sleep(3)  # wait for few seconds
            menuFeature()


def menuFeature():  # menuscript as details provided
    print("Student Transcript Generation System")
    print("===========================================================")
    print("1. Student Details")
    print("2. Statistics")
    print("3. Transcript based on major courses")
    print("4. Transcript based on minor courses")
    print("5. Full Transcript")
    print("6. Previous Transcript Request")
    print("7. Select another student")
    print("8. Terminate the system")
    print("===========================================================")
    print("Enter your feature")
    i = int(input())  # feature input
    if i == 1:  # if option 1 is selected call details feature
        inp = int(input("Enter student ID: "))
        detailsFeature(inp)


def detailsFeature(inp):  # here inp is input student id
    studentDetails.set_index("stdID", inplace=True)  # set dataset index as stdId
    print("Name:", studentDetails.get_value(inp, 'Name'))
    print("stdID:", inp)
    print("Level(s):", studentDetails.get_value(inp, 'Level'))
    print("Number of terms:", studentDetails.get_value(inp, 'Terms'))
    print("College(s):", studentDetails.get_value(inp, 'College'))
    print("Departments:", studentDetails.get_value(inp, 'Department'))


startFeature()