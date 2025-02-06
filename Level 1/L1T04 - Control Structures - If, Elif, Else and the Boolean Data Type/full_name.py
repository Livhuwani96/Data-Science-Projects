#Create variable call full_name to store the user's input.
#Request user to enter their full name.
full_name = input("Please enter your name: ")

#Read user's input
#if they have captured nothing, return message and request input again.
if len(full_name) == 0:
    print("You haven't entered anything. Please enter your full name")

#Repeat the process from beginnig
    full_name = input("Please enter your name: ")


#Read user's input
#if they have captured nothing, return message and request input again.
elif len(full_name) < 4:
    print("You have entered less than 4 characters. Please make sure that you have enter you first name and surname")

    #Repeat the process from beginnig
    full_name = input("Please enter your name: ")

#Read user's input
#if they have captured nothing, return message and request input again.
elif len(full_name) > 25:
    input("You have entered more than 25 characters. Please make sure that you have only entered your full name")

    #Repeat the process from beginnig
    full_name = input("Please enter your name: ")

#Read user's input again.
#if user has entered correct full name that meets the required len print message.
else:
    print("Thank you for entering you name")