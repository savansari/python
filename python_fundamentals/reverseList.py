import unittest
def reverseList(x):
    
    pass
    #for i in range(int(len(x)/2)):
    #   x[i],x[len(x)-i-1]=x[len(x)-i-1],x[i]
    #return x
    
class IsReverseList(unittest.TestCase):
    def testNull(self):
        self.assertEqual(reverseList([]),[])

    def testSame(self):
        self.assertEqual(reverseList([1,1,1]),[1,1,1])

    def testFull(self):
        self.assertEqual(reverseList([1,8,2,6,4,6]),[6,4,6,2,8,1])

    def setUp(self):
        print("\n Unit Test is Starting...\n")

    def tearDown(self):
        print("Running TearDown...")

if __name__ == '__main__':
    unittest.main()