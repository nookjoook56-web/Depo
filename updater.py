import requests
import json

def get_vavoo_data():
    headers = {"User-Agent": "VAVOO/2.6"}
    # 1. Güncel İmzayı Al
    config = requests.get("https://vavoo.to/config", headers=headers).json()
    signature = config.get("signature")
    
    # 2. Kanal Listesini Al (Örnek olarak Almanya/Türkiye listesi)
    # Not: Vavoo API yapısına göre URL değişkenlik gösterebilir
    channels_url = f"https://vavoo.to/channels?vexe=1&sig={signature}"
    channels = requests.get(channels_url, headers=headers).json()
    
    return signature, channels

def create_m3u(signature, channels):
    with open("playlist.m3u", "w", encoding="utf-8") as f:
        f.write("#EXTM3U\n")
        
        for ch in channels:
            name = ch.get("name", "Unknown")
            # beIN Sports veya istediğin anahtar kelimeleri filtrele
            if "BEIN" in name.upper() or "SPOR" in name.upper():
                url = ch.get("url")
                # Vavoo link yapısı: url + ?sig=...
                final_url = f"{url}?sig={signature}"
                
                f.write(f'#EXTINF:-1 tvg-name="{name}" group-title="Spor", {name}\n')
                f.write(f"{final_url}\n")

# Çalıştır
try:
    sig, chans = get_vavoo_data()
    create_m3u(sig, chans)
    with open("signature.txt", "w") as f: f.write(sig)
    print("Playlist ve İmza başarıyla güncellendi!")
except Exception as e:
    print(f"Hata: {e}")
    
