import unittest
class Test(unittest.TestCase):
    u'''判断 a == b'''
    def test01(self):
        a = 1
        b = 1
        self.assertEqual(a, b)

    def test02(self):
        u'''判断 a in b'''
        a = "hello"
        b = "hello world!"
        self.assertIn(a, b)

    def test03(self):
        u'''判断 a is True'''
        a = True
        self.assertTrue(a)

    def test04(self):
        u'''失败案例'''
        a = "广州测试"
        b = "BensonMax"
        self.assertEqual(a, b, msg="失败原因:%s != %s"%(a,b))

if __name__ == "__main__":
    unittest.main()