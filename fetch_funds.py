import requests
import json
import time

# Çekmek istediğiniz fonların listesi
fonlar = ["AZH", "ALI", "AMF", "YHK", "PHE", "ALZ", "AZK", "AZL", "HSR", "YZD", "AMZ"]

def tefas_verisi_al(fon_kodu, deneme=3):
    """TEFAS API'sinden veri çeker, hata durumunda tekrar dener."""
    url = "https://www.tefas.gov.tr/api/funds/fonBilgiGetir"
    payload = {"fonKodu": fon_kodu.upper()}
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Referer": "https://www.tefas.gov.tr/",
        "Origin": "https://www.tefas.gov.tr"
    }

    for i in range(deneme):
        try:
            response = requests.post(url, json=payload, headers=headers, timeout=15)
            print(f"  Status: {response.status_code}")
            response.raise_for_status()
            data = response.json()

            if data.get("resultList") and len(data["resultList"]) > 0:
                fund_info = data["resultList"][0]
                return {
                    "FON ADI": fon_kodu,
                    "FİYAT": str(fund_info.get("sonFiyat", 0)).replace('.', ','),
                    "DEĞİŞİM": str(fund_info.get("gunlukGetiri", 0)).replace('.', ',')
                }
        except Exception as e:
            print(f"  Deneme {i+1}/{deneme} başarısız ({fon_kodu}): {e}")
            time.sleep(3)  # ← tekrar denemeden önce bekle

    return None

def main():
    data_list = []
    print(f"--- İşlem Başladı: {time.strftime('%Y-%m-%d %H:%M:%S')} ---")
    
    for kod in fonlar:
        print(f"{kod} çekiliyor...")
        veriseti = tefas_verisi_al(kod)
        if veriseti:
            data_list.append(veriseti)
        time.sleep(1) # TEFAS'ı yormamak için her fon arası 1 sn bekle

    with open('funds.json', 'w', encoding='utf-8') as f:
        json.dump(data_list, f, ensure_ascii=False, indent=4)
    
    print(f"--- İşlem Tamamlandı. Toplam {len(data_list)} fon çekildi. ---")

if __name__ == "__main__":
    main()
