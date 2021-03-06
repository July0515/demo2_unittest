

# 加法操作
import unittest


def add(x,y):
    z = x + y
    return z


# # 最原始的测试方式
# print(add(3, 4) == 7)
# print(add(3, 4) == None)
# print(add(1.2, 4.5) == 5.7)


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

    def test_add01(self):
        print("=========执行test_add01=========")
        self.assertEqual(7, add(3, 4))

    def test_add02(self):
        print("=========执行test_add02=========")
        self.assertEqual(None, add(3, 5))

    def test_add03(self):
        print("=========执行test_add03=========")
        self.assertEqual(5.7, add(1.2, 4.5))


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestDemoAdd('test_add01'))
    runner = unittest.TextTestRunner()
    runner.run(suite)
