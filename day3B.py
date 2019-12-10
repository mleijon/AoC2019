def maketrack(start_point, move):
    stp_lst = []
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
        stp = (0, 0)
        exit('Unknown direction')
    for _ in range(move_size):
        new_location = tuple(sum(x) for x in zip(origin, stp))
        stp_lst.append(new_location)
        origin = new_location
    return [stp_lst, origin]


if __name__ == '__main__':
    positions = [set(), set()]
    total_track = [[], []]
    with open("day3_input.txt") as fi:
        path = fi.read().strip('\n').split('\n')
        for i in range(len(path)):
            path[i] = path[i].split(',')
    for count, steps in enumerate(path, start=0):
        start = (0, 0)
        for step in steps:
            (new_path, start) = maketrack(start, step)
            total_track[count] = total_track[count] + new_path
        positions[count] = set(total_track[count])
    common_positions = positions[0].intersection(positions[1])
    common_positions = list(common_positions)
    min_intersection = total_track[0].index(common_positions[0]) + \
                       total_track[1].index(common_positions[0])
    for intersection in common_positions:
        sum_intersection = total_track[0].index(intersection) + \
                           total_track[1].index(intersection)
        min_intersection = min(min_intersection, sum_intersection)
    print(min_intersection + 2)







