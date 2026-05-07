import requests
import json
import time

# Çekmek istediğiniz fonların listesi
fonlar = ["AZH", "ALI", "AMF", "YHK", "PHE", "ALZ", "AZK", "AZL", "HSR", "YZD"]

def tefas_verisi_al(fon_kodu):
    """TEFAS API'sinden doğrudan veri çeker."""
    url = "https://www.tefas.gov.tr/api/funds/fonBilgiGetir"
    
    # API'nin beklediği JSON taslağı
    payload = {"fonKodu": fon_kodu.upper()}
    
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    try:
        # POST isteği gönderiyoruz
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        response.raise_for_status() # Hata varsa fırlat
        
        data = response.json()
        
        # TEFAS API yapısı: {"resultList": [...], "errorCode": 0...}
        if data.get("resultList") and len(data["resultList"]) > 0:
            fund_info = data["resultList"][0]
            
            # Verileri çekip formatlıyoruz
            fiyat = fund_info.get("sonFiyat", 0)
            degisim = fund_info.get("gunlukGetiri", 0)
            
            return {
                "FON ADI": fon_kodu,
                "FİYAT": str(fiyat).replace('.', ','),
                "DEĞİŞİM": str(degisim).replace('.', ',')
            }
    except Exception as e:
        print(f"Hata ({fon_kodu}): {e}")
        return None

def main():
    data_list = []
    
    for kod in fonlar:
        print(f"{kod} verisi çekiliyor...")
        veriseti = tefas_verisi_al(kod)
        
        if veriseti:
            data_list.append(veriseti)
        
        # API'yi yormamak için kısa bir bekleme (opsiyonel)
        time.sleep(0.5)

    # JSON dosyasına yaz
    with open('funds.json', 'w', encoding='utf-8') as f:
        json.dump(data_list, f, ensure_ascii=False, indent=4)
    
    print("\nİşlem tamamlandı. funds.json dosyası güncellendi.")

if __name__ == "__main__":
    main()