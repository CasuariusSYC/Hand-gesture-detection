# Hand Gesture Control dengan MediaPipe to Arduino


### Perubahan Utama

#### 1. Multi-Hand Support
```python
# Sebelumnya (v1.0)
num_hands=1  # Hanya 1 tangan

# Sekarang (v2.0)  
num_hands=2  # Support 2 tangan
```

#### 2. Warna Berbeda per Tangan
```python
# Sebelumnya: Semua tangan warna hijau
def draw_landmarks(frame, hand_landmark_list):
    cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

# Sekarang: Setiap tangan warna berbeda
colors = [(0, 255, 0), (255, 255, 0)]  # Hijau, Kuning
for idx, hand_landmark_list in enumerate(results.hand_landmarks):
    color = colors[idx % len(colors)]
    draw_landmarks(frame, hand_landmark_list, color)
```

#### 3. Label FIST/OPEN di Atas Tangan
```python
# Baru: Menampilkan label di atas setiap tangan
if is_fist(hand_landmark_list):
    cv2.putText(frame, "FIST", (x - 20, y - 20), 
               cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)
else:
    cv2.putText(frame, "OPEN", (x - 20, y - 20), 
               cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)
```

#### 4. Stability Filter (Anti-Flickering)
```python
# Baru: Counter untuk stabilitas
fist_counter = 0
no_fist_counter = 0
STABILITY_THRESHOLD = 3  # 3 frame konsisten

# Hanya update state jika sudah stabil
if fist_counter >= STABILITY_THRESHOLD:
    indicator_state = 1  # ACTIVE
elif no_fist_counter >= STABILITY_THRESHOLD:
    indicator_state = 0  # LOW
```

#### 5. Informasi Tambahan di Layar
```python
# Baru: Menampilkan jumlah tangan dan kepalan
cv2.putText(frame, f"Hands: {hand_count} | Fists: {fist_count}", 
           (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

# Baru: Indikator ACTIVE menampilkan jumlah kepalan
cv2.putText(frame, f"x{fist_count}", (75, 30), 
           cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)
```

#### 6. Logika Deteksi yang Lebih Baik
```python
# Baru: Deteksi kepal per tangan
fist_count = 0
for hand_landmark_list in results.hand_landmarks:
    if is_fist(hand_landmark_list):
        fist_count += 1

# Jika ada SATU saja tangan yang kepal -> ACTIVE
if fist_count > 0:
    fist_detected = True
```

### Perbaikan Bug

#### 1. Syntax Error Fix
```python
# Sebelumnya (Error)
if TogleGraphicIndicatorStateFlag && HandDetectedFlag:  # Python tidak pakai &&

# Sekarang (Benar)
if TogleGraphicIndicatorStateFlag and HandDetectedFlag:  # Pakai 'and'
```

#### 2. Boolean Logic Fix
```python
# Sebelumnya (Error)
if (TogleGraphicIndicatorStateFlag == False) && (results.hand_landmarks == False):

# Sekarang (Benar)
if (TogleGraphicIndicatorStateFlag == False) and (not results.hand_landmarks):
```

#### 3. State Persistence Fix
```python
# Sebelumnya: State berubah ke LOW saat tangan hilang
else:
    indicator_state = 0  # Langsung LOW

# Sekarang: State tetap bertahan
else:
    # TANGAN HILANG: STATE TETAP BERTAHAN
    pass  # State tidak berubah
```

### Perbandingan Fitur

| Fitur | v1.0 | v2.0 |
|-------|------|------|
| Jumlah Tangan | 1 tangan | 2 tangan |
| Warna Tangan | Sama semua | Berbeda per tangan |
| Label Tangan | Tidak | Ya (FIST/OPEN) |
| Counter | Tidak | Ya (Hands & Fists) |
| Stability Filter | Tidak | Ya (3-frame threshold) |
| Anti-Flickering | Tidak | Ya |
| State Persistence | Tidak | Ya |
| Debug Info | Minimal | Lengkap |
| Indikator Detail | LOW/ACTIVE | LOW/ACTIVE + x{fist_count} |

### Cara Update

#### 1. Clone Repository
```bash
git clone https://github.com/yourusername/hand-gesture-control.git
cd hand-gesture-control
```

#### 2. Update Dependencies
```bash
pip install --upgrade opencv-python mediapipe pyserial
```

#### 3. Jalankan Aplikasi
```bash
python hand_gesture_control.py
```

### Changelog Detail

#### Added (v2.0)
- Multi-hand support (2 hands)
- Different colors for each hand (Green & Yellow)
- FIST/OPEN labels above each hand
- Hand counter display
- Fist counter display
- Stability filter (3-frame threshold)
- Fist count on ACTIVE indicator
- Debug information panel
- Better visual feedback

#### Fixed (v2.0)
- Boolean logic errors (&& to and)
- State comparison issues
- Detection flickering
- State persistence when hand lost
- Syntax errors in conditional statements

#### Changed (v2.0)
- Simplified state system (0 = LOW, 1 = ACTIVE)
- Enhanced visual indicators
- Improved code structure
- Better error handling

### Issue Tracking

| Issue | Status | Solution |
|-------|--------|----------|
| Syntax error && | Fixed | Ganti dengan and |
| State berubah saat tangan hilang | Fixed | State persistence |
| Flickering deteksi | Fixed | Stability filter |
| Tidak bisa deteksi 2 tangan | Fixed | Multi-hand support |
| Tidak ada label tangan | Fixed | FIST/OPEN labels |

---

## Download

### Source Code
- [Download hand_gesture_control.py](https://raw.githubusercontent.com/yourusername/hand-gesture-control/main/hand_gesture_control.py)

### Full Repository
```bash
git clone https://github.com/yourusername/hand-gesture-control.git
```

### Requirements File
```bash
# requirements.txt
opencv-python>=4.5.0
mediapipe>=2.0.0
pyserial>=3.5.0
urllib3>=1.26.0
```

### Install via pip
```bash
pip install -r requirements.txt
```

---

**Dibuat oleh**: [Andrith Blaer Nikhy Imanuel Reba]  
**Institusi**: SMKN 2 Manokwari  
**Jurusan**: Teknik Elektronika Komputer  


---

<p align="center">
  <b>SMKN 2 Manokwari - Teknik Elektronika Komputer</b>
</p>
