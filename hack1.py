import unittest

def camelCase(a):
    palabras = 1
    for i in a:
        if i.isupper() == True:
            palabras += 1 
    return palabras

class Testpingo(unittest.TestCase):
    def test1(self):
        self.assertEqual(camelCase("holaMundoMMMMMM"),8)

if __name__ == "__main__":
    unittest.main()
