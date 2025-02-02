from os import system
from colorama import Fore
import time

# Clear the screen
clear = lambda: system("cls")
clear()
print ("""
 █████╗ ███╗   ███╗██╗  ██╗         █████╗ ███████╗
██╔══██╗████╗ ████║██║  ██║        ██╔══██╗██╔════╝
███████║██╔████╔██║███████║        ███████║█████╗  
██╔══██║██║╚██╔╝██║██╔══██║        ██╔══██║██╔══╝  
██║  ██║██║ ╚═╝ ██║██║  ██║███████╗██║  ██║███████╗
╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝
""")

system('title GPA Calculator for Gelişim University')

ques = '['+Fore.MAGENTA+'?'+Fore.WHITE+'] '
cc = '['+Fore.CYAN+'*'+Fore.WHITE+'] '
era = '['+Fore.YELLOW+'!'+Fore.WHITE+'] '

letter_grades = {'AA':4.0, 'BA':3.5, 'BB':3.0, 'CB':2.5, 'CC':2.0, 'DC':1.8, 'DD':1.5}
grade_range = {'AA': [90, 100], 'BA': [85, 89], 'BB': [75, 84], 'CB': [65, 74], 'CC': [60, 64], 'DC': [50, 59], 'DD': [45, 49],'FD':[40,44], 'FF': [0, 39]}

print(f'                                     Coded by {Fore.RED}https://www.instagram.com/amh_ae_{Fore.WHITE}')


print (f'\n{cc}1. To Calculate GPA with known letter grades (AA, BA, ... , etc).')
print (f'{cc}2. To Calculate GPA with known grades (Midterm, Final, ... , etc).')
print (f'{cc}3. To Calculate letter grade for a single course.')
print (f'{cc}4. To Calculate passing grade for a single course.')

user_choice = int(input('\nChoose the operation >> '))

def single_course():
    global total, grade
    tasks = ['Midterm', 'Final', 'Homework', 'Quiz', 'Lab']
    percentages = {}
    grades = {}
    total_grade = {}
    print ('\nInputs should be as follows 10, 20, 30, ... , etc.')
    print ('If you have less than 5 tasks, enter 0 for the task you do not have.\n') 


    for index, task in enumerate(tasks):
        percentage = int(input(f'{ques}Enter the percentage of {task}: '))
        percentages[task] = percentage/100
        
    # print (f'{cc}The percentages are: {percentages}')
    print ('')
    for index, task in enumerate(tasks):
        grade = float(input(f'{ques}Enter the grade of {task}: '))
        grades[task] = grade
    # print (f'{cc}The grades are: {grades}')
    print ('')
    for task in tasks:
        total_grade[task] = grades[task] * percentages[task]
    # print (f'{cc}The total grades are: {total_grade}')
    total = sum(total_grade.values())
    print (f'{cc}The total grade is: {total}')
    
    for grade, (min, max) in grade_range.items():
        if min <= total <= max:
            print (f'{cc}Your letter grade is: {grade}')
    if total_grade['Final'] < 40.0 or total < 40.0:
        print (f'{era}You failed the course!')
    else:
        print (f'{era}You passed the course!')
    return total
    # print (type(total_grade['Final']), type(total))

def passing_grade():
    tasks = ['Midterm', 'Homework', 'Quiz', 'Lab']
    percentages = {}
    grades = {}
    total_grade = {}
    print ('\nInputs should be as follows 10, 20, 30, ... , etc\n') 

    for index, task in enumerate(tasks):
        percentage = int(input(f'{ques}Enter the percentage of {task}: '))
        percentages[task] = percentage/100
    print ('')
    for index, task in enumerate(tasks):
        grade = float(input(f'{ques}Enter the grade of {task}: '))
        grades[task] = grade
    print ('')
    for task in tasks:
        total_grade[task] = grades[task] * percentages[task]
    total = sum(total_grade.values())
    passing = 40-total*2
    if passing < 40:
        print (f'{cc}You need to get at least 40 in the final to pass the course!')
    else:
        print (f'{cc}You need to get at least {passing} in the final to pass the course!')
    
    
def previos():
    global Wcredit, Tcredit
    print (f"\n{era}If you don't know how to get the A.K and T.K, you can find them in the transcript.\nGo to Obis >> Documents >> Transcript")
    while True:
        Wcredit = input(f'\n{ques} please enter the previous Ağırlıklı Kredi (A.K) : ')
        Tcredit = input(f'{ques} please enter the previous Toplam Kredi (T.K) : ')
        try:
            Wcredit=float(Wcredit)
            Tcredit=float(Tcredit)
        except Exception as e:
            print (f'{era} Please enter valid inputs!')
            continue
        break

def output():
    choice= input(f'\n{ques}Do you want to save the results in a txt file? (y/n): ')
    if choice.lower() == 'y':
        with open('GPA.txt', 'w') as f:
            f.write(result)
        print (f'{cc}Results saved in GPA.txt!')
    else:
        print (f'{cc}Results will not be saved!')

def gpa_calc():
    global Wcredit, Tcredit, result
    try:
        total_credit = Tcredit
        total_grade = Wcredit
    except Exception :
        total_credit = 0
        total_grade = 0
    
    new_cource = {}
    for i in range(n):
        course_name = input(f'\n{ques}Enter the course name: (if you want to skip this step keep it blank) ')
        if not course_name:
            course_name = f'Course {i+1}'
        credit = int(input(f'{ques}Enter the credit of the course: '))
        grade = input(f'{ques}Enter the letter grade of the course: ').upper()
        total_credit += credit
        total_grade += letter_grades[grade] * credit
        new_cource[course_name] = [grade]
        GPA = total_grade / total_credit
    result =(f'Course: {new_cource}\nYour total Credits is: {total_credit}\nYour total A.K is: {total_grade}\nYour GPA is: {GPA}')
    print (result)
    output()

def gpa_calc2():
    global Wcredit, Tcredit
    n = int(input(f'\n{ques}How many courses do you have this semester? : '))
    list_courses = {}
    list_credits = {}

    new_sum = 0  # Initialize sum of weighted grades
    new_credit = 0  # Initialize sum of credits

    for i in range(n):
        print(f'\n{cc}Course {i+1}')
        credit = int(input(f'\n{ques}Enter the credit of course {i+1}: '))
        list_credits[i+1] = credit

        single_course()  # Calls function to get total grade for the course
        list_courses[i+1] = total  # Store total grade for the course

        # Find letter grade corresponding to total
        for letter, (min_val, max_val) in grade_range.items():
            if min_val <= total <= max_val:
                weighted_grade = letter_grades[letter] * credit
                new_sum += weighted_grade
                break  # Stop checking once the letter grade is found

        new_credit += credit  # Update total credits

    # If previous credits exist, add them
    try:
        new_credit += Tcredit
        new_sum += Wcredit
    except Exception:
        pass  # Ignore if they are not set

    # Calculate and display final GPA
    GPA = new_sum / new_credit
    print(f'\n{cc}Your total Credits is: {new_credit}')
    print(f'{cc}Your total A.K is: {new_sum}')
    print(f'{cc}Your GPA is: {GPA}')
    result =(f'\nYour total Credits is: {new_credit}\nYour total A.K is: {new_sum}\nYour GPA is: {GPA}')
    output()
    # print(f'{cc}Courses: {list_courses}, Credits: {list_credits}')

def main():
    global new_sum, new_credit, n
    if user_choice == 1:
        sem = input(f'\n{ques} Is this your first semester? (y/n) : ')
        if sem.lower() == 'n':
            previos()
            n = int(input(f'\n{ques}How many courses do you have? : '))
            gpa_calc()
        else:
            n = int(input(f'\n{ques}How many courses do you have? : '))
            gpa_calc()
        
    elif user_choice == 2:
        sem = input(f'\n{ques} Is this your first semester? (y/n) : ')
        if sem.lower() == 'n':
            previos()
            gpa_calc2()
        else:
            gpa_calc2()
       
    elif user_choice == 3:  
        single_course()
    elif user_choice == 4:
        passing_grade()


if __name__ == "__main__":
    main()
    input("\nPress Enter to exit...")  # Keeps the terminal open

    
        


