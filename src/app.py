import tkinter as tk
from tkinter import messagebox
import json
import os

from src.config import APP_TITLE, WINDOW_SIZE, DATA_FILE


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x450")
        self.tasks = []

        self.create_widgets()
        self.load_tasks()

    def create_widgets(self):
        self.entry = tk.Entry(self.root, width=30)
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", lambda event: self.add_task())

        self.add_button = tk.Button(
            self.root, text="Adicionar Tarefa", command=self.add_task
        )
        self.add_button.pack()

        self.listbox = tk.Listbox(self.root, width=40, height=15)
        self.listbox.pack(pady=10)

        self.remove_button = tk.Button(
            self.root, text="Remover Tarefa", command=self.remove_task
        )
        self.remove_button.pack()

    def add_task(self):
        task = self.entry.get()
        if task:
            self.tasks.append(task)
            self.listbox.insert(tk.END, task)
            self.entry.delete(0, tk.END)
            self.save_tasks()
        else:
            messagebox.showwarning("Aviso", "Digite uma tarefa.")

    def remove_task(self):
        try:
            index = self.listbox.curselection()[0]
            self.listbox.delete(index)
            self.tasks.pop(index)
            self.save_tasks()
        except IndexError:
            messagebox.showwarning("Aviso", "Selecione uma tarefa.")

    def load_tasks(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r", encoding="utf-8") as file:
                self.tasks = json.load(file)
                for task in self.tasks:
                    self.listbox.insert(tk.END, task)

    def save_tasks(self):
        os.makedirs("data", exist_ok=True)
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(self.tasks, file, indent=4, ensure_ascii=False)
