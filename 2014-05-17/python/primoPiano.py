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

DRAW = COMP([VIEW,STRUCT,MKPOLS])
DRAW1 = COMP([STRUCT,MKPOLS])

################################################################################################
## primo piano
primoPiano = assemblyDiagramInit([11,9,2])([[.3,1.5,.1,1.4,.1,1.9,.1,2,.1,1,.3],[.3,1.9,.1,2,.1,1,.1,1,.3],[.3,2.7]])
portaBagno = assemblyDiagramInit([3,1,2])([[.1,.3,.1],[1],[2.2,.5]])
finestra1 = assemblyDiagramInit([1,2,2])([[1],[.3,.1],[2.2,.5]])
finestra2 = assemblyDiagramInit([1,2,2])([[1],[.1,.3],[2.2,.5]])
finestra3 = assemblyDiagramInit([1,2,2])([[1],[.3,.2],[2.2,.5]])
finestra4 = assemblyDiagramInit([1,2,2])([[1],[.2,.3],[2.2,.5]])
portaCucina = assemblyDiagramInit([1,3,2])([[1],[.1,.3,.1],[2.2,.5]])
portaP = assemblyDiagramInit([1,3,2])([[1],[.1,.4,.1],[2.2,.5]])
finestraCucina = assemblyDiagramInit([3,1,3])([[.1,.5,.1],[1],[.4,.4,.2]])
finestraBagno = assemblyDiagramInit([3,1,3])([[.5,.3,.2],[1],[.4,.3,.3]])
pareteScale = assemblyDiagramInit([1,1,2])([[1],[1],[.2,.8]])


primoPiano = diagram2cell(finestra1,primoPiano,187)
primoPiano = diagram2cell(finestra2,primoPiano,183)
primoPiano = diagram2cell(finestra4,primoPiano,159)
primoPiano = diagram2cell(finestra3,primoPiano,155)
primoPiano = diagram2cell(portaCucina,primoPiano,119)
primoPiano = diagram2cell(finestraCucina,primoPiano,107)
primoPiano = diagram2cell(portaBagno,primoPiano,67)
primoPiano = diagram2cell(portaCucina,primoPiano,47)
primoPiano = diagram2cell(finestraBagno,primoPiano,35)
primoPiano = diagram2cell(pareteScale,primoPiano,27)
primoPiano = diagram2cell(portaP,primoPiano,3)

V,CV = primoPiano
hpc = SKEL_1(STRUCT(MKPOLS(primoPiano)))
hpc = cellNumbering (primoPiano,hpc)(range(len(CV)),CYAN,2)
VIEW(hpc)

emptyChain = [20,36,53,70,24,40,57,22,38,55,92,109,
				126,144,160,142,158,90,107,124,122,
				88,105,140,156,70,53,36,169,185,167,
				183,165,181,163,179,170,185,168,164,
				180,31,47,64,100,98,96,134,132,130,213,
				128,226,27,184,182,186,166,61,220,59,
				240,26,243,187,193,205,234,195,201]

solidCV = [cell for k,cell in enumerate(primoPiano[1]) if not (k in emptyChain)]
exteriorCV =  [cell for k,cell in enumerate(primoPiano[1]) if k in emptyChain]
exteriorCV += exteriorCells(primoPiano)

DRAW((primoPiano[0],solidCV))
ground1 = primoPiano[0],solidCV

CV = solidCV + exteriorCV
V = primoPiano[0]
FV = [f for f in larFacets((V,CV),3,len(exteriorCV))[1] if len(f) >= 4]
#VIEW(EXPLODE(1.5,1.5,1.5)(MKPOLS((V,FV))))
BF = boundaryCells(solidCV,FV) 
boundaryFaces = [FV[face] for face in BF] 
B_Rep = V,boundaryFaces 
#VIEW(EXPLODE(1.5,1.5,1.5)(MKPOLS(B_Rep))) 
#VIEW(STRUCT(MKPOLS(B_Rep)))


