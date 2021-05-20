import unittest


# 生成一个套件对象
# suite = unittest.TestLoader().discover(start_dir='.', pattern='test*.py')
from test_demoa import TestDemoAdd

suite = unittest.TestSuite()
suite.addTest(TestDemoAdd('test_add01'))

runner = unittest.TextTestRunner()
runner.run(suite)