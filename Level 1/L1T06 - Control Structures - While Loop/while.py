# From statistics module we will import mean

from statistics import mean

# create an empty list called user_numbers
# We will use this empty list to store numbers inputed by user.

numbers = []

while True:
        
# Request the user to input any number
# check that the number is indeed a number using int(input())
# Store number into variable called "input_number"
        
        input_number = int(input("Enter a number: "))

# If the input_number == -1
# output the average of numbers inputed
# use "break" to end the loop
        
        if input_number == -1:
            print(round(mean(numbers)))
            break

# If the input_number is not -1
# Append each input to the numbers list
# Loop back to input, continually request user to enter a number using 'continue'
        
        else:
            numbers.append(input_number)
            continue

