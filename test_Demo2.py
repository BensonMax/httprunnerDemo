import unittest

class IntegerArithmeticTestCase(unittest.TestCase):
    def setUp(self):
        print("----------测试开始----------")

    def test01Minus(self):
        u'''测试减法'''
        print("测试减法正在执行")
        result = 8-7      #实际结果
        ExpectResult = 1  #期望结果
        self.assertEquals(result,ExpectResult)
        
    def test02Divide(self):
        u'''测试除法'''
        print("测试除法正在执行")
        result = 7/2
        ExceptResult = 3.5
        self.assertEquals(result,ExceptResult)

    def tearDown(self):
        print("-----------测试结束---------")

if __name__=="__main__":
    unittest.main()