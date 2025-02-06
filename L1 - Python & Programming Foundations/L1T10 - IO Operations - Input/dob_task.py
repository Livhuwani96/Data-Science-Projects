# Create a file named “DOB”.
# Open the file “DOB.txt” in read-only mode.
# Save its content into a variable called “dob_data”.

with open ('DOB.txt', 'r') as file:
     # Create 2 empty lists
    names_list = []
    birthdates_list = []

    for line in file:

         # To split the dob_data into columns:
         # The first two columns contain names (sliced at [:2]).
         # The last three columns contain birthdates (sliced at [2:]).

        file_split = line.split()
        names_list.append(file_split[:2])
        birthdates_list.append(file_split[2:])

# Print "Name:" preceding list of names

print("Name:")
for item in names_list:

    # Clean names_list by joining to a string with '[]' and ',' removed.
    # Print the clean names.

    clean_names = item[0], ' '.join(map(str, item[1:]))
    print(*clean_names)

# Print "Birthdate:" preceding list of birthdates.

print("\nBirthdate:")
for item in birthdates_list:

    # Clean birthdates_list by joining to a string with '[]' and ',' removed.
    # Print clean birthdates.

    clean_birthdates = item[0], ' '.join(map(str, item[1:]))
    print(*clean_birthdates)