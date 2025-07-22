import requests
from datetime import datetime
import pytz  # ← NUEVO

def send_telegram_message(token, chat_id, text):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    response = requests.post(url, data=payload)
    return response.json()

# Token y chat ID (reemplazá este número con el tuyo real)
BOT_TOKEN = "7493072528:AAGxcMz9jnItEDi01qMogvyMyxac3jjnSFw"
CHAT_ID = 7827259260  # Reemplaza con tu chat ID real (número entero)

# Definir zona horaria de Argentina
arg_tz = pytz.timezone('America/Argentina/Buenos_Aires')

# Obtener hora actual en Argentina
hora_actual = datetime.now(arg_tz).strftime("%Y-%m-%d %H:%M:%S")

# Armar mensaje
mensaje = f"🕒 Notificación automática:\nHora Argentina: {hora_actual}"

# Enviar
send_telegram_message(BOT_TOKEN, CHAT_ID, mensaje)
