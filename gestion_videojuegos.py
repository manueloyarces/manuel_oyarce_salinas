import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Función para extraer el ID del videojuego seleccionado en la lista
def extraer_id(cadena):
    partes = cadena.split(',')
    for parte in partes:
        if "ID" in parte:
            return int(parte.split(':')[1].strip())

class VideojuegosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Videojuegos")

        # Configuración de conexión a la base de datos
        self.db_config = {
            'user': 'root',
            'password': '1234',
            'host': 'localhost',
            'database': 'videojuegos_db'
        }

        self.conn = mysql.connector.connect(**self.db_config)
        self.cursor = self.conn.cursor()

        # Widgets
        self.label_id = tk.Label(root, text="ID:")
        self.entry_id = tk.Entry(root)

        self.label_titulo = tk.Label(root, text="Título:")
        self.entry_titulo = tk.Entry(root)

        self.label_genero = tk.Label(root, text="Género:")
        self.entry_genero = tk.Entry(root)

        self.label_clasificacion = tk.Label(root, text="Clasificación:")
        self.entry_clasificacion = tk.Entry(root)

        self.label_plataforma = tk.Label(root, text="Plataforma:")
        self.entry_plataforma = tk.Entry(root)

        self.listbox = tk.Listbox(root, width=100)
        self.listbox.bind('<<ListboxSelect>>', self.cargar_datos)

        self.btn_agregar = tk.Button(root, text="Agregar", command=self.agregar)
        self.btn_mostrar = tk.Button(root, text="Mostrar", command=self.mostrar)

        # Posiciones
        self.label_id.grid(row=0, column=0)
        self.entry_id.grid(row=0, column=1)
        self.label_titulo.grid(row=1, column=0)
        self.entry_titulo.grid(row=1, column=1)
        self.label_genero.grid(row=2, column=0)
        self.entry_genero.grid(row=2, column=1)
        self.label_clasificacion.grid(row=3, column=0)
        self.entry_clasificacion.grid(row=3, column=1)
        self.label_plataforma.grid(row=4, column=0)
        self.entry_plataforma.grid(row=4, column=1)

        self.listbox.grid(row=5, column=0, columnspan=2, pady=10)
        self.btn_agregar.grid(row=6, column=0)
        self.btn_mostrar.grid(row=6, column=1)

    def agregar(self):
        try:
            datos = (
                int(self.entry_id.get()),
                self.entry_titulo.get(),
                self.entry_genero.get(),
                self.entry_clasificacion.get(),
                self.entry_plataforma.get()
            )
            self.cursor.execute("INSERT INTO Videojuegos (ID, Titulo, Genero, Clasificacion, Plataforma) VALUES (%s, %s, %s, %s, %s)", datos)
            self.conn.commit()
            messagebox.showinfo("Éxito", "Videojuego agregado")
            self.mostrar()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def mostrar(self):
        try:
            self.listbox.delete(0, tk.END)
            self.cursor.execute("SELECT * FROM Videojuegos")
            for fila in self.cursor.fetchall():
                self.listbox.insert(tk.END, f"ID: {fila[0]}, Título: {fila[1]}, Género: {fila[2]}, Clasificación: {fila[3]}, Plataforma: {fila[4]}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def cargar_datos(self, event):
        seleccion = self.listbox.curselection()
        if seleccion:
            datos = self.listbox.get(seleccion[0])
            id_sel = extraer_id(datos)
            self.cursor.execute("SELECT * FROM Videojuegos WHERE ID = %s", (id_sel,))
            fila = self.cursor.fetchone()
            if fila:
                self.entry_id.delete(0, tk.END)
                self.entry_id.insert(0, fila[0])
                self.entry_titulo.delete(0, tk.END)
                self.entry_titulo.insert(0, fila[1])
                self.entry_genero.delete(0, tk.END)
                self.entry_genero.insert(0, fila[2])
                self.entry_clasificacion.delete(0, tk.END)
                self.entry_clasificacion.insert(0, fila[3])
                self.entry_plataforma.delete(0, tk.END)
                self.entry_plataforma.insert(0, fila[4])

if __name__ == "__main__":
    root = tk.Tk()
    app = VideojuegosApp(root)
    root.mainloop()
