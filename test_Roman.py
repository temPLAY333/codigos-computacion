import unittest
from roman import roman_number

class PrimerTest(unittest.TestCase):
    def test_1(self):
        resultado = roman_number(1)
        self.assertEqual(resultado, "I")
    def test_2(self):
        resultado = roman_number(3)
        self.assertEqual(resultado, "III")
    def test_3(self):
        resultado = roman_number(4)
        self.assertEqual(resultado, "IV")    
    def test_4(self):
        resultado = roman_number(7)
        self.assertEqual(resultado, "VII")
    def test_5(self):
        resultado = roman_number(9)
        self.assertEqual(resultado, "IX")
    def test_6(self):
        resultado = roman_number(12)
        self.assertEqual(resultado, "XII")
    def test_7(self):
        resultado = roman_number(14)
        self.assertEqual(resultado, "XIV")
    def test_8(self):
        resultado = roman_number(19)
        self.assertEqual(resultado, "XIX")
    def test_9(self):
        resultado = roman_number(24)
        self.assertEqual(resultado, "XXIV")
    def test_10(self):
        resultado = roman_number(44)
        self.assertEqual(resultado, "XLIV")
    def test_11(self):
        resultado = roman_number(55)
        self.assertEqual(resultado, "LV")
    def test_12(self):
        resultado = roman_number(69)
        self.assertEqual(resultado, "LXIX")
    def test_13(self):
        resultado = roman_number(82)
        self.assertEqual(resultado, "LXXXII")
    def test_14(self):
        resultado = roman_number(99)
        self.assertEqual(resultado, "XCIX")
    def test_15(self):
        resultado = roman_number(182)
        self.assertEqual(resultado, "CLXXXII")
    def test_16(self):
        resultado = roman_number(269)
        self.assertEqual(resultado, "CCLXIX")
    def test_17(self):
        resultado = roman_number(399)
        self.assertEqual(resultado, "CCCXCIX")
    def test_18(self):
        resultado = roman_number(643)
        self.assertEqual(resultado, "DCXLIII")

if __name__ == '__main__': # pragma: no cover
    unittest.main()
