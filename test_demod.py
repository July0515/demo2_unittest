import unittest
from parameterized import parameterized
# 加法操作



def add(x,y):
    z = x + y
    return z


# # 最原始的测试方式
# print(add(3, 4) == 7)
# print(add(3, 4) == None)
# print(add(1.2, 4.5) == 5.7)

version = 1.2
class TestDemoAdd(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls) -> None:
    #     print("===========执行setupClass方法==========")
    #
    # @classmethod
    # def tearDownClass(cls) -> None:
    #     print("===========执行tearDownClass方法==========")
    #
    # def setUp(self) -> None:
    #     print("===========执行setup方法==========")
    #
    # def tearDown(self) -> None:
    #     print("=========执行tearDowm方法=========")

    # data = [(7, 3, 4), (4, 0, 4), (1, -3, 4), (7.7, 3.7, 4)]

    # def build_data():
    #     return [(7, 3, 4), (4, 0, 4), (1, -3, 4), (7.7, 3.7, 4)]
    #
    # @parameterized.expand(build_data)
    # def test_add(self, c, a, b):
    #     res = add(a, b)
    #     self.assertEqual(c, res)

    def test_add01(self):
        print("=========执行test_add01=========")
        res1 = add(3, 4)
        self.assertEqual(7, res1)

    @unittest.skip('此用例发现了问题，暂时不测试')
    def test_add02(self):
        print("=========执行test_add02=========")
        res2 = add(0, 1)
        self.assertEqual(None, res2)

    @unittest.skipIf(version == 1.2, '运行当前测试用例')
    def test_add03(self):
        print("=========执行test_add03=========")
        res3 = add(-1, 3)
        self.assertEqual(2, res3)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestDemoAdd('test_add01'))
    runner = unittest.TextTestRunner()
    runner.run(suite)
