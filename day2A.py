if __name__ == '__main__':
    counter = 0
    opcode = 0
    fi = open("day2_input.txt")
    data = list(map(int, fi.read().split(',')))
    data[1] = 12
    data[2] = 2
    while not counter > len(data) - 1:
        opcode = data[counter]
        if opcode == 1:
            data[data[counter + 3]] = data[data[counter + 1]] + data[data[counter + 2]]
        elif opcode == 2:
            data[data[counter + 3]] = data[data[counter + 1]] * data[data[counter + 2]]
        elif opcode == 99:
            print(data[0])
            exit(0)
        counter += 4
    print('Stop code not found')
