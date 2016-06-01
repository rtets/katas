import unittest
from heffassess import HeffAssess

class TestHeffAssess(unittest.TestCase):
    def test_heffassess(self):
        input = 'When not studying nuclear physics, Bambi likes to playbeach volleyball.'
        ha = HeffAssess()
        self.assertEqual('aaaaabbbbcccdeeeeeghhhiiiiklllllllmnnnnooopprsssstttuuvwyyyy',ha.assess(input))
