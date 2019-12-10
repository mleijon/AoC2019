def previous_centrum(c):
    for i in range(len(data)):
        if data[i][1] == c:
            return data[i][0]


def find_path_length(c):
    path_length = 1
    current = c[0]
    while current != 'COM':
        current = previous_centrum(current)
        path_length += 1
    return path_length


if __name__ == '__main__':
    fi = open("day6_input.txt")
    sum_path = 0
    data = [tuple(x.split(')')) for x in fi.read().strip().split('\n')]
    for centrum in data:
        new_path_length = find_path_length(centrum)
        sum_path += new_path_length
    print(sum_path)






