# Açıklanabilir Karar Destek Sistemi: Otonom Rota Seçici

Bu proje, görev kritik sistemler (İHA, Otonom Kara Araçları) için tasarlanmış, **Donanım-Yazılım Eş-Simülasyonu (Co-Simulation)** tabanlı bir açıklanabilir karar destek prototipidir. Sayzek ATP (Araştırma ve Teknoloji Programı) hedefleri doğrultusunda Ahali takımı tarafından geliştirilmiştir.

## ⚙️ Sistem Şeması ve Donanım
Sistemin Proteus üzerindeki genel donanım mimarisi ve bağlantı şeması aşağıdadır:

![Sistem Şeması](gorseller/sema.png)<img width="907" height="677" alt="şema" src="https://github.com/user-attachments/assets/3b44f08e-fce4-467a-b585-4cae442cd282" />

*(Not: Buraya sistemin genel bağlantı şemasının ekran görüntüsünü ekleyin)*

## 🎯 Projenin Amacı
Otonom sistemlerin aldığı kararların arkasındaki nedenlerin (Gerekçelendirme/Explainability) insanlar tarafından anlaşılabilir olmasını sağlamak. Sistem, anlık sensör verilerini işleyerek sadece bir rota seçmekle kalmaz; aynı zamanda bu kararı **neden** aldığını açık, metin tabanlı bir log olarak terminale yazdırır ve donanıma (LED'ler) fiziksel geri bildirim gönderir.

## 🚀 Senaryolar ve Otonom Kararlar (Canlı Testler)

### 1. Durum: Normal Operasyon (Ana Rota)
Tüm yollar açık. Python **Ana Rota** kararı verir ve donanımdaki yeşil LED'i yakar.
<img width="1917" height="1017" alt="çalışırken" src="https://github.com/user-attachments/assets/495c41e4-b602-49a3-82dc-16c8cc53aa0c" />


### 2. Durum: Engel Tespiti (Alternatif Rota)
Ana rotada engel tespit edildiğinde, sistem **Alternatif Rota** kararı verir (Sarı LED) ve gerekçeyi terminale bildirir.
<img width="1917" height="1017" alt="çalışırken2" src="https://github.com/user-attachments/assets/2864007b-ff0a-4d35-abe8-eb9a71969c4e" />


### 3. Durum: Kritik Engel (Acil Durum Rotası)
Ana ve Alternatif rotalar kapalı olduğunda, sistem görev sürekliliği için **Acil Durum Rotasına** (Kırmızı LED) geçer.
![Acil Durum Rotası Durumu](gorseller/durum_3_acil_rota.png)<img width="1917" height="1017" alt="çalışırken3" src="https://github.com/user-attachments/assets/c46baec8-61bb-4b22-95c8-2271d3fb4eb1" />


*(Tüm yollar kapandığında ise sistem FATAL ERROR vererek operasyonu durdurur ve donanımı güvenli moda alır.)*

## 🛠️ Kurulum ve Çalıştırma
1. `Proteus_Simulation` klasöründeki şemayı açın.
2. VSPE veya com0com ile `COM1 <-> COM2` köprüsünü kurun.
3. Arduino .hex dosyasının Proteus'a yüklü olduğundan emin olun ve simülasyonu başlatın.
4. `Python_Code` klasöründeki `main.py` betiğini çalıştırın.
5. Proteus üzerindeki butonlarla oynayarak terminaldeki açıklanabilir kararları anlık gözlemleyin.
