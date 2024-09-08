import tkinter as tk
from tkinter import messagebox

# Task List Data
tasks = []

# Command-Line Interface Functions

def add_task(task_name):
    tasks.append({"name": task_name, "completed": False})
    print(f"Task '{task_name}' added.")

def view_tasks():
    if not tasks:
        print("No tasks found.")
        return
    for idx, task in enumerate(tasks):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{idx + 1}. {task['name']} - {status}")

def update_task(index, completed):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = completed
        status = "Completed" if completed else "Pending"
        print(f"Task '{tasks[index]['name']}' marked as {status}.")
    else:
        print("Invalid task number.")

def delete_task(index):
    if 0 <= index < len(tasks):
        removed_task = tasks.pop(index)
        print(f"Task '{removed_task['name']}' deleted.")
    else:
        print("Invalid task number.")

def main_cli():
    while True:
        print("\nTo-Do List Application - CLI")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Choose an option: ")

        if choice == "1":
            task_name = input("Enter task name: ")
            add_task(task_name)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            view_tasks()
            index = int(input("Enter task number to update: ")) - 1
            completed = input("Mark as completed? (y/n): ").strip().lower() == 'y'
            update_task(index, completed)
        elif choice == "4":
            view_tasks()
            index = int(input("Enter task number to delete: ")) - 1
            delete_task(index)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

# GUI Application Class

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")

        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)

        self.task_listbox = tk.Listbox(self.frame, width=50, height=10)
        self.task_listbox.pack(side=tk.LEFT)

        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

        self.entry = tk.Entry(self.root, width=50)
        self.entry.pack(pady=10)

        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.complete_button = tk.Button(self.root, text="Complete Task", command=self.complete_task)
        self.complete_button.pack()

        self.delete_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack()

    def add_task(self):
        task_name = self.entry.get()
        if task_name:
            tasks.append({"name": task_name, "completed": False})
            self.update_listbox()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task name cannot be empty")

    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in tasks:
            status = "Completed" if task["completed"] else "Pending"
            self.task_listbox.insert(tk.END, f"{task['name']} - {status}")

    def complete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            tasks[index]["completed"] = True
            self.update_listbox()
        else:
            messagebox.showwarning("Warning", "No task selected")

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            tasks.pop(index)
            self.update_listbox()
        else:
            messagebox.showwarning("Warning", "No task selected")

# Main Entry Point

def main():
    print("Choose the interface:")
    print("1. Command-Line Interface (CLI)")
    print("2. Graphical User Interface (GUI)")
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        main_cli()
    elif choice == "2":
        root = tk.Tk()
        app = ToDoApp(root)
        root.mainloop()
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()
