

def roman_number(a):
    roman = ""
    if a >= 100:
        if 5 <= int(repr(a)[-3]) <= 8:
            roman += "D"
        if int(repr(a)[-3])%5 <= 4:
            if (int(repr(a)[-3])+4)%5 == 0:
                    roman += "C"
            elif (int(repr(a)[-3])+3)%5 == 0:
                roman += "CC"
            elif (int(repr(a)[-3])+2)%5 == 0:
                roman += "CCC"
        if (int(repr(a)[-3])+1)%5 == 0:
            roman += "C"
            if int(repr(a+100)[-3]) == 5:
                roman += "D"
    if a >= 10:
        if 5 <= int(repr(a)[-2]) <= 8:
            roman += "L"
        if int(repr(a)[-2])%5 <= 4:
            if (int(repr(a)[-2])+4)%5 == 0:
                    roman += "X"
            elif (int(repr(a)[-2])+3)%5 == 0:
                roman += "XX"
            elif (int(repr(a)[-2])+2)%5 == 0:
                roman += "XXX"
        if (int(repr(a)[-2])+1)%5 == 0:
            roman += "X"
            if int(repr(a+10)[-2]) == 5:
                roman += "L"
            elif int(repr(a+10)[-2]) == 0:
                roman += "C"
    if 5 <= int(repr(a)[-1]) <= 8:
        roman += "V"
    if a%5 <= 4:
        if (a+4)%5 == 0:
            roman += "I"
        elif (a+3)%5 == 0:
            roman += "II"
        elif (a+2)%5 == 0:
            roman += "III"
    if (a+1)%5 == 0:
        roman += "I"
        if int(repr(a)[-1]) == 4:
            roman += "V"
        elif int(repr(a)[-1]) == 9:
            roman += "X"
    return roman

