import os
from datetime import datetime
from inotify_simple import INotify, flags

inotify = INotify()
watch_flags = flags.MOVE_SELF | flags.MODIFY
wd = inotify.add_watch('log.txt', watch_flags)

# x = (1,2,3,4,5)
# (a, b, c, d, e) = x
# print(5)

a = os.path.getmtime("log.txt")
# b = os.path.getmtime("log_2.txt")
# if a > b:
#     print("besar a")
# else:
#     print("besar b")

print(datetime.utcfromtimestamp(a).strftime('%d-%m-%Y %H:%M:%S'))

with open("log.txt", "a+") as writeFile:
    writeFile.write('cobalagi')
    pass

b = os.path.getmtime('log.txt')
print(datetime.utcfromtimestamp(b).strftime('%d-%m-%Y %H:%M:%S'))



   # writeFile.seek(3)
   #  for x in writeFile:
   #     print(x.strip())
   # writeFile.write("HHH")