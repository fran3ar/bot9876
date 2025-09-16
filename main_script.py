import requests
import time
from datetime import datetime

url = "https://pageindexrepo-pjcqzhtmkf9sh9siumr5j9.streamlit.app/"  # replace with your URL

def check_url():
    try:
        r = requests.get(url, timeout=10)  # wait max 10s
        status = r.status_code

        if status == 200:
            print(f"[{datetime.now()}] ✅ ACTIVE - Status {status}")
            return True
        else:
            print(f"[{datetime.now()}] ⚠️ WARNING - Status {status}")
            return False

    except requests.exceptions.Timeout:
        print(f"[{datetime.now()}] ⏳ TIMEOUT - Page may be frozen")
    except requests.exceptions.ConnectionError:
        print(f"[{datetime.now()}] ❌ CONNECTION ERROR - Page is unreachable")
    except requests.exceptions.RequestException as e:
        print(f"[{datetime.now()}] ❌ ERROR - {e}")

    return False

# Keep checking until active
while True:
    if check_url():
        break  # stop when active
    time.sleep(5)  # check every 5 minutes
