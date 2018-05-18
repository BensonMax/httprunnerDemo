import unittest
import time
class Test(unittest.TestCase):
    def setUp(self):
        print ("start!")
    def tearDown(self):
        time.sleep(1)
        print ("end!")
    def test01(self):
        print ("执行测试用例 01")
    def test03(self):
        print ("执行测试用例 03")
    def test02(self):
        print ("执行测试用例 02")
    def addtest(self):
        print ("add 方法")
if __name__ == "__main__":
    unittest.main()