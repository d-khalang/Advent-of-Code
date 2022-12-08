file = open('trees.txt', 'r')
file = file.readlines()
#print(len(file))

outer = ((len(file[0])-1)*4)-4
counter = outer
rowcounter = 0
print(outer)
for y in range(1, len(file)-1):
    rowcounter += 1
    for x in range(1, len(file[0])-2):
        print(y, x)
        theTree = int(file[y][x])
        competitors = []
        for row in range(0, y):
            competitors.append(int(file[row][x]))
            #print("competitors: ", competitors)

        if max(competitors) < theTree:
            counter += 1
            print("stands out, row: {}, column: {}, height: {}".format(y, x, theTree))
            print("thisssss oneeeeeeeee..................................: ")
            competitors = []
            continue
        competitors = []

        for row in range(y+1, len(file)):
            competitors.append(int(file[row][x]))
            #print("competitors: ", competitors)

        if max(competitors) < theTree:
            counter += 1
            print("stands out, row: {}, column: {}, height: {}".format(y, x, theTree))
            print("thisssss oneeeeeeeee..................................: ")
            competitors = []
            continue
        competitors = []
        for column in range(0, x):
            competitors.append(int(file[y][column]))
            #print("competitors: ", competitors)

        if max(competitors) < theTree:
            counter += 1
            print("stands out, row: {}, column: {}, height: {}".format(y, x, theTree))
            print("thisssss oneeeeeeeee..................................: ")
            competitors = []
            continue
        competitors = []
        for column in range(x+1, len(file[0])-1):
            competitors.append(int(file[y][column]))
            #print("competitors: ", competitors)

        if max(competitors) < theTree:
            counter += 1
            print("stands out, row: {}, column: {}, height: {}".format(y, x, theTree))
            print("thisssss oneeeeeeeee..................................: ")
            competitors = []
            continue
        competitors = []
        #if rowcounter == 2:
        #break



print(counter)
#print(file)