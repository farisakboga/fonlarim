import requests
import json
import time

fonlar = ["AAL", "AAS", "AAV", "AC1", "AC4", "AC5", "AC6", "ACC", "ACD", "ACU", "ADE", "ADP", "AED", "AES", "AEV", "AFA", "AFO", "AFS", "AFT", "AFV", "AGC", "AHI", "AHN", "AHU", "AHV", "AIS", "AJ1", "AJK", "AK2", "AK3", "AKE", "AKU", "ALC", "AN1", "ANZ", "AOJ", "AOY", "AP5", "AP7", "APJ", "APT", "ARE", "ARL", "ARM", "AS1", "ASJ", "AU1", "AUV", "AYA", "AYR", "BAG", "BBF", "BBP", "BBS", "BCK", "BCO", "BDA", "BDC", "BDS", "BDY", "BFE", "BFS", "BFT", "BGP", "BHA", "BHF", "BHI", "BHL", "BID", "BIG", "BIH", "BIO", "BIP", "BIS", "BIY", "BJD", "BKY", "BLD", "BLT", "BMU", "BNC", "BNH", "BOL", "BON", "BOS", "BPZ", "BRC", "BRF", "BRR", "BRT", "BS1", "BSD", "BSH", "BSM", "BST", "BTE", "BTJ", "BTK", "BTZ", "BUB", "BUV", "BUY", "BV1", "BVD", "BVF", "BVK", "BVM", "BVV", "BVZ", "CAH", "CFO", "CIN", "CKF", "CKL", "CKS", "CPT", "CPU", "CVK", "CVL", "DA1", "DAH", "DAS", "DBA", "DBB", "DBH", "DBK", "DBP", "DBZ", "DCB", "DDA", "DDF", "DEF", "DFC", "DFD", "DFI", "DGF", "DGH", "DHJ", "DHM", "DHT", "DID", "DIP", "DKH", "DKL", "DKR", "DL2", "DLD", "DLY", "DMG", "DNF", "DNH", "DNK", "DNM", "DNP", "DOH", "DOL", "DOV", "DPB", "DPI", "DPK", "DPT", "DRA", "DRT", "DSD", "DSP", "DTH", "DTL", "DTM", "DTZ", "DUD", "DUH", "DUV", "DVS", "DVT", "DXP", "DYN", "DZE", "DZM", "EBD", "EBI", "EBS", "EC2", "ECA", "EDP", "EDT", "EDU", "EIB", "EID", "EIL", "EKF", "ELZ", "EML", "ENJ", "EPA", "EPI", "EPK", "EPP", "EPT", "ESG", "ESP", "EUN", "EUZ", "EVM", "EYT", "FAK", "FAL", "FBC", "FBI", "FBV", "FBZ", "FCK", "FD1", "FDG", "FDV", "FFH", "FFP", "FI3", "FIB", "FID", "FIL", "FIT", "FJB", "FJZ", "FKE", "FLS", "FLY", "FMG", "FMV", "FNO", "FNT", "FP4", "FPE", "FPG", "FPH", "FPI", "FPK", "FPZ", "FRC", "FS5", "FS6", "FSF", "FSG", "FSH", "FSK", "FSP", "FSR", "FSU", "FTL", "FUA", "FUB", "FYD", "FYI", "FYO", "FZJ", "FZP", "GA1", "GAE", "GAF", "GAG", "GAH", "GAS", "GBC", "GBG", "GBH", "GBJ", "GBL", "GBN", "GBV", "GBZ", "GGK", "GHS", "GID", "GIE", "GIH", "GJB", "GKF", "GKG", "GKH", "GKV", "GL1", "GLC", "GLG", "GLS", "GMA", "GMC", "GMD", "GMI", "GMN", "GMR", "GNH", "GNS", "GO1", "GO2", "GO3", "GO4", "GO6", "GO9", "GOH", "GOL", "GOP", "GPA", "GPB", "GPC", "GPF", "GPG", "GPI", "GPL", "GPN", "GPT", "GPU", "GPZ", "GRL", "GRO", "GRT", "GSP", "GTA", "GTF", "GTH", "GTM", "GTY", "GTZ", "GUB", "GUH", "GUK", "GUM", "GUV", "GVA", "GVI", "GYK", "GZE", "GZG", "GZH", "GZJ", "GZL", "GZM", "GZN", "GZP", "GZR", "GZV", "GZY", "GZZ", "HAM", "HAR", "HAT", "HBF", "HBN", "HBU", "HCV", "HDA", "HDK", "HEH", "HFI", "HFR", "HGM", "HGR", "HGV", "HIA", "HIF", "HIH", "HIM", "HIZ", "HJB", "HKG", "HKH", "HKJ", "HKM", "HKR", "HMC", "HMG", "HML", "HMS", "HNC", "HOA", "HOY", "HP3", "HPD", "HPH", "HPO", "HPT", "HRZ", "HSA", "HSL", "HST", "HTF", "HTJ", "HTS", "HVI", "HVK", "HVS", "HVT", "HVU", "HVZ", "HYP", "HYU", "HYV", "IAE", "IAM", "IAR", "IAT", "IAU", "IAY", "IBB", "ICA", "ICC", "ICD", "ICE", "ICF", "ICH", "ICS", "ICV", "ICZ", "IDD", "IDF", "IDH", "IDI", "IDL", "IDO", "IDY", "IED", "IEN", "IEV", "IFN", "IFV", "IHA", "IHC", "IHK", "IHP", "IHT", "IHV", "IHZ", "IIE", "IIH", "IIN", "IJA", "IJB", "IJC", "IJH", "IJP", "IJT", "IJV", "IJZ", "IKL", "IKP", "IKV", "ILU", "ILZ", "IMB", "IMF", "IML", "IOG", "IOO", "IPB", "IPG", "IPJ", "IPV", "IRB", "IRF", "IRO", "IRT", "IRV", "IRY", "IST", "ITC", "ITP", "IUF", "IUH", "IUV", "IV8", "IVF", "IVY", "IYB", "IZB", "IZS", "JET", "JUP", "KAV", "KCL", "KCV", "KDE", "KDL", "KDO", "KDT", "KGM", "KH1", "KHA", "KHB", "KHC", "KHJ", "KHT", "KIA", "KIB", "KID", "KIE", "KIF", "KIH", "KIK", "KIS", "KKC", "KKH", "KKL", "KLH", "KLI", "KLS", "KLU", "KME", "KMF", "KMN", "KNI", "KNJ", "KOD", "KOT", "KP3", "KPA", "KPC", "KPD", "KPF", "KPH", "KPI", "KPP", "KPU", "KRA", "KRC", "KRF", "KRR", "KRS", "KRT", "KSA", "KSK", "KSR", "KST", "KSV", "KTI", "KTJ", "KTM", "KTN", "KTR", "KTS", "KTT", "KTV", "KU3", "KUA", "KUB", "KUD", "KUT", "KVK", "KVR", "KVS", "KVT", "KYA", "KYS", "KZL", "KZU", "LKT", "LLA", "LPH", "MAC", "MAD", "MBL", "MBR", "MCU", "MD1", "MD2", "MDF", "MET", "MGB", "MGH", "MHF", "MJB", "MJG", "MJH", "MJL", "MKA", "MKG", "MLT", "MMH", "MOZ", "MPE", "MPF", "MPI", "MPK", "MPL", "MPN", "MPP", "MPS", "MRI", "MT1", "MT2", "MTD", "MTF", "MTG", "MTH", "MTK", "MTS", "MTV", "MTX", "MUT", "NAK", "NAU", "NBH", "NBO", "NBZ", "NCS", "NFF", "NHP", "NHY", "NJF", "NJR", "NJY", "NKA", "NKC", "NKM", "NKP", "NKT", "NLE", "NLK", "NME", "NMU", "NNF", "NOI", "NPH", "NRC", "NRG", "NSA", "NSD", "NSH", "NSK", "NSP", "NST", "NSY", "NTI", "NUB", "NUH", "NVB", "NVC", "NVK", "NVT", "NVZ", "NZH", "NZT", "NZU", "OBI", "OBP", "ODD", "ODG", "ODP", "ODS", "ODV", "OFI", "OFS", "OGD", "OHB", "OHK", "OIL", "OIR", "OJB", "OJK", "OJT", "OKD", "OKP", "OKT", "OLA", "OLD", "OLE", "OMG", "ONE", "ONK", "ONN", "ONS", "OPB", "OPD", "OPF", "OPH", "OPI", "OPL", "ORC", "OSD", "OSL", "OTJ", "OTK", "OTM", "OUD", "OVD", "P1A", "PAB", "PAF", "PAL", "PAO", "PBI", "PBK", "PBN", "PBR", "PCE", "PDD", "PDF", "PEA", "PFO", "PFS", "PGD", "PGS", "PHE", "PHI", "PHK", "PID", "PIL", "PIP", "PIR", "PIS", "PJL", "PJP", "PKD", "PKF", "PKP", "PKR", "PKT", "PKV", "PLR", "PMP", "PNU", "PO9", "POS", "PP1", "PPB", "PPE", "PPG", "PPH", "PPI", "PPJ", "PPK", "PPM", "PPN", "PPP", "PPS", "PPT", "PPV", "PPZ", "PRD", "PRH", "PRR", "PRU", "PRV", "PRY", "PSE", "PSH", "PSL", "PTE", "PTF", "PTN", "PTO", "PTP", "PTS", "PUC", "PUK", "PVK", "PYR", "RAF", "RBA", "RBB", "RBF", "RBH", "RBI", "RBK", "RBL", "RBN", "RBP", "RBR", "RBT", "RBV", "RCV", "RD1", "RDF", "RDT", "RGD", "RGH", "RHI", "RHS", "RIA", "RIH", "RIK", "RJG", "RKC", "RKH", "RKS", "RKV", "ROF", "RPC", "RPD", "RPG", "RPI", "RPL", "RPM", "RPP", "RPS", "RPT", "RPX", "RRA", "RRP", "RS1", "RSK", "RTD", "RTG", "RTH", "RTP", "RUT", "SAS", "SBH", "SFS", "SGT", "SHE", "SKO", "SKZ", "SLG", "SNY", "SOS", "SPE", "SPN", "SPP", "SPR", "SPT", "SRL", "SSK", "SSS", "ST1", "STI", "SUA", "SUB", "SUC", "SUR", "SVB", "TAL", "TAR", "TAU", "TBT", "TBV", "TCA", "TCB", "TCC", "TCD", "TCF", "TDG", "TE3", "TE4", "TEJ", "TFF", "TFU", "TGA", "TGE", "TGR", "THD", "THF", "THT", "THV", "TI2", "TI3", "TI4", "TI6", "TI7", "TIE", "TIL", "TJF", "TJI", "TJT", "TKF", "TLE", "TLH", "TLK", "TLV", "TLY", "TLZ", "TMC", "TMG", "TMM", "TMU", "TMZ", "TND", "TOT", "TP2", "TPC", "TPF", "TPJ", "TPL", "TPP", "TPV", "TPZ", "TRJ", "TRO", "TRU", "TTA", "TTE", "TTL", "TTV", "TUA", "TVE", "TVN", "TYH", "TZD", "TZT", "ULH", "UNT", "UP1", "UP2", "UPD", "UPH", "UPP", "URA", "USY", "VAY", "VCY", "VFK", "VMV", "VNK", "VPP", "VPS", "VRK", "YAC", "YAE", "YAK", "YAN", "YAS", "YAY", "YBE", "YBH", "YBR", "YBS", "YCK", "YCP", "YCY", "YDI", "YDP", "YEF", "YFV", "YGM", "YHB", "YHI", "YHK", "YHP", "YHS", "YHT", "YHZ", "YIK", "YIT", "YJH", "YJK", "YJY", "YKS", "YKT", "YLC", "YLE", "YLO", "YLY", "YMD", "YMH", "YNK", "YOT", "YOZ", "YP4", "YPC", "YPF", "YPK", "YPL", "YPR", "YPV", "YSA", "YSL", "YSO", "YSU", "YTD", "YTV", "YTY", "YUB", "YUN", "YVB", "YVG", "YZC", "YZG", "YZH", "YZK", "ZBD", "ZBI", "ZBJ", "ZBO", "ZCD", "ZCK", "ZCN", "ZDD", "ZDZ", "ZFB", "ZHH", "ZJB", "ZJI", "ZJL", "ZJV", "ZLH", "ZMT", "ZMY", "ZP6", "ZP8", "ZP9", "ZPA", "ZPC", "ZPE", "ZPF", "ZPG", "ZPR", "ZSF", "ZSG", "ZTG", "ZVO"]

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
