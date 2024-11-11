import pyautogui
import time
import webbrowser

def iniciar_whatsapp_web():
    """
    Abre WhatsApp Web en el navegador predeterminado.
    """
    webbrowser.open("https://web.whatsapp.com")
    input("Escanea el código QR y presiona Enter una vez que hayas iniciado sesión y seleccionado el chat...")

def enviar_mensajes(mensaje, repeticiones, intervalo):
    """
    Envía mensajes usando pyautogui para emular el teclado.
    """
    for i in range(repeticiones):
        # Escribir el mensaje en el chat abierto
        pyautogui.typewrite(mensaje)
        pyautogui.press("enter")
        print(f"Mensaje {i + 1} enviado")
        time.sleep(intervalo)

if __name__ == "__main__":
    mensaje = "FUISTE CAGONN"
    repeticiones = 10000  # Número de veces que se enviará el mensaje
    intervalo = 1  # Intervalo en segundos entre cada mensaje

    iniciar_whatsapp_web()
    time.sleep(5)  
    enviar_mensajes(mensaje, repeticiones, intervalo)
