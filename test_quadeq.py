from msilib.schema import Class
import unittest
import quadeq

class TestQuad(unittest.TestCase):
    def test_solution(self):
        self.assertCountEqual(quadeq.QuadEq(1,4,4).solution(),[-2,-2])
        self.assertCountEqual(quadeq.QuadEq(2,3,4).solution(),[(-0.75+1.1989578808281798j), (-0.75-1.1989578808281798j)])


