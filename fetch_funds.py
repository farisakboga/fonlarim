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
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        if data.get("resultList") and len(data["resultList"]) > 0:
            f = data["resultList"][0]
            
            # Sayısal verileri formatlama fonksiyonu
            def format_tr(val):
                return str(val).replace('.', ',')

            # Fon büyüklüğünü Milyon TL cinsinden göstermek daha okunurdur
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
                "PAZAR_PAYI": format_tr(f.get("pazarPayi", 0)),
                "TARİH": f.get("tarih", "")
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
        time.sleep(0.3)

    with open('funds.json', 'w', encoding='utf-8') as f:
        json.dump(data_list, f, ensure_ascii=False, indent=4)
    print("\nİşlem tamamlandı.")

if __name__ == "__main__":
    main()
```

### Bu Bilgiler Web Sayfasında (index.html) Nasıl Görünür?

Eğer bu verileri web sitenizde yayınlayacaksanız, `index.html` dosyanızdaki JavaScript kısmını da bu yeni anahtar kelimelere göre güncellemeniz gerekir.

**Örnek JavaScript değişikliği:**
```javascript
data.forEach(item => {
    const row = `<tr>
        <td><b>${item['KOD']}</b></td>
        <td><small>${item['AD']}</small></td>
        <td>${item['FİYAT']}</td>
        <td class="plus">%${item['DEĞİŞİM']}</td>
        <td>${item['YATIRIMCI']}</td>
        <td>${item['SIRALAMA']}</td>
    </tr>`;
    tbody.innerHTML += row;
});
