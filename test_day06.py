from unittest import TestCase
import day06


class Test(TestCase):
    def test_direct_orbits(self):
        test_data = ['COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K', 'K)L']
        centres = []
        direct_orbits_count, centres = day06.direct_orbits(test_data, centres)
        self.assertEqual(11, direct_orbits_count)

    def test_total_orbits(self):
        test_data = ['COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K', 'K)L']
        total = day06.total_orbits(test_data)
        self.assertEqual(42, total)


class Test(TestCase):
    def test_you_to_santa(self):
        test_data = ['COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K', 'K)L', 'K)YOU', 'I)SAN']
        total = day06.you_to_santa(test_data)
        self.assertEqual(
            [('COM', 'B', 1), ('B', 'C', 1), ('C', 'D', 1), ('D', 'E', 1), ('E', 'F', 1), ('B', 'G', 1), ('G', 'H', 1),
             ('D', 'I', 1), ('E', 'J', 1), ('J', 'K', 1), ('K', 'L', 1), ('K', 'YOU', 1), ('I', 'SAN', 1)], total)


class Test(TestCase):
    def test_part_2_solution(self):
        test_data = ['COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K', 'K)L', 'K)YOU', 'I)SAN']
        total = day06.part_2_solution(test_data)
        self.assertEqual(4, total)
