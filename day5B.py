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
        print('Enter a value:')
        data[data[index + 1]] = int(input())
    elif opc == '4':
        print(data[data[index + 1]])
    elif opc == '104':
        print(data[index + 1])
    elif opc == '5':
        if data[data[index + 1]] != 0:
            index = data[data[index + 2]]
            return index
        else:
            return index + 3
    elif opc == '105':
        if data[index + 1] != 0:
            index = data[data[index + 2]]
            return index
        else:
            return index + 3
    elif opc == '1005':
        if data[data[index + 1]] != 0:
            index = data[index + 2]
            return index
        else:
            return index + 3
    elif opc == '1105':
        if data[index + 1] != 0:
            index = data[index + 2]
            return index
        else:
            return index + 3
    elif opc == '6':
        if data[data[index + 1]] == 0:
            index = data[data[index + 2]]
            return index
        else:
            return index + 3
    elif opc == '106':
        if data[index + 1] == 0:
            index = data[data[index + 2]]
            return index
        else:
            return index + 3
    elif opc == '1006':
        if data[data[index + 1]] == 0:
            index = data[index + 2]
            return index
        else:
            return index + 3
    elif opc == '1106':
        if data[index + 1] == 0:
            index = data[index + 2]
            return index
        else:
            return index + 3
    elif opc == '7':
        if data[data[index + 1]] < data[data[index + 2]]:
            data[data[index + 3]] = 1
        else:
            data[data[index + 3]] = 0
    elif opc == '107':
        if data[index + 1] < data[data[index + 2]]:
            data[data[index + 3]] = 1
        else:
            data[data[index + 3]] = 0
    elif opc == '1007':
        if data[data[index + 1]] < data[index + 2]:
            data[data[index + 3]] = 1
        else:
            data[data[index + 3]] = 0
    elif opc == '1107':
        if data[index + 1] < data[index + 2]:
            data[data[index + 3]] = 1
        else:
            data[data[index + 3]] = 0
    elif opc == '8':
        if data[data[index + 1]] == data[data[index + 2]]:
            data[data[index + 3]] = 1
        else:
            data[data[index + 3]] = 0
    elif opc == '108':
        if data[index + 1] == data[data[index + 2]]:
            data[data[index + 3]] = 1
        else:
            data[data[index + 3]] = 0
    elif opc == '1008':
        if data[data[index + 1]] == data[index + 2]:
            data[data[index + 3]] = 1
        else:
            data[data[index + 3]] = 0
    elif opc == '1108':
        if data[index + 1] == data[index + 2]:
            data[data[index + 3]] = 1
        else:
            data[data[index + 3]] = 0
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
