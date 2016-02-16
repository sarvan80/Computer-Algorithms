import unittest

class TestMatrixMethods(unittest.TestCase):

    def setUp(self):
        self.m0 = Matrix(3,4)     # to check for initialization
        self.m1 = Matrix(3,4)
        self.m2 = Matrix(3,4)
        self.m3 = Matrix(4,3)
        for i in range(3):
            for j in range(4):
                self.m1.setitem(i, j, i+j)
                self.m2.setitem(i, j, i-j)                
                self.m3.setitem(j, i, (i+j)%2)

    def test_1_init(self):
        self.assertEqual(self.m0.getitem(2,2), 0)

    def test_2_shape(self):
        self.assertEqual(self.m1.shape(), (3,4))

    def test_3_setitem(self):
        self.assertRaises(IndexError, self.m1.setitem, 3, 2, -1)

    def test_getitem1(self):
        self.assertRaises(IndexError, self.m1.getitem, 3, 2)

    def test_getitem2(self):
        self.assertEqual(self.m1.getitem(1,2), 3)

    def test_getslice1(self):
        self.assertRaises(IndexError, self.m1.getslice, 1, 4, 0, 2)

    def test_getslice2(self):
        m = self.m1.getslice(1,3,1,3)
        a, b = m.getitem(0,0), m.getitem(1,1)
        self.assertEqual(a, 2)
        self.assertEqual(b, 4)
        
    def test_scaleBy(self):
        self.m1.scaleBy(3)
        self.assertEqual(self.m1.getitem(1,2), 9)

    def test_transpose(self):
        m = self.m1.transpose()
        self.assertEqual(m.shape(), (4,3))
        a, b = m.getitem(3,2), m.getitem(2,1)
        self.assertEqual(a, 5)
        self.assertEqual(b, 3)

    def test_add1(self):
        with self.assertRaises(TypeError):
            m = self.m1 + self.m3

    def test_add2(self):
        m = self.m1 + self.m2
        self.assertEqual(m.getitem(2,3), 4)
        self.assertEqual(m.getitem(1,2), 2)

    def test_sub1(self):
        with self.assertRaises(TypeError):
            m = self.m1 - self.m3

    def test_sub2(self):
        m = self.m1 - self.m2
        self.assertEqual(m.getitem(2,3), 6)
        self.assertEqual(m.getitem(1,2), 4)

    def test_mult1(self):
        with self.assertRaises(TypeError):
            m = self.m1 * self.m2

    def test_mult2(self):
        m = self.m1 * self.m3
        self.assertEqual(m.getitem(0,1), 2)
        self.assertEqual(m.getitem(2,2), 8)
        self.assertEqual(m.shape(), (3,3))

suite = unittest.TestLoader().loadTestsFromTestCase(TestMatrixMethods)
unittest.TextTestRunner().run(suite)
