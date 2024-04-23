import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from ttkbootstrap import Style

class ToDoListApp(tk.Tk):
  def __init__(self):
    super().__init__()

    self.title("My To-do List")
    self.iconbitmap("task.ico")
    self.geometry("400x515")
    self.resizable(False,False)
    style = Style()
    style.theme_use("minty")
    button_font = ttk.Style()
    button_font.configure(".", font=("Roboto", 16))

    self.create_widgets()
  
  def create_widgets(self):

    self.task_input = ttk.Entry(self, width=30, font=("Roboto", 16))
    self.task_input.pack(pady=10)

    self.task_input.insert(0, "Write your tasks here...")
    self.task_input.bind("<FocusIn>", self.clear_placeholder)
    self.task_input.bind("<FocusOut>", self.restore_placeholder)

    self.add_task_buttom = ttk.Button(self, text="Add Task", command=self.add_task, style="success.TButton")
    self.add_task_buttom.pack(pady=5)

    self.task_listbox = tk.Listbox(self, selectmode=tk.SINGLE, width=30, font=("Roboto", 16))
    self.task_listbox.pack(pady=5)

    self.done_task = ttk.Button(self, text="Done", style="success.TButton", command=self.mark_done)
    self.done_task.pack(pady=5)

    self.button_frame = tk.Frame(self)
    self.button_frame.pack(pady=5)

    self.edit_task_button = ttk.Button(self.button_frame, text="Edit Task", command=self.edit_task, style="info.TButton")
    self.edit_task_button.grid(row=0, column=0, padx=5)

    self.delete_task_button = ttk.Button(self.button_frame, text="Delete task", command=self.delete_task, style="danger.TButton")
    self.delete_task_button.grid(row=0, column=1, padx=5)

    self.save_button = ttk.Button(self.button_frame, text="Save", command=self.save_tasks)
    self.save_button.grid(row=1, column=0, padx=5, pady=5)

    self.load_button = ttk.Button(self.button_frame, text="Load", command=self.load_tasks)
    self.load_button.grid(row=1, column=1, padx=5, pady=5)

  def clear_placeholder(self, event):
    if self.task_input.get() == "Write your tasks here...":
      self.task_input.delete(0, tk.END)

  def restore_placeholder(self, event):
    if not self.task_input.get():
      self.task_input.insert(0, "Write your tasks here...")  

  def add_task(self):
    task = self.task_input.get()
    if task:
      self.task_listbox.insert(tk.END, task)
      self.task_input.delete(0, tk.END)
      self.restore_placeholder(None)

  def mark_done(self):
    task_index = self.task_listbox.curselection()
    if task_index:
      self.task_listbox.itemconfigure(task_index, fg="#78c2ad")

  def edit_task(self):
    task_index = self.task_listbox.curselection()
    if task_index:
      new_task = self.task_input.get()
      if new_task:
        self.task_listbox.delete(task_index)
        self.task_listbox.insert(task_index, new_task)
        self.task_input.delete(0, tk.END)
        self.restore_placeholder(None)

  def delete_task(self):
    task_index = self.task_listbox.curselection()
    if task_index:
      self.task_listbox.delete(task_index)

  def save_tasks(self):
    tasks = self.task_listbox.get(0, tk.END)
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    
    if file_path:
      with open(file_path, "w") as file:
        for task in tasks:
          file.write(task + "\n")
  
  def load_tasks(self):
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])

    if file_path:
      with open(file_path, "r") as file:
        tasks = [line.strip() for line in file.readlines()]

      self.task_listbox.delete(0, tk.END)

      for task in tasks:
        self.task_listbox.insert(tk.END, task)
