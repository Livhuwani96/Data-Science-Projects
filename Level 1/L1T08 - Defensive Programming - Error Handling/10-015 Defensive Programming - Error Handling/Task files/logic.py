# Creating a program to count from 0 to 10
# Print a welcome message
print("Welcome to the counter")

# Initialize a counter
count = 0

# Let's try to count up to 10                                                                                                                                                                                                                      
# I have used a - instead of + on my code and that will result in the opposite of what the code is supposed to do.
while count <= 10:
    print(f"Count: {count}")
    count -= 1  
# After running the code we will be stuck in an infinite loop
# Press Ctrl+C to escape the loop otherwise it will not stop counting.
# To have the code count from 0 to 10, channge count -= 1 and make it count += 1.