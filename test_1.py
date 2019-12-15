from unittest import TestCase

main = __import__('1')


class Test(TestCase):
    def test_find_fuel(self):
        self.assertEqual(main.findFuel(12), 2)

        self.assertEqual(main.findFuel(14), 2)

        self.assertEqual(main.findFuel(1969), 654)

        self.assertEqual(main.findFuel(100756), 33583)


class Test(TestCase):
    def test_additional_fuel(self):
        self.assertEqual(2, main.additional_fuel(14))

        self.assertEqual(966, main.additional_fuel(1969))
