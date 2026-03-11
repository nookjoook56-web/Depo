import requests
import json

def run():
    headers = {"User-Agent": "VAVOO/2.6"}
    print("İmza isteniyor...")
    
    try:
        # 1. İmzayı Al
        config_res = requests.get("https://vavoo.to/config", headers=headers, timeout=15)
        signature = config_res.json().get("signature")
        
        if not signature:
            print("HATA: İmza alınamadı!")
            return

        print(f"İmza Alındı: {signature[:10]}...")

        # 2. Kanalları Al
        channels_res = requests.get(f"https://vavoo.to/channels?vexe=1&sig={signature}", headers=headers, timeout=15)
        channels = channels_res.json()

        # 3. M3U Dosyasını Oluştur
        with open("playlist.m3u", "w", encoding="utf-8") as f:
            f.write("#EXTM3U\n")
            counter = 0
            for ch in channels:
                name = ch.get("name", "Bilinmiyor")
                # Filtreleme: beIN, Spor ve Türkiye kanalları
                if any(x in name.upper() for x in ["BEIN", "SPOR", "SPORT", "TURK"]):
                    url = ch.get("url")
                    f.write(f'#EXTINF:-1 tvg-name="{name}" group-title="Canli TV", {name}\n')
                    f.write(f"{url}?sig={signature}\n")
                    counter += 1
            
        # 4. İmza dosyasını da yaz
        with open("signature.txt", "w") as f:
            f.write(signature)
            
        print(f"İşlem tamam! {counter} kanal listeye eklendi.")

    except Exception as e:
        print(f"Sistem Hatası: {e}")

if __name__ == "__main__":
    run()
    
