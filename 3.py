with open('3_input.txt') as f:
    wireOneDirections = f.readline().split(",")
    wireTwoDirections = f.readline().split(",")

print(wireOneDirections)


def calcStepPoints(path):
    tempx = tempy = step = 0
    directions = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}
    points = {}
    for item in path:
        dx, dy = directions[item[0]]
        for _ in range(int(item[1:])):
            tempx += dx
            tempy += dy
            step += 1
            if (tempx, tempy) not in points:
                points[(tempx, tempy)] = step
    return points


def calcIntersection(wireOne, wireTwo, operation):
    wireOnePoints = calcStepPoints(wireOne)
    wireTwoPoints = calcStepPoints(wireTwo)
    intersectionPoints = [point for point in wireOnePoints if point in wireTwoPoints]
    if operation == 'shortestCrowFlies':
        return min(abs(x) + abs(y) for (x, y) in intersectionPoints)
    if operation == 'shortestWireLength':
        return min(wireOnePoints[point] + wireTwoPoints[point] for point in intersectionPoints)


print('part 1 answer ', calcIntersection(wireOneDirections, wireTwoDirections, 'shortestCrowFlies'))
print('part 2 answer ', calcIntersection(wireOneDirections, wireTwoDirections, 'shortestWireLength'))
