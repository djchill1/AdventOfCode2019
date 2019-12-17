with open('6_input.txt') as fp:
    data = fp.read().splitlines()

#print(data)

def split_orbits(value):
    centre, orbiter = value.split(')')
    return centre, orbiter


def direct_orbits(map, centres):
    direct_orbits_count = []
    for i in map:
        centre, orbiter = split_orbits(i)
        if centre in centres:
            direct_orbits_count[centres.index(centre)] += 1
        else:
            centres.append(centre)
            direct_orbits_count.append(1)
    return sum(direct_orbits_count), centres

print('# direct orbits: ', direct_orbits(data, []))

def indirect_orbits(map, centres):
    indirect_orbits_count = []
    centres_all = []
    orbiters_all = []
    for i in map:
        centre, orbiter = split_orbits(i)
        centres_all.append(centre)
        orbiters_all.append(orbiter)
    for i in centres:
        current_centre = i
        if i in orbiters_all:
            index = centres_all[orbiters_all.index(i)]
            print(index)

        # centres here are now the orbiters
        # find the index of the centre of any orbits of current_object
        # add 1 to the indirect_orbits_count
        # find any of the new "centre"s centres.
        # continue until there are no more centres the "current_object" is orbiting.
        # move onto next item in centres.

indirect_orbits(data, [])