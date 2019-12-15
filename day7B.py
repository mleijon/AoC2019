def all_comb(phases):
    c = []
    for i in phases:
        for j in phases - {i}:
            for k in phases - {i, j}:
                for l in phases - {i, j, k}:
                    for m in phases - {i, j, k, l}:
                        c.append(str(i) + str(j) + str(k) + str(l) + str(m))
    return c


def run_amp(phases):
    def operation(opc):
        nonlocal phase
        nonlocal inpp
        nonlocal amp
        nonlocal send_signal
        if opc == '1':
            data[amp][data[amp][index[amp] + 3]] = data[amp][data[amp][index[amp] + 1]] + data[amp][data[amp][index[amp] + 2]]
        elif opc == '2':
            data[amp][data[amp][index[amp] + 3]] = data[amp][data[amp][index[amp] + 1]] * data[amp][data[amp][index[amp] + 2]]
        elif opc == '101':
            data[amp][data[amp][index[amp] + 3]] = data[amp][index[amp] + 1] + data[amp][data[amp][index[amp] + 2]]
        elif opc == '102':
            data[amp][data[amp][index[amp] + 3]] = data[amp][index[amp] + 1] * data[amp][data[amp][index[amp] + 2]]
        elif opc == '1001':
            data[amp][data[amp][index[amp] + 3]] = data[amp][data[amp][index[amp] + 1]] + data[amp][index[amp] + 2]
        elif opc == '1002':
            data[amp][data[amp][index[amp] + 3]] = data[amp][data[amp][index[amp] + 1]] * data[amp][index[amp] + 2]
        elif opc == '1101':
            data[amp][data[amp][index[amp] + 3]] = data[amp][index[amp] + 1] + data[amp][index[amp] + 2]
        elif opc == '1102':
            data[amp][data[amp][index[amp] + 3]] = data[amp][index[amp] + 1] * data[amp][index[amp] + 2]
        elif opc in '3':
            if inpp == 0 and count <= 5:
                data[amp][data[amp][index[amp] + 1]] = phase
                inpp = 1
            else:
                data[amp][data[amp][index[amp] + 1]] = amp_input[amp]
                inpp = 0
        elif opc in ['4', '104']:
            send_signal = True
            if amp < 4:
                amp_input[amp + 1] = data[amp][data[amp][index[amp] + 1]]
            else:
                amp_input[0] = data[amp][data[amp][index[amp] + 1]]
        elif opc == '5':
            if data[amp][data[amp][index[amp] + 1]] != 0:
                index[amp] = data[amp][data[amp][index[amp] + 2]]
                return index[amp]
            else:
                return index[amp] + 3
        elif opc == '105':
            if data[amp][index[amp] + 1] != 0:
                index[amp] = data[amp][data[amp][index[amp] + 2]]
                return index[amp]
            else:
                return index[amp] + 3
        elif opc == '1005':
            if data[amp][data[amp][index[amp] + 1]] != 0:
                index[amp] = data[amp][index[amp] + 2]
                return index[amp]
            else:
                return index[amp] + 3
        elif opc == '1105':
            if data[amp][index[amp] + 1] != 0:
                index[amp] = data[amp][index[amp] + 2]
                return index[amp]
            else:
                return index[amp] + 3
        elif opc == '6':
            if data[amp][data[amp][index[amp] + 1]] == 0:
                index[amp] = data[amp][data[amp][index[amp] + 2]]
                return index[amp]
            else:
                return index[amp] + 3
        elif opc == '106':
            if data[amp][index[amp] + 1] == 0:
                index[amp] = data[amp][data[amp][index[amp] + 2]]
                return index[amp]
            else:
                return index[amp] + 3
        elif opc == '1006':
            if data[amp][data[amp][index[amp] + 1]] == 0:
                index[amp] = data[amp][index[amp] + 2]
                return index[amp]
            else:
                return index[amp] + 3
        elif opc == '1106':
            if data[amp][index[amp] + 1] == 0:
                index[amp] = data[amp][index[amp] + 2]
                return index[amp]
            else:
                return index[amp] + 3
        elif opc == '7':
            if data[amp][data[amp][index[amp] + 1]] < data[amp][data[amp][index[amp] + 2]]:
                data[amp][data[amp][index[amp] + 3]] = 1
            else:
                data[amp][data[amp][index[amp] + 3]] = 0
        elif opc == '107':
            if data[amp][index[amp] + 1] < data[amp][data[amp][index[amp] + 2]]:
                data[amp][data[amp][index[amp] + 3]] = 1
            else:
                data[amp][data[amp][index[amp] + 3]] = 0
        elif opc == '1007':
            if data[amp][data[amp][index[amp] + 1]] < data[amp][index[amp] + 2]:
                data[amp][data[amp][index[amp] + 3]] = 1
            else:
                data[amp][data[amp][index[amp] + 3]] = 0
        elif opc == '1107':
            if data[amp][index[amp] + 1] < data[amp][index[amp] + 2]:
                data[amp][data[amp][index[amp] + 3]] = 1
            else:
                data[amp][data[amp][index[amp] + 3]] = 0
        elif opc == '8':
            if data[amp][data[amp][index[amp] + 1]] == data[amp][data[amp][index[amp] + 2]]:
                data[amp][data[amp][index[amp] + 3]] = 1
            else:
                data[amp][data[amp][index[amp] + 3]] = 0
        elif opc == '108':
            if data[amp][index[amp] + 1] == data[amp][data[amp][index[amp] + 2]]:
                data[amp][data[amp][index[amp] + 3]] = 1
            else:
                data[amp][data[amp][index[amp] + 3]] = 0
        elif opc == '1008':
            if data[amp][data[amp][index[amp] + 1]] == data[amp][index[amp] + 2]:
                data[amp][data[amp][index[amp] + 3]] = 1
            else:
                data[amp][data[amp][index[amp] + 3]] = 0
        elif opc == '1108':
            if data[amp][index[amp] + 1] == data[amp][index[amp] + 2]:
                data[amp][data[amp][index[amp] + 3]] = 1
            else:
                data[amp][data[amp][index[amp] + 3]] = 0
        elif opc == '99':
            amp_quit[amp] = True
            print('quitting amp: {}'.format(amp))
        else:
            exit('opcode {} unknown'.format(opc))
        if opc in ['3', '4', '104']:
            index[amp] += 2
            return index[amp]
        else:
            index[amp] += 4
            return index[amp]

    count = 0
    while not amp_quit[4]:
        for amp in range(5):
            count += 1
            send_signal = False
            inpp = 0
            opcode = data[amp][index[amp]]
            phase = phases[amp]
            while not send_signal:
                new_index = operation(str(opcode))
                if send_signal or amp_quit[amp]:
                    break
                index[amp] = new_index
                opcode = data[amp][index[amp]]
    return amp_input[0]


if __name__ == '__main__':
    with open("day7_input.txt") as fi:
        data_org = list(map(int, fi.read().split(',')))
        amp_out_max = 0
    for comb in all_comb({5, 6, 7, 8, 9}):
        data = []
        for i in range(5):
            data.append(data_org.copy())
        index = [0] * 5
        amp_input = [0] * 6
        amp_quit = [False] * 5
        new_amp_input = run_amp(list(map(int, list(comb))))
        if new_amp_input > amp_out_max:
            amp_out_max = new_amp_input
    print(amp_out_max)
