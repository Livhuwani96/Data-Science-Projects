# Declare a message variable with the string "Please enter three different integers"
message = ("Please enter three different integers")

# Display the message to the user
print(message)

# Ask the user to enter the first, second and third number and convert it to an integer
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

# Calculate the sum of the three numbers and store it in a variable
# Display the sum to the user
sum = num1 + num2 + num3
print ("The sum is:", sum)

# Calculate the difference between the first and second numbers and store it in a variable
# Display the difference to the user

minus = num1 - num2
print (minus)

# Calculate the product of the third and first numbers and store it in a variable
# Display the results
multiply = num3 * num1
print (multiply)

#divide sum of all 3 values entered by num captured on num3
#print results.
divide = sum / num3
print (divide)