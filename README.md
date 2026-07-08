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

---
### opencv-python

---
### pyserial

---
