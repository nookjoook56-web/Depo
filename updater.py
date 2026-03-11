import requests

def get_vavoo_signature():
    url = "https://vavoo.to/config"
    headers = {"User-Agent": "VAVOO/2.6"}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json().get("signature")
    except:
        return None
    return None

sig = get_vavoo_signature()
if sig:
    with open("signature.txt", "w") as f:
        f.write(sig)
    print("İmza başarıyla signature.txt dosyasına yazıldı.")
    
