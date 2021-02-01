def itoBase10(nb, base):
    digits = []
    n = len(base)
    while nb != 0:
        digits.insert(0, base[nb % n])
        nb = nb // n
    return '0' if len(digits) == 0 else ''.join(digits)

def itoBase(nbs, baseSrc, baseDest):
    nb = 0
    n = len(baseSrc)
    for c in nbs:
        nb *= n
        nb += baseSrc.index(c)
    return itoBase10(nb, baseDest)

def checkLen(args):
    for s in args:
        if len(s) >= 256: return False
    return True

def checkInt10(s):
    return s.isdigit()

def checkInt(s, base):
    for c in s:
        if c not in s: return False
    return True

def checkBase(s):
    return len(set(s)) == len(s)

def usage():
    print('''Usage: 
    а) python3 task1.py <nb> <base>
    где <nb> - беззнаковое целое число, <base> - набор цифр, задающий конечную систему счисления;
    б) python3 task1.py <nbs> <baseSrc> <baseDest>
    где <baseSrc>, <baseDest> - наборы цифр, задающие начальную и конечную системы счисления соответственно,
    <nbs> - строка, представляющая беззнаковое целое число в система счисления <baseSrc>.''')

import sys

a = sys.argv
a = ['task1.py', '1ff', '0123456789abcdef', '01234567']
n = len(a)
if n == 3 and checkLen(a[1:]) and checkInt10(a[1]) and checkBase(a[2]):
    print(itoBase10(int(a[1]), a[2]))
elif n == 4 and checkLen(a[1:]) and checkBase(a[2]) and checkInt(a[1], a[2]) and checkBase(a[3]):
    print(itoBase(a[1], a[2], a[3]))
else: usage()