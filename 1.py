with open('1_input.txt') as fp:
    data = fp.read().splitlines()

import math

def findFuel(x):
    return int(math.trunc(x/3) - 2)

fuel_vals = []
for i in data:
    fuel_vals.append(findFuel(int(i)))

print('part 1 answer ', sum(fuel_vals))


def additional_fuel(x):
    new_fuel = findFuel(x)
    total_fuel = new_fuel
    while True:
        new_fuel = findFuel(new_fuel)
        if new_fuel > 0:
            total_fuel += new_fuel
        else:
            return total_fuel

final_fuel = 0

for i in data:
    final_fuel += additional_fuel(int(i))
print('part 2 answer ', final_fuel)
