from unittest import TestCase
import day07


class TestAmplifier_controller(TestCase):
    def test_amplifier_controller(self):
        data = [3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0]
        phases = day07.get_phase_settings([0, 1, 2, 3, 4], 5)
        output = day07.amplifier_controller(phases, data)
        self.assertEquals(43210, output)

    def test_amplifier_controller_2(self):
        data = [3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0]
        phases = day07.get_phase_settings([0, 1, 2, 3, 4], 5)
        output = day07.amplifier_controller(phases, data)
        self.assertEquals(54321, output)

    def test_amplifier_controller_3(self):
        data = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]
        phases = day07.get_phase_settings([0, 1, 2, 3, 4], 5)
        output = day07.amplifier_controller(phases, data)
        self.assertEquals(65210, output)