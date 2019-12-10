def makepath(start_point, move):
    stp_set = set()
    stp = ()
    move_direction = move[0]
    move_size = int(move[1:])
    origin = start_point
    if move_direction == 'R':
        stp = (0, 1)
    elif move_direction == 'L':
        stp = (0, -1)
    elif move_direction == 'U':
        stp = (1, 0)
    elif move_direction == 'D':
        stp = (-1, 0)
    else:
        exit('Unknown direction')
    for _ in range(move_size):
        new_location = tuple(sum(x) for x in zip(origin, stp))
        stp_set.add(new_location)
        origin = new_location
    return [stp_set, origin]


def manhattan_distance(coord):
    return abs(coord[0]) + abs(coord[1])


if __name__ == '__main__':
    positions = [set(), set()]
    with open("day3_input.txt") as fi:
        path = fi.read().strip('\n').split('\n')
        for i in range(len(path)):
            path[i] = path[i].split(',')
    for count, steps in enumerate(path):
        start = (0, 0)
        for step in steps:
            (new_path, start) = makepath(start, step)
            positions[count] = positions[count].union(new_path)
    common_positions = positions[0].intersection(positions[1])
    min_distance = manhattan_distance(next(iter(common_positions)))
    for item in common_positions:
        if manhattan_distance(item) < min_distance:
            min_distance = manhattan_distance(item)
    print(min_distance)





