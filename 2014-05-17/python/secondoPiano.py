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

DRAW = COMP([STRUCT,MKPOLS])

################################################################################################
## secondo piano
secondoPiano = assemblyDiagramInit([9,9,2])([[.3,2.5,.1,1.3,.1,3.1,.1,1,.3],[.3,2.5,.1,1.4,.1,1,.1,1,.3],[.3,2.7]])
V2,CV2 = secondoPiano
hpc = SKEL_1(STRUCT(MKPOLS(secondoPiano)))
hpc = cellNumbering (secondoPiano,hpc)(range(len(CV2)),CYAN,2)
#VIEW(hpc)


toRemove = [21,39,57,93,111,129,25,61,63,
			65,47,29,28,95,97,115,133,131,
			105,69,51,33,113,141,137,101,103,
			140,158,156,154,136,139,159,157,155,
			160,142,138,143,161]


secondoPiano = secondoPiano[0], [cell for k,cell in enumerate(secondoPiano[1]) if not (k in toRemove)]
hpc = SKEL_1(STRUCT(MKPOLS(secondoPiano)))
hpc = cellNumbering (secondoPiano,hpc)(range(len(secondoPiano[1])),CYAN,2)


#VIEW(hpc)
#DRAW(secondoPiano)

# porta sgabuzzino
toMerge = 37
cell = MKPOL([secondoPiano[0],[[v+1 for v in  secondoPiano[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))


diagram = assemblyDiagramInit([1,3,2])([[1],[.1,.3,.1],[2.2,.5]])
secondoPiano = diagram2cell(diagram,secondoPiano,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(secondoPiano)))
hpc = cellNumbering (secondoPiano,hpc)(range(len(secondoPiano[1])),CYAN,2)
#VIEW(hpc)

toRemove = [122]

secondoPiano = secondoPiano[0], [cell for k,cell in enumerate(secondoPiano[1]) if not (k in toRemove)]
hpc = SKEL_1(STRUCT(MKPOLS(secondoPiano)))
hpc = cellNumbering (secondoPiano,hpc)(range(len(secondoPiano[1])),CYAN,2)

#DRAW(secondoPiano)
#VIEW(hpc)


# porta camera1
toMerge = 49
cell = MKPOL([secondoPiano[0],[[v+1 for v in  secondoPiano[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))


diagram = assemblyDiagramInit([3,1,2])([[.1,.3,.1],[1],[2.2,.5]])
secondoPiano = diagram2cell(diagram,secondoPiano,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(secondoPiano)))
hpc = cellNumbering (secondoPiano,hpc)(range(len(secondoPiano[1])),CYAN,2)
#VIEW(hpc)

toRemove = [126]

secondoPiano = secondoPiano[0], [cell for k,cell in enumerate(secondoPiano[1]) if not (k in toRemove)]
hpc = SKEL_1(STRUCT(MKPOLS(secondoPiano)))
hpc = cellNumbering (secondoPiano,hpc)(range(len(secondoPiano[1])),CYAN,2)

#DRAW(secondoPiano)
#VIEW(hpc)

# porta camera 2
toMerge = 64
cell = MKPOL([secondoPiano[0],[[v+1 for v in  secondoPiano[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))


diagram = assemblyDiagramInit([1,3,2])([[1],[.1,.3,.1],[2.2,.5]])
secondoPiano = diagram2cell(diagram,secondoPiano,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(secondoPiano)))
hpc = cellNumbering (secondoPiano,hpc)(range(len(secondoPiano[1])),CYAN,2)
#VIEW(hpc)

toRemove = [130]

secondoPiano = secondoPiano[0], [cell for k,cell in enumerate(secondoPiano[1]) if not (k in toRemove)]
hpc = SKEL_1(STRUCT(MKPOLS(secondoPiano)))
hpc = cellNumbering (secondoPiano,hpc)(range(len(secondoPiano[1])),CYAN,2)

#DRAW(secondoPiano)
#VIEW(hpc)

# porta camera 3
toMerge = 67
cell = MKPOL([secondoPiano[0],[[v+1 for v in  secondoPiano[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))


diagram = assemblyDiagramInit([1,3,2])([[1],[.1,.3,.1],[2.2,.5]])
secondoPiano = diagram2cell(diagram,secondoPiano,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(secondoPiano)))
hpc = cellNumbering (secondoPiano,hpc)(range(len(secondoPiano[1])),CYAN,2)
#VIEW(hpc)

toRemove = [134]

secondoPiano = secondoPiano[0], [cell for k,cell in enumerate(secondoPiano[1]) if not (k in toRemove)]
hpc = SKEL_1(STRUCT(MKPOLS(secondoPiano)))
hpc = cellNumbering (secondoPiano,hpc)(range(len(secondoPiano[1])),CYAN,2)

#DRAW(secondoPiano)
#VIEW(hpc)


# porta bagno2
toMerge = 53
cell = MKPOL([secondoPiano[0],[[v+1 for v in  secondoPiano[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))


diagram = assemblyDiagramInit([3,1,2])([[.1,.3,.1],[1],[2.2,.5]])
secondoPiano = diagram2cell(diagram,secondoPiano,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(secondoPiano)))
hpc = cellNumbering (secondoPiano,hpc)(range(len(secondoPiano[1])),CYAN,2)
#VIEW(hpc)

toRemove = [138]

secondoPiano = secondoPiano[0], [cell for k,cell in enumerate(secondoPiano[1]) if not (k in toRemove)]
hpc = SKEL_1(STRUCT(MKPOLS(secondoPiano)))
hpc = cellNumbering (secondoPiano,hpc)(range(len(secondoPiano[1])),CYAN,2)

#DRAW(secondoPiano)
#VIEW(hpc)

# finestra camera2
toMerge = 109
cell = MKPOL([secondoPiano[0],[[v+1 for v in  secondoPiano[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))


diagram = assemblyDiagramInit([1,2,3])([[1],[.2,.3],[1.5,2.2,.5]])
secondoPiano = diagram2cell(diagram,secondoPiano,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(secondoPiano)))
hpc = cellNumbering (secondoPiano,hpc)(range(len(secondoPiano[1])),CYAN,2)
#VIEW(hpc)

toRemove = [144]

secondoPiano = secondoPiano[0], [cell for k,cell in enumerate(secondoPiano[1]) if not (k in toRemove)]
hpc = SKEL_1(STRUCT(MKPOLS(secondoPiano)))
hpc = cellNumbering (secondoPiano,hpc)(range(len(secondoPiano[1])),CYAN,2)

#VIEW(hpc)
#DRAW(secondoPiano)

# finestra camera2
toMerge = 96
cell = MKPOL([secondoPiano[0],[[v+1 for v in  secondoPiano[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))


diagram = assemblyDiagramInit([1,2,3])([[1],[.2,.1],[1.5,2.2,.5]])
secondoPiano = diagram2cell(diagram,secondoPiano,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(secondoPiano)))
hpc = cellNumbering (secondoPiano,hpc)(range(len(secondoPiano[1])),CYAN,2)
#VIEW(hpc)

toRemove = [145]

secondoPiano = secondoPiano[0], [cell for k,cell in enumerate(secondoPiano[1]) if not (k in toRemove)]
hpc = SKEL_1(STRUCT(MKPOLS(secondoPiano)))
hpc = cellNumbering (secondoPiano,hpc)(range(len(secondoPiano[1])),CYAN,2)


toMerge = 92
cell = MKPOL([secondoPiano[0],[[v+1 for v in  secondoPiano[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))


diagram = assemblyDiagramInit([1,2,3])([[1],[.1,.2],[1.5,2.2,.5]])
secondoPiano = diagram2cell(diagram,secondoPiano,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(secondoPiano)))
hpc = cellNumbering (secondoPiano,hpc)(range(len(secondoPiano[1])),CYAN,2)
#VIEW(hpc)

toRemove = [152]

secondoPiano = secondoPiano[0], [cell for k,cell in enumerate(secondoPiano[1]) if not (k in toRemove)]
hpc = SKEL_1(STRUCT(MKPOLS(secondoPiano)))
hpc = cellNumbering (secondoPiano,hpc)(range(len(secondoPiano[1])),CYAN,2)

#VIEW(hpc)
#DRAW(secondoPiano)


# finestra camera1
toMerge = 3
cell = MKPOL([secondoPiano[0],[[v+1 for v in  secondoPiano[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))


diagram = assemblyDiagramInit([1,3,2])([[1],[.2,.3,.5],[2.2,.5]])
secondoPiano = diagram2cell(diagram,secondoPiano,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(secondoPiano)))
hpc = cellNumbering (secondoPiano,hpc)(range(len(secondoPiano[1])),CYAN,2)
#VIEW(hpc)

toRemove = [154]

secondoPiano = secondoPiano[0], [cell for k,cell in enumerate(secondoPiano[1]) if not (k in toRemove)]
hpc = SKEL_1(STRUCT(MKPOLS(secondoPiano)))
hpc = cellNumbering (secondoPiano,hpc)(range(len(secondoPiano[1])),CYAN,2)
#DRAW(secondoPiano)


# finestra camera3
toMerge = 14
cell = MKPOL([secondoPiano[0],[[v+1 for v in  secondoPiano[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))


diagram = assemblyDiagramInit([1,3,2])([[1],[.1,.3,.1],[2.2,.5]])
secondoPiano = diagram2cell(diagram,secondoPiano,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(secondoPiano)))
hpc = cellNumbering (secondoPiano,hpc)(range(len(secondoPiano[1])),CYAN,2)
#VIEW(hpc)

toRemove = [158]

secondoPiano = secondoPiano[0], [cell for k,cell in enumerate(secondoPiano[1]) if not (k in toRemove)]
hpc = SKEL_1(STRUCT(MKPOLS(secondoPiano)))
hpc = cellNumbering (secondoPiano,hpc)(range(len(secondoPiano[1])),CYAN,2)


#VIEW(SKEL_1(DRAW(secondoPiano)))
#VIEW(DRAW(secondoPiano))