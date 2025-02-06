# Initialize an empty list named "stu_ids"
# Intended for holding the IDs of the students
stu_id = []

# Define a function named "get_suffix"
# This function determines the correct ordinal suffix for a number
# Parameters: num_students (int): The count of students
# Return: str: Ordinal suffix corresponding to the number (e.g., "st", "nd", "rd", "th")
def get_suffix(number_students):
    if 10 < number_students % 100 < 20:
        number_students_suffix = "th"
    else:
        last_digit = number_students % 10
        if last_digit == 1:
            number_students_suffix = "st"
        elif last_digit == 2:
            number_students_suffix = "nd"
        elif last_digit == 3:
            number_students_suffix = "rd"
        else:
            number_students_suffix = "th"
    return number_students_suffix

while True:
    # Prompt the user to input the student count
    no_of_students = int(input("How many students are you registering? "))

    # Verify the entered student count with the user
    students_confirm = input(f"You are registering {no_of_students} students. Continue? (y/n) ")
    
    # Establish valid yes/no options for the verification
    yes_choices = ["yes", "y"]
    no_choices = ["no", "n"]

    # Redirect to input prompt if verification fails
    # Process input to be case-insensitive and trim spaces
    if students_confirm.lower().replace(" ", "") not in no_choices + yes_choices:
        print("Please enter a valid input (y/n).")
        continue

    # If the user selects "no", return to input
    # Clean the input to ignore case and spaces
    elif students_confirm.lower().replace(" ", "") in no_choices:
        print("Please re-enter the number of students you are registering.")
        continue
    # If the user selects "yes":
    else:
        # Start the range from 1 to accommodate the student IDs input
        for i in range(1, no_of_students + 1):
            # Invoke the get_suffix function
            # Assign the correct ordinal suffix to the number

            number_students_suffix = get_suffix(i)
            student_id = input(f"Please input {i}{number_students_suffix} Student ID: ")
    
            # Append the student IDs to stu_id list
            stu_id.append(student_id)
    break

# Print the student IDs in a new line
print("You have successfully registered the following student IDs:", *stu_id, sep="\n")

# Open the new text file called "reg_form.txt"
reg_form = open('reg_form.txt', 'w')

# Write heading "Exam Register"
reg_form.write("Exam Register:\n\n")

# capure student ID into reg_form
for item in stu_id:
    reg_form.write(item + " ...............\n")

# Close the reg_form
reg_form.close()
