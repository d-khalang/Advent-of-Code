file = open("marker.txt", "r")
file = file.read()

counter = 0


for i in range(len(file)):
    counter += 1
    print(counter, file[i:i+4])
    theset = "".join(set(file[i:i+4]))
    if len(theset) == 4:
        print("got it: ", file[i:i+4])

        break

print(counter+3)