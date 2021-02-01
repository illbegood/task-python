import sys
from dateutil.parser import parse
import csv

class Stats:
    def __init__(self):
        self.tries = {'+': 0, '-': 0}
        self.vol = {'+': 0, '-': 0}

startVol = -1
cap = 0
cur = 0
stats = {1 : Stats(), -1: Stats()}

def usage():
    print('''Usage: python3 task3.py <path> <since> <until>
    где <path> - путь к файлу лога, <since> и <until> - даты, в промежутке между которыми нужно производить анализ сообщений лога.''')

def getParams(s):
    sgn = 1
    s_ = ' - wanna '
    s = s[s.index(s_) + len(s_):]
    action = {1 : 'top up ', -1 : 'scoop '}
    if s.startswith(action[-1]): sgn = -1
    s = s[len(action[sgn]):]
    return int(s[:s.index('l')]), sgn

def update(n, sgn, b):
    key = '-'
    global cur
    global startVol
    if startVol == -1 and b:
        startVol = cur
    if (sgn == 1 and cur + n <= cap) or (sgn == -1 and cur - n >= 0):
        cur += sgn * n
        key = '+'
    if b:
        stats[sgn].tries[key] += 1
        stats[sgn].vol[key] += n

def process(s):
    d = parse(s[:s.index(' ')])
    if d > du: return False
    n, sgn = getParams(s)
    update(n, sgn, d>=ds)
    return True

def write_csv():
    with open('task3.csv', 'w') as file:
        writer = csv.writer(file)
        names = ['Кол-во попыток (налить)', 'Процент ошибок(налить)', 
        'Налитый объем', 'неналитый объем', 'Кол-во попыток (черпать)', 'Процент ошибок(черпать)', 
        'Вычерпанный объем', 'невычерпанный объем', 'Объем в начале', 'Объем в конце']
        writer.writerow(names)
        ans = []
        for k in stats:
            tm = stats[k].tries['-']
            tpm = stats[k].tries['+'] + tm
            ans.extend((tpm, '?' if startVol == -1 else 100 * tm / tpm, stats[k].vol['+'], stats[k].vol['-']))
        ans.append('?' if startVol == -1 else startVol)
        ans.append('?' if startVol == -1 else cur)
        writer.writerow(ans)

a = sys.argv
a = ['', 'test.log', '2021-01-29T21:07:18.973Z', '2021-01-29T21:07:18.974Z']
if len(a) == 4:
    try: 
        ds = parse(a[2])
        du = parse(a[3])
        if ds > du: raise Exception
        with open(a[1]) as file:
            file.readline()
            s = file.readline().rstrip()
            cap = int(s)
            s = file.readline().rstrip()
            cur = int(s)
            while True:
                s = file.readline()
                b = process(s)
                if not b: break
        write_csv()
    except Exception as e: usage()
else: usage()
