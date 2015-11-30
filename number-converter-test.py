import unittest
import numeric_validators as nv
import string

class TestStringMethods(unittest.TestCase):
	
  def test_is_binary(self):
      self.assertTrue(nv.is_binary(10111))	
      
  def test_numeric_is_not_binary(self):
      self.assertFalse(nv.is_binary(12345))      
      
  def test_alpha_is_not_binary(self):
      self.assertFalse(nv.is_binary("abc")) 
      
  def test_alpha_lower_is_hex(self):
      self.assertTrue(nv.is_hex("abc"))                  

  def test_alpha_upper_is_hex(self):
      self.assertTrue(nv.is_hex("ABC"))                        

  def test_numeric_is_hex(self):
      self.assertTrue(nv.is_hex("123")) 
      
  def test_hex_from_list(self):
      self.assertTrue(nv.is_valid([str(x) for x in range(10)] + list(string.ascii_lowercase)[0:6], "123"))       

if __name__ == '__main__':
    unittest.main()