import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")

        # Frame para la lista de eventos
        self.frame_lista = ttk.Frame(root)
        self.frame_lista.pack(pady=10)

        # Treeview para mostrar los eventos
        self.tree = ttk.Treeview(self.frame_lista, columns=("Fecha", "Hora", "Descripción"), show="headings")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.pack()

        # Frame para los campos de entrada
        self.frame_entrada = ttk.Frame(root)
        self.frame_entrada.pack(pady=10)

        ttk.Label(self.frame_entrada, text="Fecha:").grid(row=0, column=0, padx=5, pady=5)
        self.fecha_entry = DateEntry(self.frame_entrada, width=12, background="darkblue", foreground="white", borderwidth=2)
        self.fecha_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.frame_entrada, text="Hora:").grid(row=1, column=0, padx=5, pady=5)
        self.hora_entry = ttk.Entry(self.frame_entrada)
        self.hora_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self.frame_entrada, text="Descripción:").grid(row=2, column=0, padx=5, pady=5)
        self.descripcion_entry = ttk.Entry(self.frame_entrada, width=30)
        self.descripcion_entry.grid(row=2, column=1, padx=5, pady=5)

        # Frame para los botones
        self.frame_botones = ttk.Frame(root)
        self.frame_botones.pack(pady=10)

        self.btn_agregar = ttk.Button(self.frame_botones, text="Agregar Evento", command=self.agregar_evento)
        self.btn_agregar.grid(row=0, column=0, padx=5, pady=5)

        self.btn_eliminar = ttk.Button(self.frame_botones, text="Eliminar Evento", command=self.eliminar_evento)
        self.btn_eliminar.grid(row=0, column=1, padx=5, pady=5)

        self.btn_salir = ttk.Button(self.frame_botones, text="Salir", command=root.quit)
        self.btn_salir.grid(row=0, column=2, padx=5, pady=5)

    def agregar_evento(self):
        fecha = self.fecha_entry.get()
        hora = self.hora_entry.get()
        descripcion = self.descripcion_entry.get()

        if fecha and hora and descripcion:
            self.tree.insert("", "end", values=(fecha, hora, descripcion))
            self.hora_entry.delete(0, tk.END)
            self.descripcion_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")

    def eliminar_evento(self):
        seleccionado = self.tree.selection()
        if seleccionado:
            if messagebox.askyesno("Confirmar", "¿Está seguro de eliminar este evento?"):
                for item in seleccionado:
                    self.tree.delete(item)
        else:
            messagebox.showwarning("Advertencia", "Seleccione un evento para eliminar.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()
