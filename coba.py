import os
from datetime import datetime
# from inotify_simple import INotify, flags
#
# inotify = INotify()
# watch_flags = flags.MOVE_SELF | flags.MODIFY
# wd = inotify.add_watch('log.txt', watch_flags)

def countLine(filename):
    f = open(filename, 'r')
    panjang = len(f.readlines())
    f.close()
    return panjang

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

with open('log.txt', 'r') as readFile:
    readFile.seek(0)
    print(readFile.readline())
    print(readFile.readlines())

# x = (1,2,3,4,5)
# (a, b, c, d, e) = x
# print(5)

# a = os.path.getmtime("log.txt")
# b = os.path.getmtime("log_2.txt")
# if a > b:
#     print("besar a")
# else:
#     print("besar b")

# print(datetime.utcfromtimestamp(a).strftime('%d-%m-%Y %H:%M:%S'))
#
# with open("log.txt", "a+") as writeFile:
#     writeFile.write('cobalagi')
#     pass
#
# b = os.path.getmtime('log.txt')
# print(datetime.utcfromtimestamp(b).strftime('%d-%m-%Y %H:%M:%S'))



   # writeFile.seek(3)
   #  for x in writeFile:
   #     print(x.strip())
   # writeFile.write("HHH")