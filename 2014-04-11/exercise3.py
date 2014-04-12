import sys
sys.path.insert(0, '/Users/andreadodero/lar-cc/lib/py') 
from pyplasm import *
from larcc import *
from mapper import *
from fn import *
from exercise1 import *
from exercise2 import *


###############################################################################################################
#########################################  palazzo  ##########################################################

verts = [[0,0],[1,0],[1,1],[0,1]]
cells = [[1,2,3,4]]
pols = None
parete = MKPOL([verts, cells, pols])
parete = PROD([Q(1),parete])

parete = S([1,3])([20,10])(parete)


finestra = CUBOID([1,1,2])
finestra = T([1,3])([2,7])(finestra)
finestre = STRUCT( CAT(N(7)([finestra, T(1)(2)])) )
finestre = STRUCT([T(3)(-3)(finestre),finestre,T(3)(-6)(finestre)])

parete = DIFF([parete,finestre])


parete2 = R([1,2])(PI/2)(parete)
parete2 = T(1)(1)(parete2)
parete3 = T(2)(19)(parete)
parete4 = T(1)(19)(parete2)

porta = CUBOID([1.5,1,2.5])
porta = T(1)(17)(porta)

parete = DIFF([parete,porta])

pareti = STRUCT([parete, parete2,parete3,parete4])

verts = [[0,0],[1,0],[1,1],[0,1]]
cells = [[1,2,3,4]]
pols = None
roof = MKPOL([verts, cells, pols])
roof = S([1,2])([20,20])(roof)
roof = PROD([Q(.5),(roof)])
roof = R([1,3])(PI/2)(roof)
roof = T([1,3])([20,10])(roof)

palazzo = STRUCT([pareti,roof])
#VIEW(palazzo)

###############################################################################################################
################################################################################################################

palazzo = T([1,2])([-80,70])(palazzo)
palazzo = R([1,2])(PI)(palazzo)
palazzi = STRUCT([ T([1,2])([0,50])(palazzo),palazzo, T([1,2])([-50,0])(palazzo)])

VIEW(STRUCT([castello, palazzi ]))

