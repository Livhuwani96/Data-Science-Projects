# Changed print "Welcome to the error program" to print("Welcome to the error program") for Python 3 syntax.


print("Welcome to the error program")
print("\n")

# Fixed the variable assignment age_Str == "24 years old" to age_Str = "24" for correct assignment.
# Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = "24"
age = int(age_Str)

# Corrected the print statement print("I'm" + age + "years old.") to print("I'm " + str(age) + " years old.") to convert age to a string for concatenatio

print("I'm " + str(age) + " years old.")

# Variables declaring additional years and printing the total years of age
# Changed years_from_now = "3" to years_from_now = 3 to use an integer.
years_from_now = 3
total_years = age + years_from_now


# Corrected the print statement print "The total number of years:" + "answer_years" to print("The total number of years: " + str(total_years)).
print("The total number of years: " + str(total_years))

# Variable to calculate the total amount of months from the total amount of years and printing the result
# Changed total * 12 to total_years * 12 to calculate the total months correctly.
# Converted total_months to a string for concatenation in the final print statement.
total_months = total_years * 12
print("In 3 years and 6 months, I'll be " + str(total_months) + " months old")

