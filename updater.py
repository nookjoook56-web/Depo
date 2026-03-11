import requests

def run():
    headers = {"User-Agent": "VAVOO/2.6"}
    print("İmza alınıyor...")
    try:
        config = requests.get("https://vavoo.to/config", headers=headers, timeout=15).json()
        signature = config.get("signature")
        if not signature:
            print("HATA: İmza bulunamadı!")
            return
    except Exception as e:
        print(f"HATA (Config): {e}")
        return

    print(f"İmza başarılı: {signature[:10]}...")
    print("Kanallar çekiliyor...")
    
    try:
        # Türkiye kanalları için genellikle bu liste kullanılır
        channels = requests.get(f"https://vavoo.to/channels?vexe=1&sig={signature}", headers=headers, timeout=15).json()
        
        with open("playlist.m3u", "w", encoding="utf-8") as f:
            f.write("#EXTM3U\n")
            count = 0
            for ch in channels:
                name = ch.get("name", "Unknown")
                if any(x in name.upper() for x in ["BEIN", "SPOR", "SPORT", "TURK"]):
                    url = ch.get("url")
                    f.write(f'#EXTINF:-1 tvg-name="{name}" group-title="Spor", {name}\n')
                    f.write(f"{url}?sig={signature}\n")
                    count += 1
            print(f"Bitti! {count} kanal eklendi.")
            
        with open("signature.txt", "w") as f:
            f.write(signature)
            
    except Exception as e:
        print(f"HATA (Channels): {e}")

if __name__ == "__main__":
    run()
    
