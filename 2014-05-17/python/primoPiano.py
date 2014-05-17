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
## primo piano
primoPiano = assemblyDiagramInit([11,9,2])([[.3,1.5,.1,1.4,.1,1.9,.1,2,.1,1,.3],[.3,1.9,.1,2,.1,1,.1,1,.3],[.3,2.7]])
V1,CV1 = primoPiano
hpc = SKEL_1(STRUCT(MKPOLS(primoPiano)))
hpc = cellNumbering (primoPiano,hpc)(range(len(CV1)),CYAN,2)


toRemove = [33,69,105,141,177,29,65,25,61,21,57,93,129,
			197,133,165,169,101,137,173,97,195,191,196,
			172,135,139,173,191,167,131,111,
			75,39,23,59,43,41,95,115,113,103,151,149,147,
			63,51,194,192,190,196,178,176,172,175,179,193,174,28]


primoPiano = primoPiano[0], [cell for k,cell in enumerate(primoPiano[1]) if not (k in toRemove)]
hpc = SKEL_1(STRUCT(MKPOLS(primoPiano)))
hpc = cellNumbering (primoPiano,hpc)(range(len(primoPiano[1])),CYAN,2)


# porta bagno
toMerge = 52
cell = MKPOL([primoPiano[0],[[v+1 for v in  primoPiano[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))


diagram = assemblyDiagramInit([3,1,2])([[.1,.3,.1],[1],[2.2,.5]])
primoPiano = diagram2cell(diagram,primoPiano,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(primoPiano)))
hpc = cellNumbering (primoPiano,hpc)(range(len(primoPiano[1])),CYAN,2)
#VIEW(hpc)

toRemove = [144]

primoPiano = primoPiano[0], [cell for k,cell in enumerate(primoPiano[1]) if not (k in toRemove)]
hpc = SKEL_1(STRUCT(MKPOLS(primoPiano)))
hpc = cellNumbering (primoPiano,hpc)(range(len(primoPiano[1])),CYAN,2)

#DRAW(primoPiano)


# finestra salone
toMerge = 139
cell = MKPOL([primoPiano[0],[[v+1 for v in  primoPiano[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))


diagram = assemblyDiagramInit([1,2,2])([[1],[.3,.1],[2.2,.5]])
primoPiano = diagram2cell(diagram,primoPiano,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(primoPiano)))
hpc = cellNumbering (primoPiano,hpc)(range(len(primoPiano[1])),CYAN,2)
#VIEW(hpc)

toRemove = [146]

primoPiano = primoPiano[0], [cell for k,cell in enumerate(primoPiano[1]) if not (k in toRemove)]
hpc = SKEL_1(STRUCT(MKPOLS(primoPiano)))
hpc = cellNumbering (primoPiano,hpc)(range(len(primoPiano[1])),CYAN,2)


toMerge = 135
cell = MKPOL([primoPiano[0],[[v+1 for v in  primoPiano[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))


diagram = assemblyDiagramInit([1,2,2])([[1],[.1,.3],[2.2,.5]])
primoPiano = diagram2cell(diagram,primoPiano,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(primoPiano)))
hpc = cellNumbering (primoPiano,hpc)(range(len(primoPiano[1])),CYAN,2)
#VIEW(hpc)

toRemove = [150]

primoPiano = primoPiano[0], [cell for k,cell in enumerate(primoPiano[1]) if not (k in toRemove)]
hpc = SKEL_1(STRUCT(MKPOLS(primoPiano)))
hpc = cellNumbering (primoPiano,hpc)(range(len(primoPiano[1])),CYAN,2)

#VIEW(hpc)
#DRAW(primoPiano)

# finestra sala pranzo
toMerge = 122
cell = MKPOL([primoPiano[0],[[v+1 for v in  primoPiano[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))


diagram = assemblyDiagramInit([1,2,2])([[1],[.3,.2],[2.2,.5]])
primoPiano = diagram2cell(diagram,primoPiano,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(primoPiano)))
hpc = cellNumbering (primoPiano,hpc)(range(len(primoPiano[1])),CYAN,2)
#VIEW(hpc)

toRemove = [150]

primoPiano = primoPiano[0], [cell for k,cell in enumerate(primoPiano[1]) if not (k in toRemove)]
hpc = SKEL_1(STRUCT(MKPOLS(primoPiano)))
hpc = cellNumbering (primoPiano,hpc)(range(len(primoPiano[1])),CYAN,2)

#VIEW(hpc)
#DRAW(primoPiano)

toMerge = 118
cell = MKPOL([primoPiano[0],[[v+1 for v in  primoPiano[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))


diagram = assemblyDiagramInit([1,2,2])([[1],[.2,.3],[2.2,.5]])
primoPiano = diagram2cell(diagram,primoPiano,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(primoPiano)))
hpc = cellNumbering (primoPiano,hpc)(range(len(primoPiano[1])),CYAN,2)
#VIEW(hpc)

toRemove = [154]

primoPiano = primoPiano[0], [cell for k,cell in enumerate(primoPiano[1]) if not (k in toRemove)]
hpc = SKEL_1(STRUCT(MKPOLS(primoPiano)))
hpc = cellNumbering (primoPiano,hpc)(range(len(primoPiano[1])),CYAN,2)


#DRAW(primoPiano)

# porta cucina
toMerge = 92
cell = MKPOL([primoPiano[0],[[v+1 for v in  primoPiano[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))


diagram = assemblyDiagramInit([1,3,2])([[1],[.1,.3,.1],[2.2,.5]])
primoPiano = diagram2cell(diagram,primoPiano,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(primoPiano)))
hpc = cellNumbering (primoPiano,hpc)(range(len(primoPiano[1])),CYAN,2)
#VIEW(hpc)

toRemove = [156]

primoPiano = primoPiano[0], [cell for k,cell in enumerate(primoPiano[1]) if not (k in toRemove)]
hpc = SKEL_1(STRUCT(MKPOLS(primoPiano)))
hpc = cellNumbering (primoPiano,hpc)(range(len(primoPiano[1])),CYAN,2)

#DRAW(primoPiano)

# porta principale
toMerge = 3
cell = MKPOL([primoPiano[0],[[v+1 for v in  primoPiano[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))


diagram = assemblyDiagramInit([1,3,2])([[1],[.1,.4,.1],[2.2,.5]])
primoPiano = diagram2cell(diagram,primoPiano,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(primoPiano)))
hpc = cellNumbering (primoPiano,hpc)(range(len(primoPiano[1])),CYAN,2)
#VIEW(hpc)

toRemove = [160]

primoPiano = primoPiano[0], [cell for k,cell in enumerate(primoPiano[1]) if not (k in toRemove)]
hpc = SKEL_1(STRUCT(MKPOLS(primoPiano)))
hpc = cellNumbering (primoPiano,hpc)(range(len(primoPiano[1])),CYAN,2)

#VIEW(SKEL_1(DRAW(primoPiano)))
#VIEW(DRAW(primoPiano))