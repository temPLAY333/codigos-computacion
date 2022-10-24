import unittest
from MaquinaCafe import Maquinita

maquinaCafe = Maquinita()

class TestCafe (unittest.TestCase):
    def test_opciones(self):
        self.assertEqual(maquinaCafe.opciones(), {0: "CafeSolo", 1: "CafeDoble", 2: "CafeLecheSolo", 3: "CafeLecheDoble", 4: "Chocolate", 5: "Capuchino", 6: "Te"})
    
    def test1_CafeSolo(self):
        self.assertEqual(maquinaCafe.pedir(0, 1), True)

    def test2_CafeDoble(self):
        self.assertEqual(maquinaCafe.pedir(1, 2), True)
        
    def test3_NoCoins(self):
        with self.assertRaises(Exception):
            maquinaCafe.pedir(6, 2)
        self.assertEqual(maquinaCafe.pedir(6, 4), True)

    def test4_NoCoffe(self):
        maquinaCafe.cafe = 0
        with self.assertRaises(Exception):
            maquinaCafe.pedir(2, 5)
        maquinaCafe.cafe += 100
        self.assertEqual(maquinaCafe.pedir(2, 5), True)

    def test5_NoMilk(self):
        maquinaCafe.leche = 0
        with self.assertRaises(Exception):
            maquinaCafe.pedir(3, 6)
        maquinaCafe.leche += 100
        self.assertEqual(maquinaCafe.pedir(3, 6), True)

    def test6_Money(self):
        self.assertEqual(maquinaCafe.money, 18)

    def test7_NoChocolate(self):
        maquinaCafe.chocolate = 0
        with self.assertRaises(Exception):
            maquinaCafe.pedir(4, 10)
        maquinaCafe.chocolate += 100
        self.assertEqual(maquinaCafe.pedir(4, 10), True)       

    def test8_NoSugar(self):
        maquinaCafe.azucar = 0
        self.assertEqual(maquinaCafe.pedir(0, 1), True)
        with self.assertRaises(Exception):
            maquinaCafe.ponerAzucar(15, 2)
        maquinaCafe.azucar += 100
        self.assertEqual(maquinaCafe.ponerAzucar(15, 3),True)


if __name__ == '__main__':
    unittest.main()