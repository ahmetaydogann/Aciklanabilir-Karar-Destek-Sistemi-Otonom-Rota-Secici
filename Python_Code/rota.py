import serial
import time
import traceback

PORT = 'COM2'
BAUD_RATE = 9600

try:
    try:
        ser = serial.Serial(PORT, BAUD_RATE, timeout=1)
        print(f"[*] Sistem Başlatıldı. {PORT} üzerinden donanım dinleniyor...")
        print("[*] Yeni telemetri verisi bekleniyor...\n")
    except serial.SerialException:
        print(f"[!] HATA: {PORT} açılamadı. com0com/VSPE köprüsünü kontrol edin.")
        input("Çıkmak için Enter'a basın...")
        exit()

    while True:
        if ser.in_waiting > 0:
            try:
                raw_data = ser.readline().decode('utf-8', errors='ignore').strip()
                
                if not raw_data:
                    continue
                    
                durumlar = raw_data.split(',')
                
                if len(durumlar) == 3:
                    durum_1 = durumlar[0]
                    durum_2 = durumlar[1]
                    durum_3 = durumlar[2]
                    
                    # Sadece saf veri dizilimi görünür
                    print(f"> Gelen Veri: [{durum_1}, {durum_2}, {durum_3}]")
                    
                    if durum_1 == '0':
                        print("[SİSTEM MESAJI] Yol açık. ANA ROTA üzerinden ilerleniyor.\n")
                        ser.write(b'A')  
                        
                    elif durum_1 == '1' and durum_2 == '0':
                        print("[KARAR DEĞİŞİKLİĞİ] Ana rotada engel tespit edildi.")
                        print("--> Gerekçe: Operasyon güvenliği riske girdiği için ALTERNATİF ROTA aktif edildi.\n")
                        ser.write(b'B')  
                        
                    elif durum_1 == '1' and durum_2 == '1' and durum_3 == '0':
                        print("[KRİTİK UYARI] Ana ve alternatif rotalar kapalı.")
                        print("--> Gerekçe: Görev sürekliliğini sağlamak adına ACİL DURUM ROTASI'na geçildi.\n")
                        ser.write(b'C')  
                        
                    elif durum_1 == '1' and durum_2 == '1' and durum_3 == '1':
                        print("[FATAL ERROR] Tüm rotalar engellenmiştir!")
                        print("--> Gerekçe: Geçerli güvenli rota kalmadığı için OPERASYON DURDURULDU.\n")
                        ser.write(b'X')  
                        
                else:
                    print(f"[BOZUK PAKET] Gelen veri işlenemedi: {raw_data}")
                    
            except Exception as e:
                print(f"[UYARI] Veri ayrıştırma hatası: {e}")
                
        time.sleep(0.1)

except Exception as e:
    print("\n[!] BEKLENMEYEN BİR HATA OLUŞTU:")
    traceback.print_exc()
    input("\nPencereyi kapatmak için Enter'a basın...")