import requests
import time
from datetime import datetime

urls = [
    "https://pageindexrepo-pjcqzhtmkf9sh9siumr5j9.streamlit.app/"
]

def check_url(url):
    try:
        r = requests.get(url, timeout=10)
        status = r.status_code

        if status == 200:
            print(f"[{datetime.now()}] ✅ ACTIVE - {url} - Status {status}")
            return True
        else:
            print(f"[{datetime.now()}] ⚠️ WARNING - {url} - Status {status}")
            return False

    except requests.exceptions.Timeout:
        print(f"[{datetime.now()}] ⏳ TIMEOUT - {url} - Page may be frozen")
    except requests.exceptions.ConnectionError:
        print(f"[{datetime.now()}] ❌ CONNECTION ERROR - {url} - Page is unreachable")
    except requests.exceptions.RequestException as e:
        print(f"[{datetime.now()}] ❌ ERROR - {url} - {e}")

    return False

# Seguir probando hasta que todos estén activos
while urls:
    for url in urls[:]:  # recorremos una copia de la lista
        if check_url(url):
            urls.remove(url)  # si está activo lo sacamos de la lista

    if urls:  # si todavía quedan pendientes
        time.sleep(5)  # esperar 5 minutos
    else:
        print(f"[{datetime.now()}] 🎉 Todos los links están activos")
