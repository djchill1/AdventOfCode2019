from unittest import TestCase
from unittest.mock import patch

import intcode


class Test(TestCase):
    def test_day02(self):
        self.assertEqual(2, intcode.intcode([1, 0, 0, 0, 99]))

        self.assertEqual(2, intcode.intcode([2, 3, 0, 3, 99]))

        self.assertEqual(2, intcode.intcode([2, 4, 4, 5, 99, 0]))

        self.assertEqual(30, intcode.intcode([1, 1, 1, 4, 99, 5, 6, 0, 99]))

    def test_day05(self):
        self.assertEqual(1, intcode.intcode([3, 0, 4, 0, 99]))
        ## requires input of 1


    def test_complex_day05(self):
        input = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
        output = intcode.intcode(input)
        print('received out ', output)
        self.assertEqual(999, output)
        ## requires input below 8.