const int PIN_ANA_ROTA = 2;
const int PIN_ALT_ROTA = 3;
const int PIN_ACIL_ROTA = 4;

// YENİ: LED Pinleri
const int LED_ANA = 5;
const int LED_ALT = 6;
const int LED_ACIL = 7;

int sonAnaDurum = -1;
int sonAltDurum = -1;
int sonAcilDurum = -1;

void setup() {
  Serial.begin(9600);
  
  pinMode(PIN_ANA_ROTA, INPUT);
  pinMode(PIN_ALT_ROTA, INPUT);
  pinMode(PIN_ACIL_ROTA, INPUT);
  
  // YENİ: LED'ler çıkış olarak ayarlandı
  pinMode(LED_ANA, OUTPUT);
  pinMode(LED_ALT, OUTPUT);
  pinMode(LED_ACIL, OUTPUT);
}

void loop() {
  // --- 1. KISIM: SENSÖR OKUMA VE PYTHON'A GÖNDERME ---
  int anlikAna = digitalRead(PIN_ANA_ROTA);
  int anlikAlt = digitalRead(PIN_ALT_ROTA);
  int anlikAcil = digitalRead(PIN_ACIL_ROTA);

  if (anlikAna != sonAnaDurum || anlikAlt != sonAltDurum || anlikAcil != sonAcilDurum) {
    Serial.print(anlikAna);
    Serial.print(",");
    Serial.print(anlikAlt);
    Serial.print(",");
    Serial.println(anlikAcil);

    sonAnaDurum = anlikAna;
    sonAltDurum = anlikAlt;
    sonAcilDurum = anlikAcil;
    delay(50); 
  }

  // --- 2. KISIM: PYTHON'DAN GELEN KARARI OKUMA VE LED YAKMA (YENİ) ---
  if (Serial.available() > 0) {
    char gelenEmir = Serial.read(); // Python'dan gelen tek bir harfi oku
    
    // Güvenlik: Yeni emir geldiğinde önce tüm LED'leri söndür
    digitalWrite(LED_ANA, LOW);
    digitalWrite(LED_ALT, LOW);
    digitalWrite(LED_ACIL, LOW);
    
    // Gelen harfe göre ilgili LED'i yak
    if (gelenEmir == 'A') {
      digitalWrite(LED_ANA, HIGH);
    } 
    else if (gelenEmir == 'B') {
      digitalWrite(LED_ALT, HIGH);
    } 
    else if (gelenEmir == 'C') {
      digitalWrite(LED_ACIL, HIGH);
    }
    // Eğer 'X' gelirse (Fatal Error), hiçbir LED yanmaz (veya dilerseniz hepsi yanıp sönebilir).
  }
}