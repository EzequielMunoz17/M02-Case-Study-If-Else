# Ezequiel Munoz
# Case Study.py
# This app will accept student names and GPAs and test if the student qualifies for either the Dean's List or the Honor Roll.

def check_deans_list(gpa):
    if gpa >= 3.5:
        return True
    else:
        return False

def check_honor_roll(gpa):
    if gpa >= 3.25:
        return True
    else:
        return False

def process_student_record():
    last_name = input("Enter student's last name (or 'ZZZ' to quit): ")

    if last_name == 'ZZZ':
        return False

    first_name = input("Enter student's first name: ")
    gpa = float(input("Enter student's GPA: "))

    if check_deans_list(gpa):
        print(f"{first_name} {last_name} has made the Dean's List.")

    if check_honor_roll(gpa):
        print(f"{first_name} {last_name} has made the Honor Roll.")

    return True

# Process student records
record_count = 0

while True:
    record_count += 1
    print(f"\nProcessing record #{record_count}")
    result = process_student_record()

    if not result:
        break
