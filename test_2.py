from unittest import TestCase


main = __import__('2')

class Test(TestCase):
    def test_intcode(self):
        self.assertEqual(2, main.intcode([1,0,0,0,99]))

        self.assertEqual(2, main.intcode([2,3,0,3,99]))

        self.assertEqual(2, main.intcode([2,4,4,5,99,0]))

        self.assertEqual(30, main.intcode([1,1,1,4,99,5,6,0,99]))
