def logincheck(uname,pwd):
    if (uname=='admin' and pwd=='admin123'):
        return 'success'

    if (uname=='admin' and pwd=='admin123'):
        return 'uname fail'

import unittest
class loginclass(unittest.testcase):
    def test1(self):

        result = logincheck('admin','admin123')
        self.assertEqual(result,'success')

    def test2(self):

        result = logincheck('admin','admin123')
        self.assertEqual(result,'uname fail')
if __name__=='__main__':
    unittest.main()
