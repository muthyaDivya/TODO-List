# TO-DO-List
This is a command-line-based To-Do List app built using Python and SQLite. It allows users to add, view, update, and delete tasks stored in an SQLite database (todo.db).
# Features
** Add Tasks → Users can add tasks with a status (e.g., Pending, In Progress, Complete).
** View Tasks → Displays all tasks stored in the SQLite database.
** Update Tasks → Marks a task as Complete.
** Delete Tasks → Removes a task from the database.

# Installation & Setup
1️. Clone the Repository
2️. Run the To-Do App
    **python todo.py**
    
#  Project Structure
/todo-list/
│── todo.py         # Main Python script
│── todo.db         # SQLite database (created automatically)
│── README.md       # Project documentation

# Functionality Overview
Function	                Description
add_task(task, status)  	Adds a new task with a status (e.g., "Pending")
view_tasks()              Displays all tasks from the database
update_task(task_id)  	  Marks a task as Complete
delete_task(task_id)  	  Deletes a task using its ID
main_call()  	            The main loop that provides a menu for users

#  How to Use

**python todo.py**
To-Do List App
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Exit

**Example Actions:**

Add a task → Enter task name & status (Pending or In Progress).
View all tasks → Displays stored tasks.
Mark a task as complete → Enter the task ID to update.
Delete a task → Enter the task ID to remove it.
