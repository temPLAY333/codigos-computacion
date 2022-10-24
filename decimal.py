from itertools import count
import unittest

def NumberRD(a):
    if a.count("I") >= 4 or a.count("V") >= 2 or a.count("XXXX") >= 1 or a.count("L") >= 2:
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
    numberD -= a.count("XM")*200
    return numberD
