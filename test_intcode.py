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

