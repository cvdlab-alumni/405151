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
from scala import *

DRAW = COMP([VIEW,STRUCT,MKPOLS])
DRAW1 = COMP([STRUCT,MKPOLS])

# piano terra
pianoTerra = assemblyDiagramInit([7,7,2])([[.3,3,.1,4,.1,1,.3],[.3,3,.1,.7,.1,2,.3],[.3,2.7]])
#DRAW(pianoTerra)
garage = assemblyDiagramInit([1,1,2])([[1],[.3],[2.2,.5]])
portaScale = assemblyDiagramInit([1,3,2])([[1],[.2,.8,.2],[2.2,.5]])
portaSala = assemblyDiagramInit([3,1,2])([[.1,.3,.9],[1],[2.2,.5]])
porta2 = assemblyDiagramInit([3,1,2])([[.3,.4,.3],[1],[2.2,.5]])
portaSga = assemblyDiagramInit([1,3,2])([[1],[.2,.8,.2],[2.2,.5]])
finestre = assemblyDiagramInit([8,1,3])([[.25,.2,.15,.2,.15,.2,.1,.2],[1],[.6,.6,.6]])
finestre2 = assemblyDiagramInit([4,1,3])([[.4,.4,.3,.1],[1],[.6,.6,.6]])
pareteScala = assemblyDiagramInit([2,1,1])([[.5,.5],[1],[1]])


pianoTerra = diagram2cell(portaSga,pianoTerra,63)
pianoTerra = diagram2cell(finestre,pianoTerra,55)
pianoTerra = diagram2cell(portaSala,pianoTerra,51)
pianoTerra = diagram2cell(portaScale,pianoTerra,35)
pianoTerra = diagram2cell(finestre2,pianoTerra,27)
pianoTerra = diagram2cell(pareteScala,pianoTerra,23)
pianoTerra = diagram2cell(garage,pianoTerra,3)
pianoTerra = diagram2cell(porta2,pianoTerra,146)

V,CV = pianoTerra
hpc = SKEL_1(STRUCT(MKPOLS(pianoTerra)))
hpc = cellNumbering (pianoTerra,hpc)(range(len(CV)),CYAN,2)
#VIEW(hpc)

emptyChain = [16,28,41,66,149,129,123,43,45,68,
				23,137,20,146,88,74,76,90,89,75,
				73,87,48,93,70,101,107,145,150]
			
solidCV = [cell for k,cell in enumerate(pianoTerra[1]) if not (k in emptyChain)]
exteriorCV =  [cell for k,cell in enumerate(pianoTerra[1]) if k in emptyChain]
exteriorCV += exteriorCells(pianoTerra)

#DRAW((pianoTerra[0],solidCV))

#first = DRAW1((pianoTerra[0],solidCV))
#scala = R([1,2])(PI/2)(scala)
#first = STRUCT([first, T([1,2,3])([2,3.4,.3])(scala)])
ground0 = pianoTerra[0],solidCV
#VIEW(first)

CV = solidCV + exteriorCV
V = pianoTerra[0]
FV = [f for f in larFacets((V,CV),3,len(exteriorCV))[1] if len(f) >= 4]
#VIEW(EXPLODE(1.5,1.5,1.5)(MKPOLS((V,FV))))
BF = boundaryCells(solidCV,FV) 
boundaryFaces = [FV[face] for face in BF] 
B_Rep = V,boundaryFaces 

#VIEW(EXPLODE(1.5,1.5,1.5)(MKPOLS(B_Rep))) 
#VIEW(STRUCT(MKPOLS(B_Rep)))

