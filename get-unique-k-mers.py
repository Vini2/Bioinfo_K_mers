listX = []
listY = []

with open('sorted_X.txt') as distX:
    for line in distX:
        lineElements = line.split()
        listX.append(lineElements[0])

with open('sorted_Y.txt') as distY:
    for line in distY:
        lineElements = line.split()
        listY.append(lineElements[0])

Xfile = open("unique_X.txt", "a")
Yfile = open("unique_Y.txt", "a")

i = 0
j = 0

while i<len(listX) and j< len(listY):
    if listX[i] == listY[j]:
        i=i+1
        j=j+1
        continue
    elif listX[i]<listY[j]:
        Xfile.write(listX[i])
        Xfile.write("\n")
        i=i+1
        continue
    elif listX[i]>listY[j]:
        Yfile.write(listY[j])
        Yfile.write("\n")
        j=j+1
        continue