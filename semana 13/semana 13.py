import tkinter as tk
from tkinter import ttk, messagebox


class AplicacionTareas:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")
        self.root.geometry("500x400")
        self.root.resizable(True, True)

        # Variables
        self.var_tarea = tk.StringVar()

        # Crear frames
        self.frame_input = ttk.Frame(root, padding="10")
        self.frame_input.pack(fill=tk.X)

        self.frame_lista = ttk.Frame(root, padding="10")
        self.frame_lista.pack(fill=tk.BOTH, expand=True)

        self.frame_botones = ttk.Frame(root, padding="10")
        self.frame_botones.pack(fill=tk.X)

        # Componentes para agregar tareas
        ttk.Label(self.frame_input, text="Nueva Tarea:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        ttk.Entry(self.frame_input, textvariable=self.var_tarea, width=40).grid(row=0, column=1, padx=5, pady=5)

        # Lista de tareas
        self.columnas = ('tarea',)
        self.tree = ttk.Treeview(self.frame_lista, columns=self.columnas, show='headings')

        # Definir encabezados
        self.tree.heading('tarea', text='Tarea')

        # Configurar columnas
        self.tree.column('tarea', width=450, anchor=tk.W)

        # Scrollbar para la lista
        scrollbar = ttk.Scrollbar(self.frame_lista, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)

        # Empaquetar lista y scrollbar
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Botones
        ttk.Button(self.frame_botones, text="Agregar", command=self.agregar_tarea).pack(side=tk.LEFT, padx=5)
        ttk.Button(self.frame_botones, text="Eliminar", command=self.eliminar_tarea).pack(side=tk.LEFT, padx=5)
        ttk.Button(self.frame_botones, text="Limpiar Todo", command=self.limpiar_lista).pack(side=tk.LEFT, padx=5)

    def agregar_tarea(self):
        tarea = self.var_tarea.get().strip()

        if tarea:
            self.tree.insert('', tk.END, values=(tarea,))
            self.var_tarea.set("")  # Limpiar el campo de entrada
        else:
            messagebox.showwarning("Advertencia", "Por favor ingrese una tarea.")

    def eliminar_tarea(self):
        seleccionado = self.tree.selection()
        if seleccionado:
            for item in seleccionado:
                self.tree.delete(item)
        else:
            messagebox.showinfo("Información", "Por favor seleccione una tarea para eliminar.")

    def limpiar_lista(self):
        confirmacion = messagebox.askyesno("Confirmar", "¿Está seguro que desea eliminar todas las tareas?")
        if confirmacion:
            for item in self.tree.get_children():
                self.tree.delete(item)


if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionTareas(root)
    root.mainloop()