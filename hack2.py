import unittest


def Strongpassword(a):
    special_characters = "!@#$%^&*()-+"
    a = str(a)
    min = 4
    l = 1
    L = 1
    n = 1
    e = 1
    for i in a:
        if i.isupper() == True and l==1:
            min -= 1
            l = 0
        if i.islower() == True and L == 1:
            min -= 1
            L = 0
    return min

class Testhack(unittest.TestCase):
    def test1(self):
        self.assertEqual(Strongpassword("Aaaaaa"),2)

if __name__ == "__main__":
    unittest.main()