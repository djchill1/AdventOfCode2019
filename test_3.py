from unittest import TestCase

main = __import__('3')


class Test(TestCase):
    def test_calc_intersection(self):
        wireOne = ['R8', 'U5', 'L5', 'D3']
        wireTwo = ['U7', 'R6', 'D4', 'L4']
        self.assertEqual(6, main.calcIntersection(wireOne, wireTwo, 'shortestCrowFlies'))
        self.assertEqual(30, main.calcIntersection(wireOne, wireTwo, 'shortestWireLength'))

        wireOne = ['R75','D30','R83','U83','L12','D49','R71','U7','L72']
        wireTwo = ['U62','R66','U55','R34','D71','R55','D58','R83']
        self.assertEqual(159, main.calcIntersection(wireOne, wireTwo, 'shortestCrowFlies'))
        self.assertEqual(610, main.calcIntersection(wireOne, wireTwo, 'shortestWireLength'))
