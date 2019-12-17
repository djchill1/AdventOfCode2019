with open('6_input.txt') as fp:
    data = fp.read().splitlines()


# print(data)

def split_orbits(value):
    centre, orbiter = value.split(')')
    return centre, orbiter


def all_objects(map):
    centres = []
    orbiters = []
    for value in map:
        centre, orbiter = split_orbits(value)
        centres.append(centre)
        orbiters.append(orbiter)
    all = list(set(centres + orbiters))
    return all


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


def indirect_orbits(map, centres):
    indirect_orbits_count = []
    centres_all = []
    orbiters_all = []
    all = all_objects(map)
    for i in map:
        centre, orbiter = split_orbits(i)
        centres_all.append(centre)
        orbiters_all.append(orbiter)

    for i in all:
        current_object = i
        if i in orbiters_all:
            current_object = centres_all[orbiters_all.index(i)]
            print('current object: ', current_object)
            while current_object in orbiters_all:
                current_object = centres_all[orbiters_all.index(current_object)]
                indirect_orbits_count.append(current_object)
    return len(indirect_orbits_count)

    # centres here are now the orbiters
    # find the index of the centre of any orbits of current_object
    # add 1 to the indirect_orbits_count
    # find any of the new "centre"s centres.
    # continue until there are no more centres the "current_object" is orbiting.
    # move onto next item in centres.


def total_orbits(map):
    direct, centres = direct_orbits(map, [])
    indirect = indirect_orbits(map, centres)
    return direct + indirect


def you_to_santa(map):
    dist_list = []
    for i in map:
        centre, orbiter = split_orbits(i)
        dist_list.append((centre, orbiter, 1))
    return dist_list


from collections import defaultdict


class Graph():
    def __init__(self):
        """
        self.edges is a dict of all possible next nodes
        e.g. {'X': ['A', 'B', 'C', 'E'], ...}
        self.weights has all the weights between two nodes,
        with the two nodes as a tuple as the key
        e.g. {('X', 'A'): 7, ('X', 'B'): 2, ...}
        """
        self.edges = defaultdict(list)
        self.weights = {}

    def add_edge(self, from_node, to_node, weight):
        # Note: assumes edges are bi-directional
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.weights[(from_node, to_node)] = weight
        self.weights[(to_node, from_node)] = weight


graph = Graph()


def edge_to_graph(data):
    for edge in you_to_santa(data):
        graph.add_edge(*edge)


# dijsktra code by Ben Keen.
# http://benalexkeen.com/implementing-djikstras-shortest-path-algorithm-with-python/

def dijsktra(graph, initial, end):
    # shortest paths is a dict of nodes
    # whose value is a tuple of (previous node, weight)
    shortest_paths = {initial: (None, 0)}
    current_node = initial
    visited = set()

    while current_node != end:
        visited.add(current_node)
        destinations = graph.edges[current_node]
        weight_to_current_node = shortest_paths[current_node][1]

        for next_node in destinations:
            weight = graph.weights[(current_node, next_node)] + weight_to_current_node
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, weight)
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, weight)

        next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
        if not next_destinations:
            return "Route Not Possible"
        # next node is the destination with the lowest weight
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])

    # Work back through destinations in shortest path
    path = []
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_paths[current_node][0]
        current_node = next_node
    # Reverse path
    path = path[::-1]
    return path


print('part a solution: ', total_orbits(data))


def part_2_solution(data):
    edge_to_graph(data)
    total = dijsktra(graph, 'YOU', 'SAN')
    print('path: ', total)
    print('len: ', len(total) - 3)
    return len(total) - 3
