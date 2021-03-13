import telebot
import difflib
import json
from inotify_simple import INotify, flags
from threading import Thread

CONFIG_FILE = 'config.json'


def get_config():
    try:
        with open(CONFIG_FILE, 'rb') as openFile:
            return json.load(openFile)
    except:
        print('File config tidak ditemukan')
        return None


logs = get_config()['check_files']
checks = ["check" + str(i) + ".txt" for i in range(len(logs))]
for check in checks:
    with open(check, 'w'):
        pass

chatIds = get_config()['receiver_id']
botId = get_config()['bot_id']

watch_flags = flags.MOVE_SELF | flags.MODIFY


def beda(log, check, inotify, bot):
    inotify.add_watch(log, watch_flags)
    try:
        for event in inotify.read(timeout=1):
            if event is not None:
                for flag in flags.from_mask(event.mask):
                    if str(flag) == 'flags.MODIFY':
                        with open(log, "r") as logFile, open(check) as checkFile:
                            loglines = logFile.readlines()
                            checklines = checkFile.readlines()
                            d = difflib.Differ()
                            diff = d.compare(loglines, checklines)
                            perbedaan = "".join(x[2:] for x in diff if x.startswith('- '))
                        if perbedaan != "":
                            try:
                                kirim = 'ERROR TERDETEKSI:\n' + perbedaan
                                for chatId in chatIds:
                                    bot.send_message(chatId, kirim)
                                with open(check, "a+") as appendFile:
                                    appendFile.write(perbedaan)
                            except:
                                print("Gagal mengirim error")
                        else:
                            pass
                    elif str(flag) == 'flags.MOVE_SELF':
                        with open(check, 'w'):
                            pass
                    elif str(flag) == 'flags.IGNORED':
                        print("warning")
                        for chatId in chatIds:
                            bot.send_message(chatId, "Peringatan! file error.log diubah secara manual")
                    else:
                        print(str(flag))
                        for chatId in chatIds:
                            bot.send_message(chatId, str(flag))
    except:
        print("error event")
        inotify.rm_watch(log)


def start_thread(log, check):
    inotify = INotify()
    bot = telebot.TeleBot(botId)
    i = 1
    while 1:
        if i == 1:
            with open(log, "r") as logFile, open(check) as checkFile:
                loglines = logFile.readlines()
                checklines = checkFile.readlines()
                d = difflib.Differ()
                diff = d.compare(loglines, checklines)
                perbedaan = "".join(x[2:] for x in diff if x.startswith('- '))
            if perbedaan != "":
                try:
                    kirim = 'ERROR TERDETEKSI:\n' + perbedaan
                    for chatId in chatIds:
                        bot.send_message(chatId, kirim)
                    with open(check, "a+") as appendFile:
                        appendFile.write(perbedaan)
                except:
                    print("Gagal mengirim error")
            else:
                pass
            i += 1
        beda(log, check, inotify, bot)


if __name__ == "__main__":
    threads = []
    for index, log in enumerate(logs):
        threads.append(
            Thread(target=start_thread, args=(log, checks[index])))
        threads[-1].start()

    for t in threads:
        t.join()
