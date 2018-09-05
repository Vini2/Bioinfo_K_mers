listX = []
listY = []

with open('sorted_X.txt') as distX, open('sorted_Y.txt') as distY, open("unique_X.txt", "a") as Xfile, open("unique_Y.txt", "a") as Yfile:
    for lineX, lineY in zip(distX, distY):
        if lineX == lineY:
            continue
        elif lineX < lineY:
            Xfile.write(lineX)
            Xfile.write("\n")
            lineX=next(distX, None)
            continue
        elif lineX > lineY:
            Yfile.write(lineY)
            Yfile.write("\n")
            lineY=next(distY, None)
            continue