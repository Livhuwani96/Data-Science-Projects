#I have a long sentance that is written in a way that is not easy to read.
#I will create a variable called gibberish_string.
#Input and store the sentence i stored in my variable.
gibberish_string = "The!quick!brown!fox!jumps!over!the!lazy!dog."

#using the replace() function, i'm going to replace unwanted char, print the results.
gibberish_string = gibberish_string.replace ("!", " ")
print(gibberish_string)
#using the upper() funtion, reprint the the sentence in upper case.
corrected_string = gibberish_string.upper()
print(corrected_string)

#create a slice that starts at the end of the string moving backwards.
reverse_sen = corrected_string
print(corrected_string[::-1])