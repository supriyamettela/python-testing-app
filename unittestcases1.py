import unittest
from multiply import multiplication
class multiplication(unittest.TestCase):

  def test_1(self):
       
    result =multiplication(3,400)
    self.asserEqual(result,1200)
    
 


if __name__=='__main__':
  unittest.main()
    
