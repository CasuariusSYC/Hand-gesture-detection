# Hand-gesture-detection

Di project ini berfungsi dengan mendeteksi gestur tangan dengan memanfaatkan arsitektur machine learning yang sudah di efisiensi agar CPU Frandly, arsitektur yang saya pakai di sini adalah MediaPipe, logic nya sederhana, saya mengekstrak variable hasil pemrosesan Model ML tersebut, di dalam variable berjenis array ini terdapat beberapa data yaitu class, confidance, dan kordinat objek yang tedeteksi
Kemudain untuk file model nya saya menggunakan model yang sudah di sediakan oleh google yang sudah di latih untuk mengenali bentuk tangan kemudian meletakan kordinat di tiap engkel jari, lalu hasilnya di visualisasikan dengan algoritma sederhana untuk membuat garis dari satu kordinat ke kordinat lain agar user dapat melihat secara live hasil dari pemrosesan, kemudian menggunakan algoritma untuk mendeteksi jarak dari satu kordinat dengan kordinat lain yang berubah yang mengindikasi gestur dari tangan pengguna, kemudian hasilnya mengaktifkan flag untuk mengirim data ke Mikrokontroler melalui serial comunication.

## Features

- Real-time hand tracking
- CPU-friendly menggunakan MediaPipe Tasks
- Visualisasi landmark tangan
- Deteksi gesture kepalan tangan (fist detection)
- Auto download model MediaPipe
- Auto detect Arduino Serial Port
- Mengirim data ke mikrokontroler melalui Serial Communication

---



### mediapipe

MediaPipe adalah kerangka kerja open-source dari Google yang memungkinkan aplikasi untuk memproses data sensorik (seperti video atau audio) dan menjalankan inferensi machine learning secara real-time. Sangat populer untuk visi komputer, kerangka kerja ini banyak digunakan untuk fitur pelacakan gerak tubuh, wajah, dan objek langsung di perangkat

---

### opencv-python

OpenCV-Python adalah pustaka pemrograman sumber terbuka yang digunakan untuk memproses gambar dan video secara real-time. Pustaka ini memadukan kekuatan bahasa pemrograman Python dengan ribuan algoritma visi komputer dan kecerdasan buatan, memungkinkan program untuk "melihat" dan menganalisis lingkungan visual

---

### pyserial

PySerial adalah pustaka (library) Python yang digunakan untuk mengontrol komunikasi port serial (seperti RS-232). Pustaka lintas platform ini memungkinkan Anda menghubungkan skrip Python dengan perangkat keras eksternal seperti mikrokontroler (Arduino, Raspberry Pi), sensor, dan perangkat IoT untuk membaca dan mengirim data dengan mudah

---
