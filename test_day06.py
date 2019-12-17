from unittest import TestCase
import day06

class Test(TestCase):
    def test_direct_orbits(self):
        data = ['COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K', 'K)L']
        centres = []
        direct_orbits_count, centres = day06.direct_orbits(data, centres)
        self.assertEqual(11, direct_orbits_count)
