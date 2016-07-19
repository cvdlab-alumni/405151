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
from scala import *

DRAW = COMP([VIEW,STRUCT,MKPOLS])
DRAW1 = COMP([STRUCT,MKPOLS])
water = [0.05,0.4,0.4,1,  0,0.3,0.3,0.5,  2,2,2,1, 0,0,0,1, 100]

## base primo piano, giardini

base = CUBOID([1,1,1])
base = S([1,2,3])([15,15,.1])(base)
base = T([1,2,3])([0,-8.2,3])(base)

base2 = CUBOID([1,1,1])
base2 = S([1,2,3])([2.5,12,.1])(base2)
base2 = T([1,2,3])([-2.5,-8.5,3])(base2)

base3 = S([1,2])([1.5,1.5])(base)
base3 = T(3)(-3.1)(base3)

giardino1 = CUBOID([1,1,1])
giardino1 = S([1,2,3])([13,6.3,.1])(giardino1)
giardino1 = T([1,2,3])([15,-8.2,3])(giardino1)
giardino1 = COLOR([0,0.6,0.1])(giardino1)


giardino2 = S(2)(.3)(giardino1)
giardino2 = T(2)(7.4)(giardino2)
giardino3 = S([1,2])([.18,3.9])(giardino2)
giardino3 = T([1,2])([23,-21.5])(giardino3)

muro = CUBOID([1,1,1])
muro = S([1,2,3])([20,.2,3])(muro)
muro = T([1,2])([7.6,6.6])(muro)

#### giardino superiore

giardinoUP = assemblyDiagramInit([3,5,4])([[.5,10,.5],[.5,3,.5,3,.5],[.5,2,1,.5]])
V,CV = giardinoUP
hpc = SKEL_1(STRUCT(MKPOLS(giardinoUP)))
hpc = cellNumbering (giardinoUP,hpc)(range(len(CV)),CYAN,2)
#VIEW(hpc)

emptyChain1 = [27,26,23,22,7,6,3,2,47,46,43,42,35,25]

solidCV1 = [cell for k,cell in enumerate(giardinoUP[1]) if not (k in emptyChain1)]
exteriorCV1 =  [cell for k,cell in enumerate(giardinoUP[1]) if k in emptyChain1]
exteriorCV1 += exteriorCells(giardinoUP)


gia1 = MKPOL([giardinoUP[0],[[v+1 for v in  giardinoUP[1][35]]],None])
gia2 = MKPOL([giardinoUP[0],[[v+1 for v in  giardinoUP[1][25]]],None])

gia1 = COLOR([0,0.6,0.1])(gia1)
gia2 = COLOR([0,0.6,0.1])(gia2)

giardinoUP = DRAW1((giardinoUP[0],solidCV1))
giardinoUP = STRUCT([gia1,gia2,giardinoUP])

giardinoDOWN = giardinoUP
giardinoRight = giardinoUP

#VIEW(giardinoUP)

giardinoUP = S(1)(2.8)(giardinoUP)
giardinoUP = R([1,2])(PI)(giardinoUP)
giardinoUP = T([1,2,3])([28,-8,3])(giardinoUP)


giardinoDOWN = R([1,2])(PI)(giardinoDOWN)
giardinoDOWN = S(1)(1.4)(giardinoDOWN)
giardinoDOWN = T([1,2,3])([15,15,-4])(giardinoDOWN)

giardinoRight =  R([1,2])(PI)(giardinoRight)
giardinoRight = S([1,2,3])([.6,.9,.8])(giardinoRight)
giardinoRight = T([1,2])([-2.5,1])(giardinoRight)
#### piscina
piscina = assemblyDiagramInit([3,3,3])([[.5,10,.5],[.5,6,.5],[.5,3,.5]])
V,CV = piscina
hpc = SKEL_1(STRUCT(MKPOLS(piscina)))
hpc = cellNumbering (piscina,hpc)(range(len(CV)),CYAN,2)

emptyChain = [13,14]

solidCV = [cell for k,cell in enumerate(piscina[1]) if not (k in emptyChain)]
exteriorCV =  [cell for k,cell in enumerate(piscina[1]) if k in emptyChain]
exteriorCV += exteriorCells(piscina)

acqua1 = MKPOL([piscina[0],[[v+1 for v in  piscina[1][13]]],None])
acqua1 =  MATERIAL(water)(acqua1)
piscina = DRAW1((piscina[0],solidCV))
piscina = STRUCT([piscina, acqua1])
piscina  = S(3)(.8)(piscina)

#####  albero
cilindro = COLOR([0.5,0.30,0.1])(CYLINDER([1,5.50])(240))
chioma = COLOR(GREEN)(SPHERE(5)([9,10]))
albero = STRUCT([T(3)(10)(chioma),cilindro])
albero = S([1,2,3])([.2,.2,.2])(albero)
#VIEW(albero)

alberi = STRUCT([T([1,2,3])([11,10,0])(albero), 
	T([1,2,3])([5,13,-1.5])(albero), 
	T([1,2,3])([25,-3,3])(albero), 
	T([1,2,3])([20,-6,3])(albero),
	T([1,2,3])([8,-9,5.5])(albero)])

scala = R([1,2])(-PI/2)(scala)

###  utilizzo spline per tagliare piano
controlpoints = [[-0,0],[1,0],[1,1],[2,1],[3,1]]
dom = larDomain([32],'simplex')
obj = larMap(larBezier(S1)(controlpoints))(dom)

curva  = STRUCT(MKPOLS(obj))
#curva = R([1,2])(PI)(curva)
#VIEW(curva)

pts = [[0,0],[3,0]]
baseC = JOIN([curva,POLYLINE(pts)])
baseC = OFFSET([0.01,0.01,0.01])(baseC)
baseC = S([1,2,3])([3,3,2.5])(baseC)
baseC = T([1,2,3])([-4.2,0,1])(baseC)
baseC = R([1,2])(PI)(baseC)


pareteC = PROD([curva,Q(3)])
pareteC = OFFSET([0.01,0.01,0.01])(pareteC)
pareteC = S([1,2,3])([1.8,1.4,1])(pareteC)
pareteC = T([1,2])([.3,3])(pareteC)


giardinoUP = DIFF([giardinoUP,T([1,2,3])([2,-8,2])(baseC)])

piantaCasa = STRUCT([T([1,2])([9,9])(scala), alberi , muro,giardinoRight, giardinoDOWN,giardinoUP,base2,base3, giardino3, giardino2, giardino1,base, casa, T([1,2])([15,-2])(piscina)])

VIEW(piantaCasa)
