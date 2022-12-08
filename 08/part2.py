file = open('trees.txt', 'r')
file = file.readlines()
competitors = []
mostView = []
counter = 0
for y in range(0, len(file)):
    for x in range(0, len(file[0])-1):
        theTree = int(file[y][x])
        print(y, x, theTree)

        view = 1
        for row in range(y-1, -1, -1):
            if int(file[row][x]) < theTree:
                competitors.append(file[row][x])
            elif int(file[row][x]) >= theTree:
                competitors.append(file[row][x])
                break
        if len(competitors) != 0:
            view = view * len(competitors)
        print(competitors, view)
        competitors = []

        for row in range(y + 1, len(file)):
            if int(file[row][x]) < theTree:
                competitors.append(file[row][x])
            elif int(file[row][x]) >= theTree:
                competitors.append(file[row][x])
                break
        if len(competitors) != 0:
            view = view * len(competitors)
        print(competitors, view)
        competitors = []

        for column in range(x-1, -1, -1):
            if int(file[y][column]) < theTree:
                competitors.append(int(file[y][column]))
            elif int(file[y][column]) >= theTree:
                competitors.append(int(file[y][column]))
                break
        if len(competitors) != 0:
            view = view * len(competitors)
        print(competitors, view)
        competitors = []

        for column in range(x+1, len(file[0])-1):
            if int(file[y][column]) < theTree:
                competitors.append(int(file[y][column]))
            elif int(file[y][column]) >= theTree:
                competitors.append(int(file[y][column]))
                break
        view = view * len(competitors)
        print(competitors, view)
        competitors = []
        if len(competitors) != 0:
            view = view * len(competitors)


        mostView.append(view)
        print()
    counter += 1
    #if counter >= 2:
        #break
print(max(mostView))
