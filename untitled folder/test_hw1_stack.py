import unittest
from itertools import permutations

class TestStackPermutations(unittest.TestCase):
        
    def test_legal(self):
        p1 = [3, 2, 4, 1, 0]
        result = stackPermutationTrace(5, p1)
        ans1 = ['push', 'push', 'push', 'pass', 'pop', 'pass', 'pop', 'pop']
        ans2 = ['push', 'push', 'push', 'push', 'pop', 'pop', 'push', 'pop', 'pop', 'pop']
        self.assertTrue(result==ans1 or result==ans2)
        
    def test_illegal(self):
        p1 = [4, 2, 3, 1, 0]
        result = stackPermutationTrace(5, p1)
        self.assertTrue(result==['stuck'])
                       
suite = unittest.TestLoader().loadTestsFromTestCase(TestStackPermutations)
unittest.TextTestRunner().run(suite)
