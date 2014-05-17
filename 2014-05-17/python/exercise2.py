from pyplasm import *
from scipy import *
import os,sys
sys.path.append("/Users/andreadodero/lar-cc/lib/py") 
from lar2psm import *
from simplexn import *
from larcc import *
from largrid import *
from mapper import *
from boolean import *
from sysml import *
from myfont import *
from architectural import *
from splines import *
from exercise1 import casa

base = S([1,2,3])([15,22,-.1])(CUBOID([1,1,1]))	
base = T([1,2])([-2,-15])(base)

discesa = S([1,2,3])([3,4.5,-.1])(CUBOID([1,1,1]))	

discesa = T([1,2])([2,4])(discesa)	
discesa = R([1,2])(PI)(discesa)	
discesa = R([2,3])(-PI/4)(discesa)	
discesa = T(3)(-5.9)(discesa)	

base2 =  T(3)(-3)(base)

#pool
controls = [[0,2],[0,0],[2.5,0],[1.5,2.5],[0,2.5]]
knots = [0,1,2,3,4,5,6,7]           # periodic B-spline
tbspline = TBSPLINE(S1)(2)(knots)(controls)  
obj = larMap(tbspline)(larDom(knots))

pool = STRUCT(MKPOLS(obj))

pool3d = DIFFERENCE([PROD([SOLIDIFY(pool),Q(0.3)]),CUBOID([8.4,.1,.3])])
pool3d = COLOR(BLUE)(pool3d)
pool3d = S([1,2])([5,5])(pool3d)

pool3d = T([1,2,3])([1,-15,-.2])(pool3d)

VIEW(STRUCT([base,base2, pool3d, T(3)(-3)(casa), discesa]))

