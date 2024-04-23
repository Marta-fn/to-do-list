import tkinter as tk
from tkinter import filedialog
from ttkbootstrap import Style

class ToDoListApp(tk.Tk):
  def __init__(self):
    super().__init__()

    self.title("My To-do List App")
    self.geometry("400x400")
    style = Style(theme="minty")
    style.configure("Custon.TEntry", foreground="white")

    self.create_widgets()
  
  def create_widgets(self):
    self.task_input = tk.Entry(self, width=38)
    self.task_input.pack(pady=10)

    self.add_task_buttom = tk.Button(self, text="Add Task", command=self.add_task)
    self.add_task_buttom.pack(pady=5)

    self.task_list = tk.Listbox(self, selectmode=tk.SINGLE)
    self.task_list.pack(pady=5)

    self.button_frame = tk.Frame(self)
    self.button_frame.pack(pady=5)

    self.edit_task_button = tk.Button(self.button_frame, text="Edit Text", command=self.edit_task)
    self.edit_task_button.grid(row=0, column=0, padx=5)

    self.delete_task_button = tk.Button(self.button_frame, text="Delete task", command=self.delete_task)
    self.delete_task_button.grid(row=0, column=1, padx=5)

    self.save_button = tk.Button(self, text="Save", command=self.save_tasks)
    self.button_frame.pack(pady=5)

    self.load_button = tk.Button(self, text="Load", command=self.load_tasks)
    self.button_frame.pack(pady=5)

    