lower_data = 134564
upper_data = 585159

possibilities = []

def distinct(x):
    # find distinct values in a list
    output = []
    for i in x:
        if i not in output:
            output.append(i)
    return output

def strictly_increasing(x):
    return all(x<=y for x, y in zip(x, x[1:]))

def find_increasing_in_range(lower, upper):
    possibilities = []
    for i in range(lower,upper):
        # check number is increasing
        list = [int(x) for x in str(i)]
        if strictly_increasing(list):
            possibilities.append(i)
    return distinct(possibilities)


def find_adjacent_doubles(list):
    possibilities = []
    # Check two adjacent digits are the same
    for i in list:
        list_number = [int(x) for x in str(i)]
        for j in range(0,len(list_number)-1):
            if list_number[j] == list_number[j+1]:
                possibilities.append(i)
    return distinct(possibilities)

def not_more_adjacents(list):
    possibilities = []
    for i in list:
        list_number = [int(x) for x in str(i)]
        # check number of occurances of each number, if one is exactly 2 then we're good
        for j in range(0,10):
            if list_number.count(j) == 2:
                possibilities.append(i)
    return distinct(possibilities)

out = find_increasing_in_range(lower_data,upper_data)
final = find_adjacent_doubles(out)
print('part 1 solution ', len(final))
part2 = not_more_adjacents(final)
print('part 2 solution ', len(part2))