import requests

def run():
    headers = {"User-Agent": "VAVOO/2.6"}
    
    # 1. İmza Al
    try:
        config = requests.get("https://vavoo.to/config", headers=headers, timeout=10).json()
        signature = config.get("signature")
        if not signature: return
    except: return

    # 2. Kanalları Al (Almanya/Türkiye karışık liste genelde buradadır)
    try:
        # Not: Bu URL Vavoo'nun güncel kanal listesi endpoint'idir
        channels = requests.get(f"https://vavoo.to/channels?vexe=1&sig={signature}", headers=headers).json()
    except: return

    # 3. M3U Oluştur
    with open("playlist.m3u", "w", encoding="utf-8") as f:
        f.write("#EXTM3U\n")
        for ch in channels:
            name = ch.get("name", "Unknown")
            # Sadece SPOR ve BEIN kanallarını filtrele
            if any(x in name.upper() for x in ["BEIN", "SPOR", "SPORT"]):
                url = ch.get("url")
                f.write(f'#EXTINF:-1 tvg-name="{name}" group-title="Spor", {name}\n')
                f.write(f"{url}?sig={signature}\n")
    
    # İmza dosyasını da yedekle
    with open("signature.txt", "w") as f:
        f.write(signature)

if __name__ == "__main__":
    run()
    
