# !/usr/bin/env python
# encoding: utf-8
import unittest
import source


class mytest(unittest.TestCase):
    def test(self):
        self.assertEqual(source.f_1d97cca(1,2,3,4,5,6,7),8,'fail')
if __name__ == '__main__':
    unittest.main()