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


shape = [7,7,2]
sizePatterns = [[.3,3,.1,4,.1,1,.3],[.3,3,.1,1,.1,2,.3],[.3,2.7]]


# piano terra
pianoTerra = assemblyDiagramInit(shape)(sizePatterns)
V,CV = pianoTerra
hpc = SKEL_1(STRUCT(MKPOLS(pianoTerra)))
hpc = cellNumbering (pianoTerra,hpc)(range(len(CV)),CYAN,2)

toRemove = [45,31,17,73,53,49,47,75,77,81,95,83,80,94,83,97,82,96,21,25]
pianoTerra = V,[cell for k,cell in enumerate(CV) if not (k in toRemove)]


## garage
toMerge = 3
cell = MKPOL([pianoTerra[0],[[v+1 for v in  pianoTerra[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))

diagram = assemblyDiagramInit([1,1,2])([[1],[.3],[2.2,.5]])
pianoTerra = diagram2cell(diagram,pianoTerra,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(pianoTerra)))
hpc = cellNumbering (pianoTerra,hpc)(range(len(pianoTerra[1])),CYAN,2)
#VIEW(hpc)

toRemove = [78]
pianoTerra = pianoTerra[0], [cell for k,cell in enumerate(pianoTerra[1]) if not (k in toRemove)]
#DRAW(pianoTerra)

hpc = SKEL_1(STRUCT(MKPOLS(pianoTerra)))
hpc = cellNumbering (pianoTerra,hpc)(range(len(pianoTerra[1])),CYAN,2)
#VIEW(hpc)

## porta scale
toMerge = 30
cell = MKPOL([pianoTerra[0],[[v+1 for v in  pianoTerra[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))

diagram = assemblyDiagramInit([1,3,2])([[1],[.2,.8,.2],[2.2,.5]])
pianoTerra = diagram2cell(diagram,pianoTerra,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(pianoTerra)))
hpc = cellNumbering (pianoTerra,hpc)(range(len(pianoTerra[1])),CYAN,2)
#VIEW(hpc)

toRemove = [80]
pianoTerra = pianoTerra[0], [cell for k,cell in enumerate(pianoTerra[1]) if not (k in toRemove)]
#DRAW(pianoTerra)


## porta saletta
toMerge = 42
cell = MKPOL([pianoTerra[0],[[v+1 for v in  pianoTerra[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))

diagram = assemblyDiagramInit([3,1,2])([[.1,.3,.9],[1],[2.2,.5]])
pianoTerra = diagram2cell(diagram,pianoTerra,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(pianoTerra)))
hpc = cellNumbering (pianoTerra,hpc)(range(len(pianoTerra[1])),CYAN,2)
#VIEW(hpc)

toRemove = [84]
pianoTerra = pianoTerra[0], [cell for k,cell in enumerate(pianoTerra[1]) if not (k in toRemove)]
#DRAW(pianoTerra)

hpc = SKEL_1(STRUCT(MKPOLS(pianoTerra)))
hpc = cellNumbering (pianoTerra,hpc)(range(len(pianoTerra[1])),CYAN,2)
#VIEW(hpc)

## porta sgabuzzino
toMerge = 52
cell = MKPOL([pianoTerra[0],[[v+1 for v in  pianoTerra[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))

diagram = assemblyDiagramInit([1,3,2])([[1],[.2,.8,.2],[2.2,.5]])
pianoTerra = diagram2cell(diagram,pianoTerra,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(pianoTerra)))
hpc = cellNumbering (pianoTerra,hpc)(range(len(pianoTerra[1])),CYAN,2)
#VIEW(hpc)

toRemove = [88]
pianoTerra = pianoTerra[0], [cell for k,cell in enumerate(pianoTerra[1]) if not (k in toRemove)]
#DRAW(pianoTerra)

hpc = SKEL_1(STRUCT(MKPOLS(pianoTerra)))
hpc = cellNumbering (pianoTerra,hpc)(range(len(pianoTerra[1])),CYAN,2)
#VIEW(hpc)

## finestre 
toMerge = 44
cell = MKPOL([pianoTerra[0],[[v+1 for v in  pianoTerra[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))

diagram = assemblyDiagramInit([8,1,3])([[.25,.2,.15,.2,.15,.2,.1,.2],[1],[.6,.6,.6]])
pianoTerra = diagram2cell(diagram,pianoTerra,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(pianoTerra)))
hpc = cellNumbering (pianoTerra,hpc)(range(len(pianoTerra[1])),CYAN,2)
#VIEW(hpc)

toRemove = [94,100,106]
pianoTerra = pianoTerra[0], [cell for k,cell in enumerate(pianoTerra[1]) if not (k in toRemove)]
#DRAW(pianoTerra)

## finestre 
toMerge = 20
cell = MKPOL([pianoTerra[0],[[v+1 for v in  pianoTerra[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))

diagram = assemblyDiagramInit([4,1,3])([[.4,.4,.3,.1],[1],[.6,.6,.6]])
pianoTerra = diagram2cell(diagram,pianoTerra,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(pianoTerra)))
hpc = cellNumbering (pianoTerra,hpc)(range(len(pianoTerra[1])),CYAN,2)
#VIEW(hpc)


toRemove = [116,117,112,111]
pianoTerra = pianoTerra[0], [cell for k,cell in enumerate(pianoTerra[1]) if not (k in toRemove)]

#VIEW(SKEL_1(DRAW(pianoTerra)))
#VIEW(DRAW(pianoTerra))

