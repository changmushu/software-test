#第一次修改
# import unittest
# from test_mathfunc import TestMathFunc
#
# if __name__ == '__main__':
#     suite = unittest.TestSuite()
#
#     tests = [TestMathFunc("test_add"), TestMathFunc("test_minus"), TestMathFunc("test_divide")]
#     suite.addTests(tests)
#
#     runner = unittest.TextTestRunner(verbosity=2)
#     runner.run(suite)

#第二次修改
# import unittest
# from test_mathfunc import TestMathFunc
#
# if __name__ == '__main__':
#     suite = unittest.TestSuite()
#
#     tests = [TestMathFunc("test_add"), TestMathFunc("test_minus"), TestMathFunc("test_divide")]
#     suite.addTests(tests)
#     # 直接用addTest方法添加单个TestCase
#     suite.addTest(TestMathFunc("test_multi"))
#     # 用addTests + TestLoader
#     # loadTestsFromName()，传入'模块名.TestCase名'
#     suite.addTests(unittest.TestLoader().loadTestsFromName('test_mathfunc.TestMathFunc'))
#     suite.addTests(unittest.TestLoader().loadTestsFromNames(['test_mathfunc.TestMathFunc']))
#     # loadTestsFromTestCase()，传入TestCase
#     suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMathFunc))
#     runner = unittest.TextTestRunner(verbosity=2)
#     runner.run(suite)

#第三次修改，将控制台输出转到文本文件中
import unittest
from test_mathfunc import TestMathFunc

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMathFunc))

    with open('UnittestTextReport.txt', 'a') as f:
        runner = unittest.TextTestRunner(stream=f, verbosity=2)
        runner.run(suite)

