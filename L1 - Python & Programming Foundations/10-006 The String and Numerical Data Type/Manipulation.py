#Create a varible called str_manip.
#using input method, request user to input any sentance.
#print the results.
str_manip = input("Please enter a sentence: ")
print(str_manip)

#use len funtion to calculate and display the number of number of characters inputed.
print(len(str_manip))

#crate another variable to cast the main variable and use slice funtion to only cast the last letter of the string.
last_letter = str_manip[-1]

#Therefore replace the last letter and it's occurance on the string with a @sign
#print the results.
last_letter_replace = str_manip.replace(last_letter,"@")
print(last_letter_replace)

#Print the last 3 characters in str_manip backwards

backwards = str_manip[-3:]
rev_char = backwards[::-1]
print (rev_char)

# Create a five-letter word that is made up of the first three characters and the last two characters in str_manip
first_three = str_manip[:3]
last_two = str_manip[-2:]
five_letter_word = first_three + last_two
print (five_letter_word)


