from unittest import TestCase

main = __import__('4')

class Test(TestCase):
    def test_not_more_adjacents(self):
        input = [112233]
        self.assertEqual(1, len(main.not_more_adjacents(input)))

        input = [123444]
        self.assertEqual(0, len(main.not_more_adjacents(input)))

        input = [111122]
        self.assertEqual(1, len(main.not_more_adjacents(input)))