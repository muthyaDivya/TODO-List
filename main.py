import sqlite3 as sql

Connection = sql.connect("todo.db")
cursor = Connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT NOT NULL,
    status TEXT NOT NULL
)
""")
Connection.commit()

#! Function to add a task
def add_task(task,status):
    cursor.execute("""
                INSERT INTO tasks (task, status) VALUES (?, ?)""", (task,status))
    Connection.commit()
    print("Task added successfully!")

#! Function to View all the tasks
def view_tasks():
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()

    if tasks:
        print("\n TO-Do List:")
        for task in tasks:
            print(f"{task[0]}. {task[1]}- {task[2]}")
    else:
        print("\n No tasks found")

#! Function to Update a task
def update_task(task_id):
    cursor.execute("UPDATE tasks SET status = 'Complete' WHERE id = ?",(task_id,))
    Connection.commit()
    print("Task Updated Successfully")

#! Funnction to Delete a task
def delete_task(task_id):
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    Connection.commit()
    print("Task deleted successfully")

#! Main Function of To-Do List
def main_call():
    while True:
        print("\nTo-Do List App")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = int(input("Select an option: "))
        print(choice)
        if choice == 1:
            task = input("Enter the task: ")
            status = input("Enter the status: ")
            add_task(task,status)
        elif choice == 2:
            view_tasks()
        elif choice == 3:
            task_id = int(input("Enter the task ID to mark as complete: "))
            update_task(task_id)
        elif choice == 4:
            task_id = int(input("Enter the task ID to delete: "))
            delete_task(task_id)
        elif choice == 5:
            print("Good Bye!")
            break
        else:
            print("Invalid selection, please try again!")

main_call()


