class Katilimci:
    """Katılımcı bilgilerini tutan sınıf"""
    def __init__(self, katilimci_id, ad, email):
        self.katilimci_id = katilimci_id
        self.ad = ad
        self.email = email

class Etkinlik:
    """Etkinlik bilgilerini ve katılımcı yönetimini yapan sınıf"""
    def __init__(self, etkinlik_id, ad, tarih, kapasite):
        self.etkinlik_id = etkinlik_id
        self.ad = ad
        self.tarih = tarih
        self.kapasite = kapasite
        self.katilimcilar = []  

    def katilimci_ekle(self, katilimci):
        """Metot: Etkinliğe katılımcı ekler, kapasite kontrolü yapar"""
        if len(self.katilimcilar) < self.kapasite:
            self.katilimcilar.append(katilimci)
            print(f"BAŞARILI: {katilimci.ad}, {self.ad} etkinliğine eklendi.")
            return True
        else:
            print(f"HATA: {self.ad} etkinliği için kontenjan dolu! ({self.kapasite} kişilik)")
            return False

    def katilim_raporu(self):
        """Ek Özellik: Etkinliğe kaç kişi katıldı raporu sunar"""
        print(f"\n--- {self.ad} Etkinlik Raporu ---")
        print(f"Tarih: {self.tarih}")
        print(f"Toplam Kapasite: {self.kapasite}")
        print(f"Kayıtlı Katılımcı Sayısı: {len(self.katilimcilar)}")
        print("Katılımcı Listesi:")
        for k in self.katilimcilar:
            print(f"- {k.ad} ({k.email})")
        print("-" * 30)

class Bilet:
    """Bilet oluşturma işlemlerini yöneten sınıf"""
    def __init__(self, bilet_id, etkinlik, katilimci):
        self.bilet_id = bilet_id
        self.etkinlik = etkinlik
        self.katilimci = katilimci

    def bilet_olustur(self):
        """Metot: Bilet bilgilerini ekrana yazdırır"""
        print("\n" + "="*25)
        print("      DİJİTAL BİLET      ")
        print("="*25)
        print(f"Bilet No   : {self.bilet_id}")
        print(f"Etkinlik   : {self.etkinlik.ad}")
        print(f"Tarih      : {self.etkinlik.tarih}")
        print(f"Katılımcı  : {self.katilimci.ad}")
        print("="*25)

# --- SİSTEMİ TEST ETME ---

# 1. Etkinlik Tanımlama (Örnek kapasite: 2)
etkinlik1 = Etkinlik(1, "Beşiktaş vs Göztepe Maçı", "20.05.2026", 2)

# 2. Katılımcıları Oluşturma
k1 = Katilimci(101, "Ahmet Poyraz Kara", "poyraz@iku.edu.tr")
k2 = Katilimci(102, "Mert Öztürk", "mert@gmail.com")
k3 = Katilimci(103, "Can Demir", "can@gmail.com")

# 3. Katılımcıları Ekleme ve Bilet Oluşturma Senaryosu
katilimcilar = [k1, k2, k3]
bilet_sayaci = 1000

for kisi in katilimcilar:
    # Katılımcı eklemeyi dene (Kapasite kontrolü metot içinde yapılıyor)
    if etkinlik1.katilimci_ekle(kisi):
        bilet_sayaci += 1
        yeni_bilet = Bilet(f"B-{bilet_sayaci}", etkinlik1, kisi)
        yeni_bilet.bilet_olustur()

# 4. Raporu Görüntüle
etkinlik1.katilim_raporu()
