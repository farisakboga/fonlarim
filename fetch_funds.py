import requests
import json
import time

fonlar = ["AZH", "ALI", "AMF", "YHK", "PHE", "ALZ", "AZK", "AZL", "HSR", "YZD"]

def tefas_verisi_al(fon_kodu):
    url = "https://www.tefas.gov.tr/api/funds/fonBilgiGetir"
    payload = {"fonKodu": fon_kodu.upper()}
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Referer": "https://www.tefas.gov.tr/",
        "Origin": "https://www.tefas.gov.tr"
    }
    try:
        response = requests.post(url, json=payload, headers=headers, timeout=15)
        
        # ← YENİ: Ham yanıtı logla
        print(f"  Status: {response.status_code}")
        print(f"  Response: {response.text[:200]}")
        
        response.raise_for_status()
        data = response.json()

        if data.get("resultList") and len(data["resultList"]) > 0:
            fund_info = data["resultList"][0]
            fiyat = fund_info.get("sonFiyat", 0)
            degisim = fund_info.get("gunlukGetiri", 0)
            return {
                "FON ADI": fon_kodu,
                "FİYAT": str(fiyat).replace('.', ','),
                "DEĞİŞİM": str(degisim).replace('.', ',')
            }
        else:
            print(f"  UYARI: {fon_kodu} için resultList boş!")
            return None

    except Exception as e:
        print(f"  HATA ({fon_kodu}): {e}")
        return None

def main():
    data_list = []

    for kod in fonlar:
        print(f"\n{kod} verisi çekiliyor...")
        veriseti = tefas_verisi_al(kod)
        if veriseti:
            data_list.append(veriseti)
        time.sleep(1)

    # ← YENİ: Boşsa eski dosyayı koru, üzerine yazma
    if not data_list:
        print("\nHIÇ VERİ ÇEKILEMEDI! funds.json güncellenmedi.")
        exit(1)  # ← Actions'da commit atmayı engeller

    with open('funds.json', 'w', encoding='utf-8') as f:
        json.dump(data_list, f, ensure_ascii=False, indent=4)

    print(f"\n✅ {len(data_list)} fon kaydedildi.")

if __name__ == "__main__":
    main()
