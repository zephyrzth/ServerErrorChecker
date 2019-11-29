![Server Error Checker](./images/logo.png)
Server error checker untuk mengecek error yang ada di server* dan mengirimnya ke telegram pengguna melalui bot telegram. Program ini dibuat dengan bahasa pemrograman Python dan dijalankan di server.

__**Hanya error pada Nginx*__

---

## Fitur

1. Mendeteksi error di server secara real-time
2. Mengirim error melalui bot telegram dengan menggunakan api telegram kepada user atau grup telegram yang diinginkan
    Contoh error : 
    ![Error example](./images/error_example.png)

---

## Instalasi

* **Kebutuhan**:

  * Sistem Operasi \(Linux, Windows, macOS\)
  * Python 3
  * Package python `inotify-simple` dan `pyTelegramBotAPI`
  * Koneksi internet
  * Aplikasi telegram
  * Akun telegram yang sudah memiliki username

* **Cara install:**
    * `git clone https://github.com/zephyrzth/ServerErrorChecker.git`
    * Install package pyTelegramBotAPI `pip install pyTelegramBotAPI` (kunjungi https://pypi.org/project/pyTelegramBotAPI/ untuk dokumentasi lengkap)
    * Install package inotify-simple `pip install inotify-simple` (kunjungi https://pypi.org/project/inotify-simple/ untuk dokumentasi lengkap)

---

## Cara Menggunakan
1. Copy file `nginx_checker.py` dari folder `ServerErrorChecker` hasil clone dari github ke server.
2. Buat file teks untuk membandingkan error yang sudah ada (misal: `check.txt`)
3. Buka file `nginx_checker.py` dan ubah:

   ```python
   log = '' # Isi sesuai nama file log error dan direktorinya (misal error.log dari Nginx)
   check = '' # Isi sesuai nama file dan direktorinya pada step 2

   chatId = '' # Isi sesuai id group atau chat telegram yang ingin dikirimkan pesan errornya
   bot = telebot.TeleBot("") # Masukkan kode API token dari bot Telegram yang sudah dibuat
   ```
4. Jalankan `nginx_checker.py` sebagai daemon agar bisa dijalankan di background.

---

## Cara menyiapkan bot telegram untuk mengirim pesan error ke user
1. Cari BotFather di telegram
2. Ketik `/newbot` di chat room BotFather dan ikuti instruksi selanjutnya
![Create Bot](./images/add_bot.png)
3. API token bot akan didapatkan contoh : `911053354:AAFhSlXk7m789BZ2FKNuJNnfBsSMjaV23uMQWk`
4. Buka chat room bot yang telah dibuat dan ketikkan `/start`
5. Buka link `https://api.telegram.org/bot(token_api_bot)/getUpdates` di browser
6. Cari nilai id kalian di nilai `id` pada object `chat` yang sesuai dengan username yang sedang digunakan
    ```{"update_id":8393,"message":{"message_id":3,"from":
    {"id":7474,"first_name":"AAA"},"chat":
    {"id":,"title":""},"date":25497,"new_chat_participant":
    {"id":71,"first_name":"NAME","username":"YOUR_BOT_NAME"}}}
    ```
7. Copy dan paste id yang baru saja didapatkan ke script `nginx_checker.py`

---

## Cara menyiapkan bot telegram untuk mengirim pesan error ke grup
1. Cari BotFather di telegram
2. Ketik `/newbot` di chat room BotFather dan ikuti instruksi selanjutnya
![Create Bot](./images/add_bot.png)
3. API token bot akan didapatkan contoh : `911053354:AAFhSlXk7m789BZ2FKNuJNnfBsSMjaV23uMQWk`
4. Buat grup di telegram dan invite bot yang telah dibuat
5. Cari nilai id yang memiliki tanda minus (-)
6. Buka link `https://api.telegram.org/bot(token_api_bot)/getUpdates` di browser
7. Copy dan paste id yang baru saja didapatkan ke script `nginx_checker.py`
8. Jalankan script python tersebut
9. Akan ada pesan error yang memberikan id yang baru, lalu id itu yang akan digunakan dalam script python

---

## Alternatif untuk mengambil chat id pada grup
1. Tambahkan bot `Telegram Bot Raw`
    ![Add Telegram Bot Raw](./images/add_telegram_bot_raw.png)
2. Undang bot `Telegram Bot Raw` ke grup
3. Bot tersebut akan mengeluarkan info tentang grup tersebut
    ![Id telegram](./images/id_with_telegram_bot_raw.png)
4. Copy dan paste id yang baru saja didapatkan ke script `nginx_checker.py`
5. Jalankan script python tersebut
6. Akan ada pesan error yang memberikan id yang baru, lalu id itu yang akan digunakan dalam script python
