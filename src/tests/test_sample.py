
"""
This is the test suite for sample.py.
"""

from unittest import TestCase


from src.sample import main

SUCCESS = 0


class SampleTestCase(TestCase):
    def test_main(self):
        self.assertTrue(main() == SUCCESS)
