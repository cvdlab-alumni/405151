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
feritoia = S([1,3])([.1,.5])(feritoia)

feritoiaNord = R([1,2])(-20)(feritoia)
feritoiaEst = R([1,2])(-2)(feritoia)
feritoiaOvest = R([1,2])(-0.4)(feritoia)

feritoiaNord = T([1,2,3])([2.4,1.3,7])(feritoiaNord)
feritoiaEst = T([1,2,3])([2.6,-1,7])(feritoiaEst)
feritoiaOvest = T([1,2,3])([1,2.6,7])(feritoiaOvest)

feritoia2Nord = T(3)(10)(feritoiaNord)
feritoia2Est = T(3)(10)(feritoiaEst)
feritoia2Ovest = T(3)(10)(feritoiaOvest)

feritoie = STRUCT([feritoiaNord, feritoia2Nord, feritoia2Est, feritoiaEst, feritoiaOvest, feritoia2Ovest])

###############################################################################################################
#########################################  porta torre  #######################################################

porta_torre = T([1,2])([-10.5,-4.8])(porta_interna) 
porta2torre = T(3)(10)(porta_torre) 
porteTorre = STRUCT([porta_torre,porta2torre])

feritoie_porte = STRUCT([feritoie,porteTorre])
torreConFeritoie = DIFF([torre, feritoie_porte])

torri_nord = R([1,2])(PI)(torreConFeritoie)
torri_est = R([1,2])(PI/2)(torreConFeritoie)
torri_ovest = R([1,2])(-PI/2)(torreConFeritoie)

torri = STRUCT([

	T([1,2])([0,23])(torri_est),
	T([1,2])([-17,17])(torri_est),

	T([1,2])([0,-23])(torri_ovest),
	T([1,2])([17,-17])(torri_ovest),

	T([1,2])([-17,-17])(torri_nord),
	T([1,2])([-23,0])(torri_nord),

	T([1,2])([23,0])(torreConFeritoie),
	T([1,2])([17,17])(torreConFeritoie)

	])

###############################################################################################################
#########################################  comp castello  #####################################################
 
mura_interne = MATERIAL([1,0,0,1,  0,1,0,1,  0,0,1,0, 0,0,0,1, 100])(mura_interne)
mura_esterne = MATERIAL([1,0,0,1,  0,1,0,1,  0,0,1,0, 0,0,0,1, 100])(mura_esterne)
piani = MATERIAL([1,0,0,1,  0,1,0,1,  0,0,1,0, 0,0,0,1, 100])(piani)
torri = MATERIAL([1,0,0,1,  0,1,0,1,  0,0,1,0, 0,0,0,1, 100])(torri)
scala = MATERIAL([1,0,0,1,  0,1,0,1,  0,0,1,0, 0,0,0,1, 100])(scala)
colonne = MATERIAL([1,0,0,1,  0,1,0,1,  0,0,1,0, 0,0,0,1, 100])(colonne)

castello = STRUCT([mura_interne, mura_esterne, piani, torri, scala,COLOR(GREEN)(base),colonne, COLOR(GREEN)(cortile)])

VIEW(castello)




