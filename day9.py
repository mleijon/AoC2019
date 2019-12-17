def operation(opc, index):
    global relative_base
    opc = opc.zfill(5)
    mode = opc[:3]
    if opc == '00099':
        exit(0)
    if mode in ['000', '100', '200']:
        op1 = data[data[index + 1]]
        op2 = data[data[index + 2]]
    elif mode in ['001', '101', '201']:
        op1 = data[index + 1]
        op2 = data[data[index + 2]]
    elif mode in ['010', '110', '210']:
        op1 = data[data[index + 1]]
        op2 = data[index + 2]
    elif mode in ['011', '111', '211']:
        op1 = data[index + 1]
        op2 = data[index + 2]
    elif mode in ['002', '102', '202']:
        op1 = data[data[index + 1] + relative_base]
        op2 = data[data[index + 2]]
    elif mode in ['020', '120', '220']:
        op2 = data[data[index + 1]]
        op1 = data[data[index + 2] + relative_base]
    elif mode in ['022', '122', '222']:
        op1 = data[data[index + 1] + relative_base]
        op2 = data[data[index + 2] + relative_base]
    elif mode in ['012', '112', '212']:
        op1 = data[data[index + 1] + relative_base]
        op2 = data[index + 2]
    elif mode in ['021', '121', '221']:
        op1 = data[index + 1]
        op2 = data[data[index + 2] + relative_base]
    else:
        exit('Operation mode {} unknown. Exits.'.format(mode))
    if opc[4] == '1':
        if mode[0] == '0':
            data[data[index + 3]] = op1 + op2
        elif mode[0] == '1':
            data[index + 3] = op1 + op2
        elif mode[0] == '2':
            data[data[index + 3] + relative_base] = op1 + op2
    elif opc[4] == '2':
        if mode[0] == '0':
            data[data[index + 3]] = op1*op2
        elif mode[0] == '1':
            data[index + 3] = op1*op2
        elif mode [0] == '2':
            data[data[index + 3] + relative_base] = op1 *op2
    elif opc[4] == '3':
        print('Enter a value:')
        if mode == '000':
            data[data[index + 1]] = int(input())
        elif mode == '001':
            data[index + 1] = int(input())
        elif mode == '002':
            data[data[index + 1] + relative_base] = int(input())
    elif opc[4] == '9':
        if mode == '000':
            relative_base += data[data[index + 1]]
        elif mode == '001':
            relative_base += data[index + 1]
        elif mode == '002':
            relative_base += data[data[index + 1] + relative_base]
    elif opc[4] == '4':
        if mode == '000':
            print(data[data[index + 1]])
        elif mode == '001':
            print(data[index + 1])
        elif mode == '002':
            print(data[data[index + + 1] + relative_base])
    elif opc[4] == '5':
        if op1 != 0:
            index = op2
            return index
        else:
            return index + 3
    elif opc[4] == '6':
        if op1 == 0:
            index = op2
            return index
        else:
            return index + 3
    elif opc[4] == '7':
        if op1 < op2:
            if mode[0] == '0':
                data[data[index + 3]] = 1
            elif mode[0] == '1':
                data[index +3] = 1
            elif mode[0] == '2':
                data[data[index + 3] + relative_base] = 1
        else:
            if mode[0] == '0':
                data[data[index + 3]] = 0
            elif mode[0] == '1':
                data[index +3] = 0
            elif mode[0] == '2':
                data[data[index + 3] + relative_base] = 0
    elif opc[4] == '8':
        if op1 == op2:
            if mode[0] == '0':
                data[data[index + 3]] = 1
            elif mode[0] == '1':
                data[index +3] = 1
            elif mode[0] == '2':
                data[data[index + 3] + relative_base] = 1
        else:
            if mode[0] == '0':
                data[data[index + 3]] = 0
            elif mode[0] == '1':
                data[index +3] = 0
            elif mode[0] == '2':
                data[data[index + 3] + relative_base] = 0
    else:
        exit('opcode {} unknown'.format(opcode))
    if opc[4] in ['3', '4', '9']:
        index += 2
        return index
    else:
        index += 4
        return index


global relative_base
if __name__ == '__main__':
    fi = open("day9_input.txt")
    data = list(map(int, fi.read().split(','))) + [0]*10000000
    index = 0
    relative_base = 0
    opcode = data[index]
    while True:
        new_index = operation(str(opcode), index)
        index = new_index
        opcode = data[index]
