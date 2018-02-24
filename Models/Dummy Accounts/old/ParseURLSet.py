count = 0
lineCt = 0
first = True
previous = ""
current = ""

with open("fall11_urls.txt", encoding="Latin-1") as infile:
    for line in infile:
        try:
            if(first):
                previous = line[:9]
                first = False
                lineCt = 1
                continue
            current = line[:9]
            if(current!=previous):
                if(lineCt<2000):
                    lineCt = 1
                    previous = current
                    continue
                print(previous)
                count+=1
                lineCt = 1
                previous = current
            lineCt += 1
        except:
            continue
print(count)
