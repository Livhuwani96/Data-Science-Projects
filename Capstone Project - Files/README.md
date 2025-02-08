# Task Manager

## Project Overview  
This **Task Manager** program is designed to help a small business manage tasks assigned to team members. The program allows users to **log in, assign tasks, track task progress, and generate user statistics**.  

Built as part of my **Data Science Bootcamp at HyperionDev**, this project strengthened my skills in **file handling, user authentication, and Python programming**.  

---

# Features  
✔ **User Authentication** – Secure login system using `user.txt`  
✔ **User Registration** – Admin-only feature to add new users  
✔ **Task Management** – Add, view, and track tasks  
✔ **Task Storage** – Tasks are saved in `tasks.txt`  
✔ **Admin Statistics** – View total users and tasks  

---

# How It Works  
# 1 **Login System**  
- Users must enter valid credentials stored in `user.txt`.  
- Admin (`admin, adm1n`) has additional privileges.  

# 2️ **Menu Options**  
| Option | Description |
|--------|------------|
| `r` | Register a new user (Admin only) |
| `a` | Add a new task |
| `va` | View all tasks |
| `vm` | View tasks assigned to the logged-in user |
| `ds` | View task statistics (Admin only) |
| `e` | Exit the program |

---

# File Structure  
- **`task_manager.py`** → The main Python script  
- **`user.txt`** → Stores usernames & passwords  
- **`tasks.txt`** → Stores task details  

---
