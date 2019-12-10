if __name__ == '__main__':
    with open("day2_input.txt") as fi:
        data = list(map(int, fi.read().split(',')))
    last_index = len(data) - 1
    data_org = data.copy()
    for data[1] in range(0, 100):
        data_org_1 = data.copy()
        for data[2] in range(0, 100):
            opcode = 0
            counter = 0
            while counter <= last_index:
                opcode = data[counter]
                if opcode == 1:
                    data[data[counter + 3]] = data[data[counter + 1]] + \
                                              data[data[counter + 2]]
                elif opcode == 2:
                    data[data[counter + 3]] = data[data[counter + 1]] * \
                                              data[data[counter + 2]]
                elif opcode == 99 and data[0] == 19690720:
                    print(100*data[1] + data[2])
                    exit(0)
                else:
                    data = data_org_1.copy()
                    break
                counter += 4
            data = data_org_1.copy()
        data = data_org.copy()
