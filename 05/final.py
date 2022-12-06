thedic = {1: 'QMGCL',
          2: 'RDLCTFHG',
          3: 'VJFNMTWR',
          4: 'JFDVQP',
          5: 'NFMSLBT',
          6: 'RNVHCDP',
          7: 'HCT',
          8: 'GSJVZNHP',
          9: 'ZFHG'}


file = open("crates.txt", "r")
file = file.readlines()

counter = 0
for instruction in file:

    instruction = instruction.strip().split()
    moves = int(instruction[1])
    begin = int(instruction[3])
    end = int(instruction[5])
    print(moves, begin, end)

    box = thedic[begin][-moves: ]
    thedic[begin] = thedic[begin].removesuffix(box)
    print("go from the row: ", thedic[begin])
    thedic[end] = thedic[end] + box
    print('yesssss the box contains: ', box)
    print(thedic)

    #print(thedic[end])
    counter += 1
    #if counter == 5:
        #break



print(counter)

#print(len(file))