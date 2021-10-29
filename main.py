from carte import *

p = Perseverance(Terrain(100, 100, 10.0, True))
print(p.terrain)
p.scan_360()
print(p.carte)
