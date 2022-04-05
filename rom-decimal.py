from itertools import count
import unittest

def NumberRD (a):
    if a.count("IIII") >= 1 or a.count("VV") >= 1 or a.count("XXXX") >= 1 or a.count("LL") >= 1:
        return "Ese no es un numero romano"
    if a.isupper == False or a.count(" ") >= 1:
        return "Ese no es un numero romano"
    numberD = 0
    numberD += a.count("I")
    numberD += a.count("V")*5
    numberD -= a.count("IV")*2
    numberD += a.count("X")*10
    numberD -= a.count("IX")*2
    numberD += a.count("L")*50
    numberD -= a.count("XL")*20
    numberD += a.count("C")*100
    numberD -= a.count("XC")*20
    numberD += a.count("D")*500
    numberD -= a.count("CD")*200
    numberD += a.count("M")*1000
    numberD -= a.count("CM")*200
    return numberD


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
    def test15(self):
        self.assertEqual(NumberRD("XCXXX"),"Ese no es un numero romano")
if __name__ == "__main__":
    unittest.main()
