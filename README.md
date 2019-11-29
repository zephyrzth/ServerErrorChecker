# Server Error Checker
Server error checker untuk mengecek error yang ada di server* dan mengirimnya ke telegram pengguna melalui bot telegram. Program ini dibuat dengan bahasa pemrograman Python dan dijalankan di server.

*Sementara hanya error pada Nginx

---

## Fitur

1. Mendeteksi error di server secara real-time
2. Mengirim error melalui bot telegram dengan menggunakan api telegram kepada grup telegram yang diinginkan

---

## Instalasi

* **Kebutuhan**:

  * Sistem Operasi \(Linux, Windows, macOS\)
  * Python 3
  * Package python `inotify-simple` dan `pyTelegramBotAPI`
  * Koneksi internet

* **Cara install:**
    * `git clone https://github.com/zephyrzth/ServerErrorChecker.git`
    * Install package pyTelegramBotAPI `pip install pyTelegramBotAPI`
    * Install package inotify-simple `pip install inotify-simple`

---

## Cara Menggunakan
1. Copy file `nginx_checker.py` dari folder `ServerErrorChecker` hasil clone dari github ke server.
2. Buat file teks untuk membandingkan error yang sudah ada (misal: `check.txt`)
3. Buka file `nginx_checker.py` dan ubah:

   ```python
   log = '' // Isi sesuai nama file log error dan direktorinya (misal error.log dari Nginx)
   check = '' // Isi sesuai nama file dan direktorinya pada step 2

   chatId = '' // Isi sesuai id group atau chat telegram yang ingin dikirimkan pesan errornya
   bot = telebot.TeleBot("") // Masukkan kode API dari bot Telegram yang sudah dibuat
   ```
4. Jalankan `nginx_checker.py` sebagai daemon agar bisa dijalankan di background.
