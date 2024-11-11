import pyautogui
import time
import webbrowser
import sys

def iniciar_whatsapp_web():
    """
    Abre WhatsApp Web en el navegador predeterminado y espera al usuario.
    """
    print("Abriendo WhatsApp Web...")
    webbrowser.open("https://web.whatsapp.com")
    input("Escanea el código QR y selecciona el chat al que quieres enviar mensajes. Luego, presiona Enter para continuar...")

def enviar_mensajes(mensaje, repeticiones, intervalo):
    """
    Envía mensajes usando pyautogui para emular el teclado.
    """
    try:
        for i in range(repeticiones):
            pyautogui.typewrite(mensaje)
            pyautogui.press("enter")
            print(f"[{i + 1}/{repeticiones}] Mensaje enviado")
            time.sleep(intervalo)
        print("✅ Envío completado.")
    except KeyboardInterrupt:
        print("\n⛔ Interrumpido por el usuario.")
        sys.exit()
    except Exception as e:
        print(f"⚠️ Error al enviar mensajes: {e}")
        sys.exit()

def obtener_entrada_usuario():
    """
    Solicita al usuario que ingrese el mensaje, número de repeticiones y el intervalo.
    """
    mensaje = input("Introduce el mensaje que deseas enviar: ")
    
    while True:
        try:
            repeticiones = int(input("Introduce el número de veces que se enviará el mensaje: "))
            intervalo = float(input("Introduce el intervalo (en segundos) entre cada mensaje: "))
            break
        except ValueError:
            print("⚠️ Error: Por favor, ingresa valores numéricos válidos.")
    
    return mensaje, repeticiones, intervalo

if __name__ == "__main__":
    print("=== WhatsApp Message Automation Script ===")
    mensaje, repeticiones, intervalo = obtener_entrada_usuario()
    
    iniciar_whatsapp_web()
    print("Preparando para enviar mensajes...")
    time.sleep(5)
    enviar_mensajes(mensaje, repeticiones, intervalo)
