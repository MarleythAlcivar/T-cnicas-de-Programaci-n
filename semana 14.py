import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

def agregar_evento():
    fecha = entry_fecha.get()
    hora = entry_hora.get()
    descripcion = entry_descripcion.get()
    if fecha and hora and descripcion:
        tree.insert("", "end", values=(fecha, hora, descripcion))
        entry_fecha.set_date("")
        entry_hora.delete(0, tk.END)
        entry_descripcion.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")

def eliminar_evento():
    seleccionado = tree.selection()
    if seleccionado:
        confirmacion = messagebox.askyesno("Confirmar", "¿Deseas eliminar el evento seleccionado?")
        if confirmacion:
            for item in seleccionado:
                tree.delete(item)
    else:
        messagebox.showwarning("Advertencia", "Selecciona un evento para eliminar.")

# Crear ventana principal
root = tk.Tk()
root.title("Agenda Personal")
root.geometry("500x400")
root.resizable(False, False)

# Frame para la lista de eventos
frame_lista = tk.Frame(root)
frame_lista.pack(pady=10)

# Treeview para mostrar eventos
tree = ttk.Treeview(frame_lista, columns=("Fecha", "Hora", "Descripción"), show="headings")
tree.heading("Fecha", text="Fecha")
tree.heading("Hora", text="Hora")
tree.heading("Descripción", text="Descripción")
tree.pack()

# Frame para entrada de datos
frame_entrada = tk.Frame(root)
frame_entrada.pack(pady=10)

tk.Label(frame_entrada, text="Fecha:").grid(row=0, column=0)
entry_fecha = DateEntry(frame_entrada, width=12, background='darkblue', foreground='white', borderwidth=2)
entry_fecha.grid(row=0, column=1, padx=5)

tk.Label(frame_entrada, text="Hora:").grid(row=1, column=0)
entry_hora = tk.Entry(frame_entrada)
entry_hora.grid(row=1, column=1, padx=5)

tk.Label(frame_entrada, text="Descripción:").grid(row=2, column=0)
entry_descripcion = tk.Entry(frame_entrada)
entry_descripcion.grid(row=2, column=1, padx=5)

# Frame para botones
frame_botones = tk.Frame(root)
frame_botones.pack(pady=10)

tk.Button(frame_botones, text="Agregar Evento", command=agregar_evento).grid(row=0, column=0, padx=5)
tk.Button(frame_botones, text="Eliminar Evento", command=eliminar_evento).grid(row=0, column=1, padx=5)
tk.Button(frame_botones, text="Salir", command=root.quit).grid(row=0, column=2, padx=5)

root.mainloop()

git