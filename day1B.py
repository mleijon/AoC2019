import math

if __name__ == '__main__':
    fuel = 0
    fuel_total = 0
    with open("day1_input.txt") as fi:
        for mass in fi:
            fuel = math.trunc(int(mass)/3) - 2
            fuel_add = math.trunc(int(fuel)/3) - 2
            while fuel_add > 0:
                fuel += fuel_add
                fuel_add = math.trunc(int(fuel_add)/3) - 2
            fuel_total += fuel
    print(fuel_total)
