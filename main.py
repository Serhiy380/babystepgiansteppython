import galois
import math
import numpy as np
def giantStep(p,g,h):
    GFp = galois.GF(p)
    g = GFp(g)
    h = GFp(h)
    n = 1 + math.floor(math.sqrt(g.multiplicative_order()))
   # print(g.multiplicative_order())
   # print(f"n:{n}")
    lst1 = [(g**i,i) for i in range(n+1)]
 #   print(lst1)
    lst2 = [(h*g**(-i*n),i) for i in range(n+1)]
  #  print(lst2)
    for l in lst1:
        for l2 in lst2:
            if l[0] == l2[0]:
                return l[1] + n*l2[1]



p = 17389
h = 13896
g = 9704

print(giantStep(p,g,h))