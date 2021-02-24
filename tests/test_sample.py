
"""
This is the test suite for sample.py.
"""

from unittest import TestCase


from sample import main, other_func

SUCCESS = 0


class SampleTestCase(TestCase):
    def test_main(self):
        self.assertTrue(main() == SUCCESS)

    def test_other_func(self):
        self.assertEquals(other_func(7), 14)
