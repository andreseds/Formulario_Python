# Importar los módulos necesarios
import tkinter as tk
import re
import smtplib

# Crear la ventana principal
window = tk.Tk()
window.title("Formulario de contacto")

# Crear las etiquetas para solicitar los datos
label_name = tk.Label(window, text="Nombre completo:")
label_email = tk.Label(window, text="Correo:")
label_message = tk.Label(window, text="Mensaje:")
label_status = tk.Label(window, text="")

# Crear las entradas de texto para ingresar los datos
entry_name = tk.Entry(window)
entry_email = tk.Entry(window)
entry_message = tk.Text(window, height=10, width=40)

# Crear el botón para enviar el formulario
button_send = tk.Button(window, text="Enviar")

# Posicionar los elementos en la ventana usando grid
label_name.grid(row=0, column=0, sticky="e")
label_email.grid(row=1, column=0, sticky="e")
label_message.grid(row=2, column=0, sticky="e")
label_status.grid(row=4, column=0, columnspan=2)
entry_name.grid(row=0, column=1)
entry_email.grid(row=1, column=1)
entry_message.grid(row=2, column=1)
button_send.grid(row=3, column=0, columnspan=2)

# Definir la función para validar el formato del correo
def validate_email(event):
    # Obtener el correo ingresado por el usuario
    email = entry_email.get()
    # Definir la expresión regular para validar el formato del correo
    regex = "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    # Verificar si el correo cumple con la expresión regular
    if re.match(regex, email):
        # Si es válido, borrar el mensaje de error si existe
        label_status.config(text="")
    else:
        # Si no es válido, mostrar un mensaje de error
        label_status.config(text="Correo inválido", fg="red")

# Definir la función para enviar el correo
def send_email(event):
    # Obtener los datos ingresados por el usuario
    name = entry_name.get()
    email = entry_email.get()
    message = entry_message.get("1.0", "end")
    # Definir los datos del remitente y del destinatario
    sender = "mi_correo@gmail.com"
    password = "mi_contraseña"
    receiver = "mi_correo@gmail.com"
    subject = f"Formulario de contacto de {name}"
    body = f"Nombre: {name}\nCorreo: {email}\nMensaje: {message}"
    # Crear el mensaje completo
    msg = f"Subject: {subject}\n\n{body}"
    # Intentar enviar el correo usando smtplib
    try:
        # Crear una instancia de SMTP y establecer una conexión segura con el servidor
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        # Iniciar sesión con el remitente y enviar el mensaje al destinatario
        server.login(sender, password)
        server.sendmail(sender, receiver, msg)
        # Cerrar la conexión con el servidor
        server.quit()
        # Mostrar un mensaje de éxito en la etiqueta de estado
        label_status.config(text="Correo enviado con éxito", fg="green")
    except:
        # Mostrar un mensaje de fracaso en la etiqueta de estado
        label_status.config(text="Error al enviar el correo", fg="red")

# Asignar las funciones de validación y envío al botón de enviar usando el método bind
button_send.bind("<Button-1>", validate_email)
button_send.bind("<ButtonRelease-1>", send_email)

# Ejecutar la ventana principal usando el método mainloop
window.mainloop()