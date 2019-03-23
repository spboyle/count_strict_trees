#!/usr/bin/env python

from importlib import import_module
import sys
import time
import unittest

# unittest.TestLoader.sortTestMethodsUsing = lambda _s, x, y: 0
# unittest.TestLoader.sortTestMethodsUsing = None

from recursive_memo import count_strict_trees


# if len(sys.argv) < 2:
#     raise Exception("Name the file you want to test.")

# import ipdb; ipdb.set_trace()
# module = import_module(sys.argv.pop().replace('alg=', ''))
# count_strict_trees = module.count_strict_trees


class StrictTreesTest(unittest.TestCase):

    def setUp(self):
        self._start = time.time()

    def tearDown(self):
        print('{}s'.format(round(time.time() - self._start, 4)))

    def test_Y_with_N1_K_1(self):
        result = count_strict_trees(n=1, k=1)
        self.assertEqual(result, 1)

    def test_Z_with_N3_K_2(self):
        result = count_strict_trees(n=3, k=2)
        self.assertEqual(result, 1)

    def test_a_with_N5_K_3(self):
        result = count_strict_trees(n=5, k=3)
        self.assertEqual(result, 2)

    def test_b_with_N9_K_4(self):
        result = count_strict_trees(n=9, k=4)
        self.assertEqual(result, 6)

    def test_c_with_N35_K_7(self):
        result = count_strict_trees(n=35, k=7)
        self.assertEqual(result, 5024)

    def test_d_with_N15_K_4(self):
        result = count_strict_trees(n=15, k=4)
        self.assertEqual(result, 1)

    def test_e_with_N75_K_47(self):
        result = count_strict_trees(n=75, k=47)
        self.assertEqual(result, 0)

    def test_f_with_N99_K_15(self):
        result = count_strict_trees(n=99, k=15)
        self.assertEqual(result, 2365)

    def test_g_with_N172_K_44(self):
        result = count_strict_trees(n=172, k=44)
        self.assertEqual(result, 0)

    def test_h_with_N165_K_65(self):
        result = count_strict_trees(n=165, k=65)
        self.assertEqual(result, 3470)

    def test_i_with_N177_K_57(self):
        result = count_strict_trees(n=177, k=57)
        self.assertEqual(result, 5010)

    def test_j_with_N198_K_56(self):
        result = count_strict_trees(n=198, k=56)
        self.assertEqual(result, 0)

    def test_k_with_N199_K_99(self):
        result = count_strict_trees(n=199, k=99)
        self.assertEqual(result, 1808)

    def test_l_with_N199_K_77(self):
        result = count_strict_trees(n=199, k=77)
        self.assertEqual(result, 3114)


unittest.main(verbosity=2)
