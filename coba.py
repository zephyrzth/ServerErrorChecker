x =  (1,2,3,4,5)
(a, b, c, d, e) = x
print(5)

with open("log.txt", "a+") as writeFile:
    writeFile.seek(3)
    #for x in writeFile:
    #    print(x.strip())
    writeFile.write("HHH")