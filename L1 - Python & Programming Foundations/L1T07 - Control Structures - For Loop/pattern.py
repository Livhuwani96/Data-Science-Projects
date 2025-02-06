# Define the number of rows for the pattern
row_num = 5

# Loop through each row for the stars to be repeated up until 5
for i in range(1, row_num * 2):
    if i <= row_num:

        # Print increasing number of stars up until each line has a star added to it.
        print("*" * i)
    else:
        # Once the program has counted up to 5, print decreasing number of stars from 5 to 1.
        print("*" * (2 * row_num - i))