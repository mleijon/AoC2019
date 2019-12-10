def operation(opc, index):
    if opc == '1':
        data[data[index + 3]] = data[data[index + 1]] + data[data[index + 2]]
    elif opc == '2':
        data[data[index + 3]] = data[data[index + 1]] * data[data[index + 2]]
    elif opc == '101':
        data[data[index + 3]] = data[index + 1] + data[data[index + 2]]
    elif opc == '102':
        data[data[index + 3]] = data[index + 1] * data[data[index + 2]]
    elif opc == '1001':
        data[data[index + 3]] = data[data[index + 1]] + data[index + 2]
    elif opc == '1002':
        data[data[index + 3]] = data[data[index + 1]] * data[index + 2]
    elif opc == '1101':
        data[data[index + 3]] = data[index + 1] + data[index + 2]
    elif opc == '1102':
        data[data[index + 3]] = data[index + 1] * data[index + 2]
    elif opc == '3':
        print('Enter a value (1):')
        data[data[index + 1]] = int(input())
    elif opc == '4':
        print(data[data[index + 1]])
    elif opc == '104':
        print(data[index + 1])
    elif opc == '99':
        exit(0)
    else:
        exit('opcode {} unknown'.format(opcode))
    if opc in ['3', '4', '104']:
        index += 2
        return index
    else:
        index += 4
        return index


if __name__ == '__main__':
    fi = open("day5_input.txt")
    data = list(map(int, fi.read().split(',')))
    index = 0
    opcode = data[index]
    while True:
        new_index = operation(str(opcode), index)
        index = new_index
        opcode = data[index]

