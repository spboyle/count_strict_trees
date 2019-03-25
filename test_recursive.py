#!/usr/bin/env python

import time
import unittest

from recursive import count_strict_trees


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
        expected = 1707996
        self.assertEqual(result, 1707996)

    def test_d_with_N15_K_4(self):
        result = count_strict_trees(n=15, k=4)
        self.assertEqual(result, 1)

    def test_e_with_N75_K_47(self):
        result = count_strict_trees(n=75, k=47)
        self.assertEqual(result, 0)

    def test_f_with_N99_K_15(self):
        result = count_strict_trees(n=99, k=15)
        expected = 22729036112064713000946176
        self.assertEqual(result, expected)

    def test_g_with_N172_K_44(self):
        result = count_strict_trees(n=172, k=44)
        self.assertEqual(result, 0)

    def test_h_with_N165_K_65(self):
        result = count_strict_trees(n=165, k=65)
        self.assertEqual(result, 121504704165532482317209524552641544192)

    def test_i_with_N177_K_57(self):
        result = count_strict_trees(n=177, k=57)
        expected = 1084387921879907686960966467476228135840645120
        self.assertEqual(result, expected)

    def test_j_with_N198_K_56(self):
        result = count_strict_trees(n=198, k=56)
        self.assertEqual(result, 0)

    def test_k_with_N199_K_99(self):
        result = count_strict_trees(n=199, k=99)
        expected = 15291035365253017155553982414848
        self.assertEqual(result, expected)

    def test_l_with_N199_K_77(self):
        result = count_strict_trees(n=199, k=77)
        expected = 62999606927580161322700338643186028813263831040
        self.assertEqual(result, expected)

unittest.main(verbosity=2)
