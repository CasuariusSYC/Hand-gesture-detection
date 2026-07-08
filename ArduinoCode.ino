/*
 * Hand Gesture Control - Arduino Receiver
 * 
 * Menerima sinyal dari Python via Serial UART
 * '1' = Nyalakan LED (Fist Detected / ACTIVE)
 * '0' = Matikan LED (No Fist / LOW)
 * 
 * Pin 13 = LED Built-in (bisa diganti ke pin lain)
 * 
 * SMKN 2 Manokwari - Teknik Elektronika Komputer
 */

// Definisikan pin LED
#define LED_PIN 13  // Bisa diganti ke pin lain (misal: 9, 10, 11)

// Variabel untuk menyimpan state
char receivedChar = '0';
bool ledState = false;

void setup() {
  // Inisialisasi Serial
  Serial.begin(9600);  // Pastikan sama dengan Python (9600 baud)
  
  // Set pin LED sebagai output
  pinMode(LED_PIN, OUTPUT);
  
  // Matikan LED saat awal
  digitalWrite(LED_PIN, LOW);
  
  // Tampilkan pesan di Serial Monitor (untuk debugging)
  Serial.println("=== Hand Gesture Control Ready ===");
  Serial.println("Waiting for command...");
  Serial.println("'1' = Turn ON | '0' = Turn OFF");
  Serial.println("====================================");
}

void loop() {
  // Cek apakah ada data yang masuk dari Serial
  if (Serial.available() > 0) {
    // Baca karakter dari Serial
    receivedChar = Serial.read();
    
    // Proses perintah
    if (receivedChar == '1') {
      // Nyalakan LED
      digitalWrite(LED_PIN, HIGH);
      ledState = true;
      
      // Kirim konfirmasi ke Python (opsional)
      Serial.println("ACTIVE: LED ON");
      
    } else if (receivedChar == '0') {
      // Matikan LED
      digitalWrite(LED_PIN, LOW);
      ledState = false;
      
      // Kirim konfirmasi ke Python (opsional)
      Serial.println("LOW: LED OFF");
      
    } else {
      // Jika ada karakter lain, abaikan
      Serial.print("Unknown command: ");
      Serial.println(receivedChar);
    }
  }
}

// Fungsi tambahan untuk debugging
void printStatus() {
  Serial.print("LED State: ");
  Serial.println(ledState ? "ON" : "OFF");
}