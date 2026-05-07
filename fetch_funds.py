import requests
import json
import time

# Çekmek istediğiniz fonların listesi
fonlar = ["AZH", "ALI", "AMF", "YHK", "PHE", "ALZ", "AZK", "AZL", "HSR", "YZD"]

def tefas_verisi_al(fon_kodu, deneme_sayisi=3):
    """TEFAS API'sinden veri çeker, hata durumunda yeniden dener."""
    url = "https://www.tefas.gov.tr/api/funds/fonBilgiGetir"
    payload = {"fonKodu": fon_kodu.upper()}
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }

    for i in range(deneme_sayisi):
        try:
            # timeout=30 yaparak sunucuya daha fazla zaman tanıdık
            response = requests.post(url, json=payload, headers=headers, timeout=30)
            response.raise_for_status()
            data = response.json()
            
            if data.get("resultList") and len(data["resultList"]) > 0:
                f = data["resultList"][0]
                
                def format_tr(val):
                    return str(val).replace('.', ',')

                buyukluk_milyon = round(f.get("portBuyukluk", 0) / 1_000_000, 2)

                return {
                    "KOD": fon_kodu,
                    "AD": f.get("fonUnvan", ""),
                    "KATEGORİ": f.get("fonKategori", ""),
                    "FİYAT": format_tr(f.get("sonFiyat", 0)),
                    "DEĞİŞİM": format_tr(f.get("gunlukGetiri", 0)),
                    "YATIRIMCI": f"{f.get('yatirimciSayi', 0):,}".replace(',', '.'),
                    "BÜYÜKLÜK_MİLYON_TL": format_tr(buyukluk_milyon),
                    "SIRALAMA": f"{f.get('kategoriDerece', 0)} / {f.get('kategoriFonSay', 0)}",
                    "TARİH": f.get("tarih", "")
                }
        except Exception as e:
            if i < deneme_sayisi - 1:
                print(f"Uyarı: {fon_kodu} için {i+1}. deneme başarısız, tekrar deneniyor... ({e})")
                time.sleep(2) # 2 saniye bekle ve tekrar dene
            else:
                print(f"Hata: {fon_kodu} 3 denemeye rağmen çekilemedi: {e}")
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
