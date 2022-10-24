import unittest
from decimal import *

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(NumberRD("I"),1)
    def test2(self):
        self.assertEqual(NumberRD("II"),2)
    def test3(self):
        self.assertEqual(NumberRD("III"),3)
    def test4(self):
        self.assertEqual(NumberRD("IV"),4)
    def test5(self):
        self.assertEqual(NumberRD("VIII"),8)
    def test6(self):
        self.assertEqual(NumberRD("X"),10)
    def test7(self):
        self.assertEqual(NumberRD("XXXVII"),37)
    def test8(self):
        self.assertEqual(NumberRD("XLIV"),44)
    def test9(self):
        self.assertEqual(NumberRD("XCIX"),99)
    def test10(self):
        self.assertEqual(NumberRD("CCXXVI"),226)
    def test11(self):
        self.assertEqual(NumberRD("XXXX"),"Ese no es un numero romano")
    def test12(self):
        self.assertEqual(NumberRD("XXXXX"),"Ese no es un numero romano")
    def test13(self):
        self.assertEqual(NumberRD("XXXIX"),39)    
    def test14(self):
        self.assertEqual(NumberRD("La Campanita"),"Ese no es un numero romano")

if __name__ == "__main__": # pragma: no cover
    unittest.main()