#Creating a program that will read students data
import datetime
import time
import pandas as pd
import numpy as np

studentDetails = pd.read_csv("D:\\Downloads\\Py_reader\\DataReader\\studentDetails.csv")  # loading dataset

# Function to select student level and degree
def startFeature():
    global level, degree
    print("Select student level:")
    print("U: Undergraduate")
    print("G: Graduate")
    print("B: Both")
    level = input()
    if level == "G" or level == "B":
        print("Select degree:")
        print("M: Master")
        print("D: Doctorate")
        print("B0: Both")
        degree = input()
    time.sleep(2)
    menuFeature()

# Function to display menu and get user input
def menuFeature():
    print("Student Transcript Generation System")
    print("===================================")
    print("1. Student details")
    print("2. Statistics")
    print("3. Transcript based on major courses")
    print("4. Transcript based on minor courses")
    print("5. Full transcript")
    print("6. Previous transcript requests")
    print("7. Select another student")
    print("8. Terminate the system")
    print("===================================")
    choice = int(input("Enter your feature: "))
    if choice == 1:
        detailsFeature()
    elif choice == 2:
        statisticsFeature()
    elif choice == 3:
        majorTranscriptFeature()
    elif choice == 4:
        minorTranscriptFeature()
    elif choice == 5:
        fullTranscriptFeature()
    elif choice == 6:
        previousRequestsFeature()
    elif choice == 7:
        startFeature()
    elif choice == 8:
        print("Exiting system...")
    else:
        print("Invalid choice!")
        menuFeature()

# Function to display student details
def detailsFeature():
    global level, degree
    stdID = input("Enter student ID: ")  # prompt user to enter their student ID
    print("Name:")
    print("stdID:")
    print("Level(s): " + level)
    if level == "U":
        print("Number of terms:")
    elif degree == "M":
        print("Number of semesters:")
    elif degree == "D":
        print("Number of quarters:")
    else:
        print("Number of terms/semesters/quarters:")
    print("College(s):")
    print("Department(s):")
    # write student details to file
    with open("std" + stdID + "details.txt", "w") as f:
        f.write("Name:\n")
        f.write("stdID:\n")
        f.write("Level(s): " + level + "\n")
        if level == "U":
            f.write("Number of terms:\n")
        elif degree == "M":
            f.write("Number of semesters:\n")
        elif degree == "D":
            f.write("Number of quarters:\n")
        else:
            f.write("Number of terms/semesters/quarters:\n")
        f.write("College(s):\n")
        f.write("Department(s):\n")
    time.sleep(2)
    # clear screen and return to menu
    print("\033c", end="")
    menuFeature()
# Function to display statistics
def statisticsFeature():
    std_id = input("Enter Student ID: ")
    std_level = input("Enter Student Level (U for Undergraduate, M for Graduate): ")
    print("=" * 40)
    if std_level.upper() == "U":
        print("*******Undergraduate Level*******")
    elif std_level.upper() == "M":
        print("******Graduate(M) Level******")
    else:
        print("Invalid Student Level!")
        return

    print("=" * 40)

    # Here you can implement the necessary logic to retrieve the student's records
    # and calculate the statistics based on the selected options

    # Example statistics
    overall_average = 85
    term_averages = [80, 85, 90]
    max_grades = [("CS101", 95, "Term 2"), ("MA101", 92, "Term 3")]
    min_grades = [("CS201", 75, "Term 1"), ("MA201", 78, "Term 2")]
    repeated_courses = ["CS101"]

    # Print statistics
    print("Overall average (major and minor) for all terms: ", overall_average)
    print("Average (major and minor) of each term:")
    for i, term_avg in enumerate(term_averages):
        print("Term {}: {}".format(i+1, term_avg))
    print("Maximum grade(s) and in which term(s):")
    for course, grade, term in max_grades:
        print("{}: {} in {}".format(course, grade, term))
    print("Minimum grade(s) and in which term(s):")
    for course, grade, term in min_grades:
        print("{}: {} in {}".format(course, grade, term))
    print("Repeated course(s): ", ", ".join(repeated_courses))

    # Store statistics in file
    filename = "std{}statistics.txt".format(std_id)
    with open(filename, "w") as f:
        f.write("Overall average (major and minor) for all terms: {}\n".format(overall_average))
        f.write("Average (major and minor) of each term:\n")
        for i, term_avg in enumerate(term_averages):
            f.write("Term {}: {}\n".format(i+1, term_avg))
        f.write("Maximum grade(s) and in which term(s):\n")
        for course, grade, term in max_grades:
            f.write("{}: {} in {}\n".format(course, grade, term))
        f.write("Minimum grade(s) and in which term(s):\n")
        for course, grade, term in min_grades:
            f.write("{}: {} in {}\n".format(course, grade, term))
        f.write("Repeated course(s): {}\n".format(", ".join(repeated_courses)))

    # Clear screen and wait before returning to menu
    time.sleep(3)
    print("\n" * 100)
# # Function to display major transcript
# def majorTranscriptFeature():
#     # get student information from file or input
#     student_info = getStudentInfo()

#     # get list of major courses and grades from file
#     major_courses = getMajorCourses(student_info['major'])
#     grades = getGrades(student_info['ID'], major_courses)

#     # calculate major average for each term and overall major average
#     major_averages = []
#     overall_major_average = 0
#     for term in range(1, student_info['terms'] + 1):
#         term_grades = grades[term - 1]
#         major_grades = [grade for course, grade in term_grades.items() if course in major_courses]
#         major_average = sum(major_grades) / len(major_grades)
#         major_averages.append(major_average)
#         overall_major_average += major_average
#         print(f"{'*'*75}\n{' '*30}TERM {term}\n{'*'*75}")
#         print("course ID\tcourse name\tcredit hours\tgrade")
#         for course, grade in term_grades.items():
#             if course in major_courses:
#                 print(f"{course}\t{'course name'}\t{'credit hours'}\t{grade}")
#         print(f"Major Average = {major_average:.2f}\tOverall Average = {overall_major_average/term:.2f}")
    
#     # save transcript to file
#     filename = f"std{student_info['ID']}majorTranscript.txt"
#     with open(filename, "w") as f:
#         f.write(f"Name: {student_info['name']}\tstdID: {student_info['ID']}\n")
#         f.write(f"College: {student_info['college']}\tDepartment: {student_info['department']}\n")
#         f.write(f"Major: {student_info['major']}\tMinor: {student_info['minor']}\n")
#         f.write(f"Level: {student_info['level']}\tNumber of terms: {student_info['terms']}\n")
#         f.write("="*80 + "\n")
#         for term in range(1, student_info['terms'] + 1):
#             term_grades = grades[term - 1]
#             major_grades = {course: grade for course, grade in term_grades.items() if course in major_courses}
#             major_average = major_averages[term - 1]
#             f.write(f"{'*'*75}\n{' '*30}TERM {term}\n{'*'*75}\n")
#             f.write("course ID\tcourse name\tcredit hours\tgrade\n")
#             for course, grade in major_grades.items():
#                 f.write(f"{course}\t{'course name'}\t{'credit hours'}\t{grade}\n")
#             f.write(f"Major Average = {major_average:.2f}\tOverall Average = {overall_major_average/term:.2f}\n")
#         f.write("="*80 + "\n")
    
#     print("\nTranscript saved to file:", filename)
#     time.sleep(5)
    

# # Function to display minor transcript
# def minorTranscriptFeature():
#     # get student information from file or input
#     student_info = getStudentInfo()

#     # get list of minor courses and grades from file
#     minor_courses = getMinorCourses(student_info['minor'])
#     grades = getGrades(student_info['ID'], minor_courses)

#     # calculate minor average for each term and overall minor average
#     minor_averages = []
#     overall_minor_average = 0
#     for term in range(1, student_info['terms'] + 1):
#         term_grades = grades[term - 1]
#         minor_grades = [grade for course, grade in term_grades.items() if course in minor_courses]
#         minor_average = sum(minor_grades) / len(minor_grades)
#         minor_averages.append(minor_average)
#         overall_minor_average += minor_average
#         print(f"{'*'*75}\n{' '*30}TERM {term}\n{'*'*75}")
#         print("course ID\tcourse name\tcredit hours\tgrade")
#         for course, grade in term_grades.items():
#             if course in minor_courses:
#                 print(f"{course}\t{'course name'}\t{'credit hours'}\t{grade}")
#         print(f"Minor Average = {minor_average:.2f}\tOverall Average = {overall_minor_average/term:.2f}")
    
#     # save transcript to file
#     filename = f"std{student_info['ID']}minorTranscript.txt"
#     with open(filename, "w") as f:
#         f.write(f"Name: {student_info['name']}\tstdID: {student_info['ID']}\n")
#         f.write(f"College: {student_info['college']}\tDepartment: {student_info['department']}\n")
#         f.write(f"Major: {student_info['major']}\tMinor: {student_info['minor']}\n")
#         f.write(f"Level: {student_info['level']}\tNumber of terms: {student_info['terms']}\n")
#         f.write("="*80 + "\n")
#         for term in range(1, student_info['terms'] + 1):
#             term_grades = grades[term - 1]
#             minor_grades = {course: grade for course, grade in term_grades.items() if course in minor_courses}
#             minor_average = minor_averages[term - 1]
#             f.write(f"{'*'*75}\n{' '*30}TERM {term}\n{'*'*75}\n")
#             f.write("course ID\tcourse name\tcredit hours\tgrade\n")
#             for course, grade in minor_grades.items():
#                 f.write(f"{course}\t{'course name'}\t{'credit hours'}\t{grade}\n")
#             f.write(f"Minor Average = {minor_average:.2f}\tOverall Average = {overall_minor_average/term:.2f}\n")
#         f.write("="*80 + "\n")
    
#     print("\nTranscript saved to file:", filename)
#     time.sleep(5)
# # Function to display full transcript
def majorTranscriptFeature(students):
    major = input("Enter major name: ")
    for student in students:
        if student["major"] == major:
            print("Name:", student["name"])
            print("ID:", student["id"])
            print("Major:", student["major"])
            print("Courses:", student["majorCourses"])

def minorTranscriptFeature(students):
    minor = input("Enter minor name: ")
    for student in students:
        if student["minor"] == minor:
            print("Name:", student["name"])
            print("ID:", student["id"])
            print("Minor:", student["minor"])
            print("Courses:", student["minorCourses"])
def fullTranscriptFeature():
    clear_screen()
    print("Full Transcript Feature")
    print("----------------------")
    stdID = input("Please enter your student ID: ")

    try:
        # Load student's data
        student_data = load_student_data(stdID)
        college = student_data["college"]
        department = student_data["department"]
        major = student_data["major"]
        minor = student_data["minor"]
        level = student_data["level"]
        num_terms = student_data["num_terms"]
        courses = student_data["courses"]
    except:
        print("Invalid student ID.")
        time.sleep(2)
        return

    # Sort courses by term number
    sorted_courses = sorted(courses, key=lambda c: c["term"])

    # Create list of dictionaries with the average of each term
    terms_avg = []
    for t in range(1, num_terms+1):
        term_courses = [c for c in sorted_courses if c["term"] == t]
        term_avg = calculate_term_average(term_courses)
        terms_avg.append({"term": t, "average": term_avg})

    # Calculate major and minor averages
    major_avg = calculate_major_average(courses, major)
    minor_avg = calculate_minor_average(courses, minor)

    # Print transcript header
    print_transcript_header(stdID, college, department, major, minor, level, num_terms)

    # Print each term's courses and average
    for term in sorted_courses_by_term(sorted_courses):
        print_term_courses(term)
        print("Major Average = {:<40} Overall Average = {:.2f}\n".format("", term["average"]))

    # Print major and minor averages
    print_major_minor_averages(major_avg, minor_avg)

    # Save transcript to file
    file_name = "{}FullTranscript.txt".format(stdID)
    save_transcript_to_file(file_name, stdID, college, department, major, minor, level, num_terms, sorted_courses, terms_avg, major_avg, minor_avg)

    time.sleep(2)
    mainMenu()

def previousRequestsFeature(stdID):
    # Load previous requests from file
    with open(f'std{stdID}PreviousRequests.txt', 'r') as f:
        previous_requests = f.readlines()
    
    # Print header
    print('{:<20}{:<20}{:<20}'.format('Request', 'Date', 'Time'))
    print('='*60)
    
    # Print previous requests
    for request in previous_requests:
        request_data = request.strip().split(',')
        print('{:<20}{:<20}{:<20}'.format(request_data[0], request_data[1], request_data[2]))
    
    # Save current request to file
    with open(f'std{stdID}PreviousRequests.txt', 'a') as f:
        current_time = datetime.datetime.now().strftime('%d/%m/%Y %H:%M %p')
        request = f'{request_type},{current_time}\n'
        f.write(request)
    
    # Clear screen and redirect to menu
    clear_screen()
    sleep(2)
    show_menu(stdID)

def terminateFeature():
    # Print number of requests during session
    print(f'Total requests: {num_requests}')
    
    # Terminate program
    sys.exit()

# Start the program
startFeature()