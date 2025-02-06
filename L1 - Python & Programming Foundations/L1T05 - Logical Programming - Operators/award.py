# Ask for the uswer to input the times of each event.
# Store each time in it's own variable created.

swimming_time = float(input("Enter your swimming time): "))
cycling_time = float(input("Please enter your cycling time): "))
running_time = float(input("Please enter your running time:"))


# Create a new variable called total time and use it to calculate the values inputed by user.
# Display the total time taken in all activities.
total_time = swimming_time + cycling_time + running_time
print("Total time to complete:", total_time, "minutes")

# Determine and print the award based on the total minutes taken
if total_time <= 100:
    award = "Provincial Colours"
elif 101 <= total_time <=105:
    award = "Provincial Half Colours"
elif 106 <= total_time <= 110:
    award = "provincial scroll"
else:
    award = "No award"

print(f"Award: {award}")