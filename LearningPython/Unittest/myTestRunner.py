#!usr/bin/env python
#-*-coding:utf-8-*-
import unittest
import unittest_ddt
case = unittest.TestLoader().loadTestsFromTestCase(unittest_ddt.TestDemo)
mysuite=unittest.TestSuite([case])
myrunner = unittest.TextTestRunner(verbosity=2)
myrunner.run(mysuite)