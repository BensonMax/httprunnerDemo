import unittest

class IntegerArithmeticTestCase(unittest.TestCase):
    def testAdd(self):
        u'''测试加法用例'''
        self.assertEquals((1+2),3)
        self.assertEquals(0+1,1)
    def testMultiply(self):
        u'''测试减法用例'''
        self.assertEquals((0*10),0)
        self.assertEqual((5*8),40)

if __name__=="__main__":
    unittest.main()

'''
1.第一行是导入 unittest 这个模块
2.class 这一行是定义一个测试的类，并继承 unittest.TestCase 这个类
3.接下来是定义了两个测试 case 名称:testAdd 和 testMultiply
4.注释里面有句话很重要，这个要敲下黑板记笔记了：## test method names begin 'test*'
--翻译：测试用例的名称要以 test 开头
5.然后是断言 assert，这里的断言方法是 assertEqual-判断两个是否相等，这个断言可以是一个也可以
是多个
6.if 下面的这个 unittest.main()是运行主函数，运行后会看到测试结果（跑了两个用例耗时 0.000 秒,两
个用例都通过）：
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s
OK
'''