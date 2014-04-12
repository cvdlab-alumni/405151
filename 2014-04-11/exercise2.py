import sys
sys.path.insert(0, '/Users/andreadodero/lar-cc/lib/py') 
from pyplasm import *
from larcc import *
from mapper import *
from fn import *
from exercise1 import *


###############################################################################################################
#########################################    scala   ##########################################################

gradino = S([1,2,3])([10,10.5,.25])(CUBOID([1,1,1]))	
scala = STRUCT( CAT(N(13)([gradino, T(3)(0.25), S(1)(.9)])) )
scala = T([1,2])([21,-5])(scala)
scala= R([1,2])(PI/8)(scala)

###############################################################################################################
#########################################    porta  ###########################################################

domainarco3 = PROD([domain(50), INTERVALS(1)(1)])
disco = MAP(disco)(domainarco3)
disco = PROD([Q(1),disco])
disco = ROTN([PI,[1,1,0]])(disco)
disco = T([1,3])([1,3.5])(disco)
porta = S([1,2,3])([2,1,3.5])(CUBOID([1,1,1]))	
porta = STRUCT([porta,disco])
obj = porta
porta= R([1,2])(-42)(porta)
porta = T([1,2,3])([20,7.5,3])(porta)
mura_esterne = DIFF([mura_esterne, porta])

###############################################################################################################
#########################################    porta interna  ###########################################################

porta_interna = porta
porta_interna = T([1,2])([-11.8,-4.8])(porta_interna)
mura_interne = DIFF([mura_interne,porta_interna])

###############################################################################################################
#########################################  colonne  ###########################################################


V,CV = larRod([.25,7])([50,1])
colonna = STRUCT(MKPOLS([V,CV]))
colonna = T([1,2,3])([20.5,7,3])(colonna)

colonna2 = STRUCT(MKPOLS([V,CV]))
colonna2 = T([1,2,3])([19.2,10,3])(colonna2)
castello = STRUCT([castello,colonna,colonna2])

verts = [[0,0],[4,0],[2,2]]
cells = [[1,2,3]]
pols = None
trave = MKPOL([verts, cells, pols])
trave = PROD([Q(1),trave])
trave = T(3)(10)(trave)

trave= R([1,2])(-31)(trave)
trave = T([1,2])([19.9,6.4])(trave)

colonne = STRUCT([colonna,colonna2,trave])

#VIEW(STRUCT([castello,trave]))

###############################################################################################################
#########################################  finestra  ##########################################################

finestra = porta
finestra = S([1,2,3])([.5,.5,.5])(porta)
finestra = T([1,2,3])([9.7,4.3,12])(finestra)
mura_esterne = DIFF([mura_esterne, finestra])

###############################################################################################################
#########################################  feritoie  ##########################################################

feritoia = obj
feritoia = S([1,3])([.2,.5])(feritoia)
feritoia= R([1,2])(-20)(feritoia)
feritoia = T([1,2,3])([2.5,1.3,7])(feritoia)
feritoia1 = T(3)(10)(feritoia)
feritoie = STRUCT([feritoia1,feritoia])

torreConFeritoie = DIFF([torre,COLOR(BLACK)(feritoie)])

torri = STRUCT([T([1,2])([0,23])(torreConFeritoie),T([1,2])([-23,0])(torreConFeritoie),
	T([1,2])([0,-23])(torreConFeritoie),T([1,2])([23,0])(torreConFeritoie),
	T([1,2])([-17,17])(torreConFeritoie),T([1,2])([17,-17])(torreConFeritoie),
	T([1,2])([-17,-17])(torreConFeritoie),T([1,2])([17,17])(torreConFeritoie)])

castello = STRUCT([mura_interne, mura_esterne, piani, torri, scala,COLOR(GREEN)(base),colonne, COLOR(GREEN)(cortile)])

#VIEW(castello)




