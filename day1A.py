import math
if __name__ == '__main__':
    fuel = 0
    with open("day1_input.txt") as fi:
        for mass in fi:
            fuel += math.trunc(int(mass)/3) - 2
    print(fuel)