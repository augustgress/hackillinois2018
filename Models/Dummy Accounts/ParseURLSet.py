count = 0
lineCt = 0
first = True
previous = ""
current = ""
images = ""

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
                if(lineCt<2200):
                    lineCt = 1
                    previous = current
                    images = ""
                    continue
                with open("test/" + previous+".txt") as file:
                    file.write(images)
                images = ""
                print(previous)
                count+=1
                lineCt = 1
                previous = current
                images += line[15:] + "\n"
            lineCt += 1
        except:
            continue
print(count)


# with open("fall11_urls.txt", encoding="Latin-1") as infile:
#     for line in infile:
#         print(line[15:])
