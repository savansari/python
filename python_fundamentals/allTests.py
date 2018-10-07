import unittest
from myHomework import reverseList, isPalindrome,payInCoins,Fib,Factorial

class IsReverseList(unittest.TestCase):
    def testNull(self):
        return self.assertEqual(reverseList([]),[])

    def testSame(self):
        return self.assertEqual(reverseList([1,1,1]),[1,1,1])

    def testFull(self):
        return self.assertEqual(reverseList([1,8,2,6,4,6]),[6,4,6,2,8,1])

    def setUp(self):
        print("\n Unit Test is Starting...\n")

    def tearDown(self):
        print("Running TearDown...")

class testIsPalindrome(unittest.TestCase):
    def testNull(self):
        return self.assertEqual(isPalindrome(""),True)
        #return self.assertTrue(isPalindrome(""))

    def testNull(self):
        return self.assertEqual(isPalindrome("1"),True)
        return self.assertTrue(isPalindrome("1"))

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

class testCoins(unittest.TestCase):
    def testNull(self):
        self.assertEqual(payInCoins(0),[0,0,0,0])
    def testSame(self):
        self.assertEqual(payInCoins(1),[0,0,0,1])
        self.assertEqual(payInCoins(5),[0,0,1,0])
        self.assertEqual(payInCoins(10),[0,1,0,0])
        self.assertEqual(payInCoins(25),[1,0,0,0])
    def testFull(self):
        self.assertEqual(payInCoins(99),[3,2,0,4])
        self.assertEqual(payInCoins(91),[3,1,1,1])
        self.assertEqual(payInCoins(76),[3,0,0,1])

    def setUp(self):
        print("\n Unit Test is Starting...\n")

    def tearDown(self):
        print("Running TearDown...")

class testFib(unittest.TestCase):
    def testNull(self):
        self.assertEqual(Fib(0),0)
        self.assertEqual(Fib(1),1)
    def testSame(self):
        self.assertEqual(Fib(2),1)
        self.assertEqual(Fib(5),5)
        self.assertEqual(Fib(-1),0)
    

    def setUp(self):
        print("\n Unit Test is Starting...\n")

    def tearDown(self):
        print("Running TearDown...")

class testfact(unittest.TestCase):
    def testNull(self):
        self.assertEqual(Factorial(0),0)
    def testSame(self):
        self.assertEqual(Factorial(1),1)
        self.assertEqual(Factorial(3),6)
        self.assertEqual(Factorial(-1),0)
        self.assertEqual(Factorial(4),24)

    def setUp(self):
        print("\n Unit Test is Starting...\n")

    def tearDown(self):
        print("Running TearDown...")

if __name__ == '__main__':
    unittest.main()