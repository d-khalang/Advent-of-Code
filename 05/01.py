thedic = {1: ['Q', 'M', 'G', 'C', 'L'],
          2: ['R', 'D', 'L', 'C', 'T', 'F', 'H', 'G'],
          3: ['V', 'J', 'F', 'N', 'M', 'T', 'W', 'R'],
          4: ['J', 'F', 'D', 'V', 'Q', 'P'],
          5: ['N', 'F', 'M', 'S', 'L', 'B', 'T'],
          6: ['R', 'N', 'V', 'H', 'C', 'D', 'P'],
          7: ['H', 'C', 'T'],
          8: ['G', 'S', 'J', 'V', 'Z', 'N', 'H', 'P'],
          9: ['Z', 'F', 'H', 'G']}


file = open("crates.txt", "r")
file = file.readlines()


for instruction in file:

    instruction = instruction.strip().split()
    moves = int(instruction[1])
    begin = int(instruction[3])
    end = int(instruction[5])
    print(moves, begin, end)
    for i in range(moves):
        box = thedic[begin].pop()
        print('the box number: ', box)
        thedic[end].append(box)

print(thedic)