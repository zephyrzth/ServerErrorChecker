import telebot
import time
import mmap

log = "log.txt"
log2 = "log.txt.2"
check = "check.txt"

chatId = 872706884

bot = telebot.TeleBot("911053354:AAFhSlXk7muBZ2FKNuJNnfB9MjaVOauMQWk")


def countLine(filename):
    # 	f = open(filename, "r+")
    # 	buf = mmap.mmap(f.fileno(), 0)
    # 	lines = 0
    # 	readline = buf.readline
    # 	while readline():
    # 		lines += 1
    #     f.close()
    # 	return lines
    f = open(filename, 'r')
    panjang = len(f.readlines())
    f.close()
    return panjang


def beda(log, check):
    if (countLine(log) > countLine(check)):
        # print("countline log " +str(countLine(log)))
        # print("countline check " + str(countLine(check)))
        # pasti ada beda
        return 1
    elif (countLine(log) < countLine(check)):
        # pasti ga error, ganti log baru
        if (countLine(log) != 0):
            return -2
        return -1
    else:
        return 0


def bedaIsi(log, check):
    fileLog = open(log, 'r')
    fileCheck = open(check, 'r')
    fileLog.seek(0)
    fileCheck.seek(0)
    len1 = countLine(check)
    isiLog = ''
    isiCheck = ''
    for line in range(len1):
        isiLog = fileLog.readline().replace('\n', '')
        isiCheck = fileCheck.readline().replace('\n', '')
        if (isiLog != isiCheck):
            fileLog.close()
            fileCheck.close()
            return -1
    hasil = fileLog.readlines()
    fileLog.close()
    fileCheck.close()
    return hasil


while 1:
    print("ehamsuk")
    kondisi = beda(log, check)
    # kondisi kalau ada beda jumlah line
    print(kondisi)
    if (kondisi == 1):
        kondisi = bedaIsi(log, check)
        if (kondisi != -1):
            print("beda ada")
            kirim = 'ERROR TERDETEKSI:\n'
            for baris in kondisi:
                kirim += baris
            bot.send_message(chatId, kirim)
            f1 = open(check, 'a')
            f1.write('\n')
            for baris in kondisi:
                f1.write(baris)
            f1.close()
    # line sama, tp beda isi
    elif (bedaIsi(log, check) == -1):
        kondisi = -1
        # langsung send file log
        # kosongin file checker, kemungkinan error log ada yg ganti manual
        bot.send_message(chatId,
                         "Ada kesalahan dalam error log, file checker akan disamakan dengan file log dan file log akan dikirimkan")
        f1 = open(log, 'rb')
        bot.send_document(chatId, f1)
        f1.close()
        with open(log) as f:
            with open(check, 'w') as f1:
                for line in f:
                    if "ROW" in line:
                        f1.write(line)
    # kalau tidak ad beda
    else:
        time.sleep(5)
        continue

    # kondisi kalau ada kejanggalan
    if (kondisi == -1):
        print("beda aneh")
        kondisi = beda(log2, check)
        # ada tiga kemungkinan,
        # line log2 sama, lebih banyak, atau sedikit

        # kalau log2 lebih banyak, cek isinya
        if (kondisi == 1):
            kondisi = bedaIsi(log2, check)
            # kalau kondisi == -1, akan di check nanti

            # kalau memang ada beda dan bukan error, kirim pesan
            if (kondisi != -1):
                kirim = 'ERROR TERDETEKSI:\n'
                for baris in kondisi:
                    kirim += baris
                bot.send_message(chatId, kirim)
                f1 = open(check, 'a+')
                f1.write(kondisi)
                f1.close

        # kalau log2 sama, berarti log hanya terupdate, tanpa ada error baru
        elif (kondisi == 0):
            f1 = open(check, 'w')
            f1.close()
            # print("kosng goblok")
            continue

    # kalau ternyata log2 isinya beda dari check
    # atau kalau log2 lebih sedikit, berarti ada error
    if (kondisi == -1 or kondisi == -2):
        # error log rusak, file log akan dikirim dan disarankan
        # untuk melakukan pengecekan manual
        # send 2 file
        # f1 = open(check,'w')
        # f1.close()
        iya = 1
    time.sleep(5)
