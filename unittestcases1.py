import unittest
from multiply import multiplication
class multiplication(unittest.testcase1):

  def test_1(self):
    
    result =multiplication(3,400)
    self.asserEqual(result,1200)
  def test_2(self):

    result =multiplication(-3,4)
    self.asserEqual(result,-12)
  def test_3(self):

    result =multiplication(-3,-4)
    self.asserEqual(result,12)

if __name__=='__main__':
  unittest.main()
    
