import requests
import os

def get_vavoo_signature():
    url = "https://vavoo.to/config"
    headers = {"User-Agent": "VAVOO/2.6"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        # Vavoo'nun o anki aktif anahtarını/imzasını ayıkla
        config_data = response.json()
        signature = config_data.get("signature")
        return signature
    return None

# Aldığımız imzayı bir dosyaya yazıyoruz (veya FastAPI sunucuna yolluyoruz)
sig = get_vavoo_signature()
if sig:
    print(f"Yeni İmza Alındı: {sig}")
    # Burada imzayı GitHub repona push edebilir veya bir database'e yazabilirsin
  
