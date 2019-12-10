def previous_centrum(c):
    for i in range(len(data)):
        if data[i][1] == c:
            return data[i][0]


def find_path2com(c):
    current = c[0]
    path2com = list()
    path2com.append(c[0])
    while current != 'COM':
        current = previous_centrum(current)
        path2com.append(current)
    return path2com


def find_first_centrum(c):
    for centrum in data:
        if centrum[1] == c:
            return centrum
    exit('Can\'t find YOU')


if __name__ == '__main__':
    fi = open("day6_input.txt")
    sum_path = 0
    data = [tuple(x.split(')')) for x in fi.read().strip().split('\n')]
    you2com = find_path2com(find_first_centrum('YOU'))
    san2com = find_path2com(find_first_centrum('SAN'))
    common = set(you2com).intersection(set(san2com))
    minpath = 10000
    for item in common:
        if you2com.index(item) + san2com.index(item) < minpath:
            minpath = you2com.index(item) + san2com.index(item)
    print(minpath)







