# define the conversion function first
def convert_to_letter_grade(percentage):
    letter_grade = None

    if percentage >= 90:
        letter_grade = "A+"
    elif percentage >= 85:
        letter_grade = "A"
    elif percentage >= 80:
        letter_grade = "A-"
    elif percentage >= 77:
        letter_grade = "B+"
    elif percentage >= 73:
        letter_grade = "B"
    elif percentage >= 70:
        letter_grade = "B-"
    elif percentage >= 67:
        letter_grade = "C+"
    elif percentage >= 63:
        letter_grade = "C"
    elif percentage >= 60:
        letter_grade = "C-"
    elif percentage >= 57:
        letter_grade = "D+"
    elif percentage >= 53:
        letter_grade = "D"
    elif percentage >= 50:
        letter_grade = "D-"
    else:
        letter_grade = "F"

    return letter_grade


# prompt user for a percentage grade
print("Hi there, please enter your percentage grade: (i.e., 85 is 85%)")
user_percentage_grade = int(input())
# convert the percentage grade into a letter grade
letter_grade = convert_to_letter_grade(user_percentage_grade)

# output the converted letter grade
print("Your percentage grade in letter format is:\n{}".format(letter_grade))
