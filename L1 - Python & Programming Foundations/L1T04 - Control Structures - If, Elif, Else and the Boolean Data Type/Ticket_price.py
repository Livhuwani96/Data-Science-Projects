#create a variable and name it age, request user to input their age
#create another variable call it time, request user to iput the time which the movie will play at.
#create another variable to store ticket price aand assign a zero to it.

age = int(input("Enter your age: "))
time = int(input("Please enter the showtime(24-hour formart): "))
ticket_price = 0


#create a if statement that if the age is less than 12 years old, the ticket price should be R50.
#create another if statement (elif) that if the age is equal to and not less than 12 and not more than 60, ticket should be R75
#otherwise if the first two statements are false, which means the user inputed over 60 years, ticket should be on a pensior speacial and be R35

if age > 12:
    ticket_price = 50

elif 12 <= age > 60:
    ticket_price = 75

else:
    ticket_price = 35

#create another if statement that, if the showtime is after 17:00 add on the ticket price R2.
    
if time > 17:
    ticket_price += 2

print("Ticket Price: R" + str(ticket_price))
  