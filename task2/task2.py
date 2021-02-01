import sys
import yaml
import numpy as np

data = {}
with open(sys.argv[1]) as file:
    data = yaml.load(file)

xyz = []
s = data['sphere']
sc = s['center']
sr = s['radius']
l = data['line']

for a, b in zip(l[0], l[1]):
    xyz.append(np.poly1d([1, 0]) * a + np.poly1d([-1, 1]) * b)

e = np.poly1d(- sr ** 2)
for x, c in zip(xyz, sc):
    e += (c - x)**2
r = e.r.real[abs(e.r.imag)<1e-5]

ans = []
if len(r) == 0:
    print('Коллизий не найдено')
else:
    for root in r:
        ans.append(list(map(lambda x: x(root) , xyz)))
        print(ans[-1])

import Geometry3D as g3d
sren = g3d.Sphere(g3d.Point(sc[0], sc[1], sc[2]), sr)
lren = [g3d.Point(l[0][0], l[0][1], l[0][2]), g3d.Point(l[1][0], l[1][1], l[1][2])]
p = [g3d.Point(x[0], x[1], x[2]) for x in ans]
ren = g3d.Renderer(backend='matplotlib')
ren.add((g3d.Segment(lren[0], lren[1]),'b',2))
ren.add((sren,'r',1))
for x, y in zip(p, lren):
    ren.add((g3d.Segment(x, y),'b',2))
for x in p:
    ren.add((x,'g',10))
ren.show()
