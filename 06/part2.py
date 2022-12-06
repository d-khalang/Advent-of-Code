file = open("marker.txt", "r")
file = file.read()

counter = 0


for i in range(len(file)):
    counter += 1
    print(counter, file[i:i+14])
    theset = "".join(set(file[i:i+14]))
    if len(theset) == 14:
        print("got it: ", file[i:i+14])

        break

print(counter+13)