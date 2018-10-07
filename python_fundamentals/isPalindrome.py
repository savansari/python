import unittest
def isPalindrome(x):
    i=0
    while i<int(len(x)/2) and x[i]==x[len(x)-1-i]:
        i+=1
    if i<int(len(x)/2):
        return False
    return True


class testIsPalindrome(unittest.TestCase):
    def testNull(self):
        self.assertEqual(isPalindrome(""),True)
        self.assertTrue(isPalindrome(""))

    def testNull(self):
        self.assertEqual(isPalindrome("1"),True)
        self.assertTrue(isPalindrome("1"))

    def testNull(self):
        self.assertEqual(isPalindrome("rabcr"),True)
        self.assertFalse(isPalindrome("rabcr"))

    def testNull(self):
        self.assertEqual(isPalindrome("racecar"),True)
        self.assertTrue(isPalindrome("racecar"))
   
    def setUp(self):
        print("Setting up...")
    def tearDown(self):
        print("Teraing Down...")
    
if __name__ == '__main__':
    unittest.main()

