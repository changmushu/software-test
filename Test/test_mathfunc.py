import unittest
from mathfunc import *

class TestDoWork(unittest.TestCase):
    def test_statement_coverage_1(self):
        self.assertEqual(DoWork(4, 3, 10), None)

    def test_statement_coverage_2(self):
        self.assertEqual(DoWork(2, 6, 5), None)

    def test_statement_coverage_3(self):
        self.assertEqual(DoWork(5, 2, 11), None)

    def test_decision_coverage_1(self):
        self.assertEqual(DoWork(4, 3, 10), None)

    def test_decision_coverage_2(self):
        self.assertEqual(DoWork(2, 6, 5), None)

    def test_decision_coverage_3(self):
        self.assertEqual(DoWork(5, 2, 11), None)

    def test_condition_coverage_1(self):
        self.assertEqual(DoWork(4, 3, 10), None)

    def test_condition_coverage_2(self):
        self.assertEqual(DoWork(2, 6, 5), None)

    def test_condition_coverage_3(self):
        self.assertEqual(DoWork(5, 2, 11), None)

    def test_decision_condition_coverage_1(self):
        self.assertEqual(DoWork(4, 3, 10), None)

    def test_decision_condition_coverage_2(self):
        self.assertEqual(DoWork(2, 6, 5), None)

    def test_decision_condition_coverage_3(self):
        self.assertEqual(DoWork(5, 2, 9), None)

    def test_path_coverage_1(self):
        self.assertEqual(DoWork(4, 3, 10), None)

    def test_path_coverage_2(self):
        self.assertEqual(DoWork(2, 6, 5), None)

    def test_path_coverage_3(self):
        self.assertEqual(DoWork(5, 2, 11), None)


