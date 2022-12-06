file = open("pairs.txt", "r")
file = file.readlines()
final = []

for pair in file:
    tempo = []
    pair = pair.strip().split(',')
    print(pair)
    item1 = pair[0]
    item2 = pair[1]
    tempo.append(int(item1.split('-')[0]))
    tempo.append(int(item1.split('-')[1]))
    tempo.append(int(item2.split('-')[0]))
    tempo.append(int(item2.split('-')[1]))
    print(tempo)
    final.append(tempo)

print(final[0])


counter = 0
for pair in final:
    list1 = [item for item in range(pair[0], pair[1]+1)]
    list2 = [item for item in range(pair[2], pair[3] + 1)]
    result1 = any(elem in list1 for elem in list2)
    result2 = any(elem in list2 for elem in list1)
    if result1 or result2:
        counter += 1
        print('list1 begins in {} and ends in {}\nbeginning of list2 is {} and ending is {} \n'.format(min(list1), max(list2), min(list2), max(list2)))
    #print("list1 is: ", list1, list2)
print(counter)