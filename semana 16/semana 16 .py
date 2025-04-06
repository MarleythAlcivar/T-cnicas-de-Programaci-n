import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")
        self.root.geometry("400x400")

        # Campo de entrada
        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=10)
        self.entry.focus()

        # Lista de tareas
        self.task_listbox = tk.Listbox(root, width=50, height=15)
        self.task_listbox.pack(pady=10)

        # Botones
        button_frame = tk.Frame(root)
        button_frame.pack(pady=5)

        self.add_button = tk.Button(button_frame, text="Añadir Tarea", command=self.add_task)
        self.add_button.grid(row=0, column=0, padx=5)

        self.complete_button = tk.Button(button_frame, text="Completar Tarea", command=self.complete_task)
        self.complete_button.grid(row=0, column=1, padx=5)

        self.delete_button = tk.Button(button_frame, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.grid(row=0, column=2, padx=5)

        # Atajos de teclado
        self.root.bind('<Return>', lambda event: self.add_task())
        self.root.bind('<c>', lambda event: self.complete_task())
        self.root.bind('<C>', lambda event: self.complete_task())
        self.root.bind('<d>', lambda event: self.delete_task())
        self.root.bind('<D>', lambda event: self.delete_task())
        self.root.bind('<Delete>', lambda event: self.delete_task())
        self.root.bind('<Escape>', lambda event: self.root.quit())

    def add_task(self):
        task = self.entry.get()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Campo vacío", "Por favor, escribe una tarea.")

    def complete_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            task = self.task_listbox.get(index)
            if not task.startswith("✔ "):
                self.task_listbox.delete(index)
                self.task_listbox.insert(index, f"✔ {task}")
        else:
            messagebox.showwarning("Selección", "Selecciona una tarea para marcar como completada.")

    def delete_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            self.task_listbox.delete(selected[0])
        else:
            messagebox.showwarning("Selección", "Selecciona una tarea para eliminarla.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
