import unittest
from MaquinaCafe import Maquinita

class TestCafe (unittest.TestCase):
    def setUp(self):
        self.MC = Maquinita()

    def test_opciones(self):
        self.assertEqual(self.MC.opciones(), {0: "CafeSolo", 1: "CafeDoble", 2: "CafeLecheSolo", 3: "CafeLecheDoble", 4: "Chocolate", 5: "Capuchino", 6: "Te"})
    
    def test1_CafeSolo(self):
        self.assertEqual(self.MC.pedir(0, 1), True)

    def test2_CafeDoble(self):
        self.assertEqual(self.MC.pedir(1, 2), True)
        
    def test3_NoCoins(self):
        with self.assertRaises(Exception):
            self.MC.pedir(6, 2)
        self.assertEqual(self.MC.pedir(6, 4), True)

    def test4_NoCoffe(self):
        self.MC.cafe = 0
        with self.assertRaises(Exception):
            self.MC.pedir(2, 5)
        self.MC.cafe += 100
        self.assertEqual(self.MC.pedir(2, 5), True)

    def test5_NoMilk(self):
        self.MC.leche = 0
        with self.assertRaises(Exception):
            self.MC.pedir(3, 6)
        self.MC.leche += 100
        self.assertEqual(self.MC.pedir(3, 6), True)

    def test6_NoSugar(self):
        self.MC.azucar = 0
        with self.assertRaises(Exception):
            self.MC.pedir(4, 10)
        self.MC.azucar += 100
        self.assertEqual(self.MC.pedir(4, 10), True)    

    def test7_Money(self):
        self.assertEqual(self.MC.money, 0)

    def test8_NoChocolate(self):
        self.MC.chocolate = 0
        with self.assertRaises(Exception):
            self.MC.pedir(4, 10)
        self.MC.chocolate += 100
        self.assertEqual(self.MC.pedir(4, 10), True)       

    def test9_NoSugar(self):
        self.MC.azucar = 0
        self.assertEqual(self.MC.pedir(0, 1), True)
        with self.assertRaises(Exception):
            self.MC.ponerAzucar(15, 2)
        self.MC.azucar += 100
        self.assertEqual(self.MC.ponerAzucar(15, 3),True)

    def test10_NoSugar(self):
        self.assertEqual(self.MC.pedir(0, 1), True)
        with self.assertRaises(Exception):
            self.MC.ponerAzucar(45, 5)
        self.assertEqual(self.MC.ponerAzucar(15, 3),True)
    
    def test11_NoSugar(self):
        self.assertEqual(self.MC.pedir(0, 1), True)
        with self.assertRaises(Exception):
            self.MC.ponerAzucar(15, 0)
        self.assertEqual(self.MC.ponerAzucar(15, 3),True)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()