# Import necessary modules
import datetime

# LOGIN SECTION

# Initialize lists for storing user data
list_of_users = []
list_of_passwords = []

# Open and read only the user.txt file and populate the user data lists
with open('user.txt', 'r') as existing_users:
    for line in existing_users:
        # Remove newlines and divide the values using comma and space as separators
        # Add the usernames, which are at index 0, to the list_of_users
        # Add the passwords, which are at index 1, to the list_of_passwords
        existing_users_split = line.strip().split(", ")
        list_of_users.append(existing_users_split[0])
        list_of_passwords.append(existing_users_split[1])

# A loop that continuously accepts username and password, and verifies their validity
while True:
    # Request user to enter username and password
    username_input = input("Please enter your username: ")
    password_input = input("Please enter your password: ")
    
    # Verify the correctness of both username and password
    # If they are not correct, prompt for input again
    if username_input not in list_of_users or password_input not in list_of_passwords:
        print("Invalid username and/or password. Please try again.")
        continue
    # If the username and password are correct, the user is successfully logged in
    else:
        print("You have successfully logged in!")
        break

# A loop that continuously accepts a menu option and navigates the user to the selected function
while True:

    if username_input == "admin":
    # Display the menu options to the user
    # Make sure that the user's input is transformed to lower case
        menu = input('''Select one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
ds - display task statistics
e - exit
: ''').lower()
        
    else:
        menu = input('''Select one of the following options:
a - add task
va - view all tasks
vm - view my taks
e - exit
: ''').lower()

    ################################################################################################################################################################# 
    #REGISTER NEW USER

    if menu == 'r':
        # Only admin users can register a new user
        if username_input == "admin":
            
            # A loop that continuously accepts a new username and password, and verifies their authenticity
            while True:
                # Request user to input:
                # new username;
                # new password;
                # password confirmation.
                new_username = input("Please create a new username: ")
                new_password = input("Please create a new password: ")
                new_password_confirmation = input("Please confirm your password: ")
                
                # Check if passwords match
                if new_password != new_password_confirmation:
                    print("Passwords do not match. Please try again.")
                    continue
                # Check if username already exists
                elif new_username in list_of_users:
                    print("User already exists. Please try again.")
                    continue
                # Check if password contains a digit
                elif not any(char.isdigit() for char in new_password):
                    print("Password should contain at least 1 digit. Please try again.")
                    continue
                # Check if password contains at least 5 characters
                elif len(new_password) < 5:
                    print("Password should contain at least 5 characters. Please try again.")
                    continue
                else:
                    # If new user details pass all validation checks, write new user details in user.txt
                    with open('user.txt', 'a') as register_user:
                        register_user.write(f"\n{new_username}, {new_password}")
                    print(f"You have successfully registered the user {new_username}!")
                    break
        
        # Non-admin users do no have access to this function
        else:
            print("You do not have the necessary permissions to register a user.")
            continue
        
        #########################################################################################################################
#                                                 ADD NEW TASK

        
    elif menu == 'a':
        
        # Open tasks.txt in append mode as add_task
        add_task = open('tasks.txt', 'a')
        
        # Request user to enter:
            # username;
            # task title;
            # task description;
            # due date.
        new_task_usernames = input("Please enter username of the person who the task is assigned to: ").replace(",", "")
        new_task_titles = input("Please enter a title for the task: ").replace(",", "")
        new_task_descriptions = input("Please enter a description of the task: ").replace(",", "")
        new_task_due_dates = input("Please enter the due date of the task (dd Mon YYYY): ").replace(",", "")
        # Extract today's date in dd Mon YYYY format
        new_task_creation_dates = datetime.date.today().strftime("%d %b %Y")
        
        # Write task details into task.txt
        add_task.write(f"\n{new_task_usernames}, {new_task_titles}, {new_task_descriptions}, {new_task_creation_dates}, {new_task_due_dates}, No")
        print("Task successfully added")
        
        # Flush add_task to ensure changes are written to tasks.txt
        add_task.flush()
        
        # Close tasks.txt file
        add_task.close()
        pass


#                                                 VIEW ALL TASKS

    
    elif menu == 'va':
        
        # Open tasks.txt in read-only mode as "all_tasks"
        all_tasks = open('tasks.txt', 'r')
        
        for line in all_tasks:
            # Remove newlines and divide the values using comma and space as separators
# Retrieve task details using the slicing technique
            all_tasks_split = line.strip().split(", ")
            task_username = all_tasks_split[0]
            task_title = all_tasks_split[1]
            task_description = all_tasks_split[2]
            task_creation_date = all_tasks_split[3]
            task_due_date = all_tasks_split[4]
            task_complete = all_tasks_split[5]
            
            # Create 2 lists:
                # task_headings;
                # task_details.
            task_headings = ["Task:", "Assigned to:", "Date assigned:", "Due date:", "Task complete?", "Task description:"]
            task_details = [task_title, task_username, task_creation_date, task_due_date, task_complete, task_description]
            
            # Utilize the zip() function to iterate over task_headings as x
# Correspond each value in task_details with the matching task_heading, denoted as y
            for x, y in zip(task_headings, task_details):
                print(f"{x:30}\t{y}")  # Width must be 30 for headings column
            print("\u2500" * 100)  # Print solid the line beneath each of the loop using unicode
            print()  
        
        # Close tasks.txt file
        all_tasks.close()
        pass


#                                              VIEW USER-SPECIFIC TASKS


    elif menu == 'vm':
        
        # Declare boolean variable called "tasks_found"
        tasks_found = False
        
        # Open tasks.txt in read-only mode as "my_tasks"
        all_tasks = open('tasks.txt', 'r')
        
        for line in all_tasks:
            # Remove newlines and divide the values using comma and space as separators
# Retrieve task details using the slicing technique
            all_tasks_split = line.strip().split(", ")
            task_username = all_tasks_split[0]
            task_title = all_tasks_split[1]
            task_description = all_tasks_split[2]
            task_creation_date = all_tasks_split[3]
            task_due_date = all_tasks_split[4]
            task_complete = all_tasks_split[5]

            # Create 2 lists:
                # task_headings;
                # task_details.
            task_headings = ["Task:", "Assigned to:", "Date assigned:", "Due date:", "Task complete?", "Task description:"]
            task_details = [task_title, task_username, task_creation_date, task_due_date, task_complete, task_description]
            
            # Check user's input name against usernames in tasks.txt
            if username_input == task_username:
                # If tasks are found for user, tasks_found = True
                tasks_found = True
                # Use the zip() function to iterate over task_headings, represented as x
# Pair each value in task_details with its corresponding task_heading, denoted as y
                for x, y in zip(task_headings, task_details):
                    print(f"{x:30}\t{y}") # Width of 30 for headings column
                print("\u2500" * 100)
                print() 
        
        # If no tasks are found for user, print message
        if not tasks_found:
            print("You do not have a task assigned to you at the moment. Please check again later.")
        
        # Close tasks.txt file
        all_tasks.close()
        pass
    

#                                                  DISPLAY TASK STATISTICS

    
    elif menu == "ds":
        
        # Only admin users can view task statistics
        if username_input == "admin":
            
            # Update list of users
            list_users = []
            with open('user.txt', 'r') as existing_users:
                for line in existing_users:
                # Remove newlines and divide the values using comma and space as separators
# Add the usernames, which are at index 0, to the list_of_users
                    existing_users_split = line.strip().split(", ")
                    list_users.append(existing_users_split[0])

            # Save len(list_of_users) as "no_of_users"
            no_of_users = len(list_users)
            
            # Declare 2 empty lists:
                # task_users;
                # unassigned_users.
            task_users = []
            unassigned_users = []
            
            # Open tasks.txt in read-only mode as "tasks_file"
            with open('tasks.txt', 'r') as tasks_file:
                lines = tasks_file.readlines()

            # Declare 2 int variables:
                # no_of_tasks;
                # completed_tasks.
            no_of_tasks = 0
            completed_tasks = 0

            # Add 1 to no_of_task for each line in tasks.txt
            for line in lines:
                no_of_tasks += 1
                
                # Remove newlines and divide the values using comma and space as separators
# Retrieve task users and completion status using the slicing technique
# Add the users to the task_users list
                task_file_split = line.split(", ")
                task_users.append(task_file_split[0])
                task_completed_column = task_file_split[5]
                
                # If Task Completed == "Yes", add 1 to completed_tasks
                if "Yes" in task_completed_column:
                    completed_tasks += 1

            # Calculate percentage of complete tasks
            # Calculation: completed_tasks/no_of_tasks * 100
            percent_complete = round(completed_tasks/no_of_tasks * 100, 2)

            # Identify common elements between list_of_users and task_users
# If a user is not found in task_users, add that user to the unassigned_users list
            for i in list_of_users:
                if i not in task_users:
                    unassigned_users.append(i)
            
            # Convert unassigned_users to str
            unassigned_users_list = ', '.join(unassigned_users) if len(unassigned_users) >= 1 else "None"
            # Calculate no_of_assigned_users as no_of_users - len(unassigned_users)
            no_of_assigned_users = no_of_users - len(unassigned_users)
            # Calculate resource_allocation as a ration of assigned to unassigned users
            resource_allocation = round(no_of_assigned_users / no_of_users * 100, 2)
            
            # Create 2 lists:
                # stats_headings;
                # stats_details.
            stats_headings = ["Total no. of users:", "Total no. of tasks:", "Percent completed tasks:", "Percent resource allocation:", "Unassigned user/s:"]
            stats_details = [no_of_users, no_of_tasks, percent_complete, resource_allocation, unassigned_users_list]
            
            # Using zip() method, print out stats_headings as x
            # Match each value in stats_details with corresponding stats_headings, as y
            for x, y in zip(stats_headings, stats_details):
                print(f"{x:30}\t{y}") # Width of 30 for headings column
            print("\u2500" * 100) 
            print() 

        # Non-admin users do not have access to statistics
        else:
            print("Invalid input. Please try again.")

        pass


#                                                  EXIT PROGRAM

    
    elif menu == 'e':
        print('Goodbye!')
        exit() # Exit the program

#                                                  INVALID INPUT

    
    else:
        print("Invalid input. Please try again.")
        continue