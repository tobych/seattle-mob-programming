import unittest


class SomeTests(unittest.TestCase):
    
    def test_something(self):
        self.assertEquals(0, 1)
    

if __name__ == "__main__":
    unittest.main()
