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

##################################################	secondo piano   ##############################################

secondoPiano = assemblyDiagramInit([9,9,2])([[.3,2.5,.1,1.3,.1,3.1,.1,1,.3],[.3,2.5,.1,1.4,.1,1,.1,1,.3],[.3,2.7]])
portaSga = assemblyDiagramInit([1,3,2])([[1],[.1,.3,.1],[2.2,.5]])
porta1 = assemblyDiagramInit([1,3,2])([[1],[.1,.4,.1],[2.2,.5]])
porta2 = assemblyDiagramInit([1,3,2])([[1],[.1,.3,.1],[2.2,.5]])

porta3 = assemblyDiagramInit([3,1,2])([[.1,.3,.1],[1],[2.2,.5]])
finestra2 = assemblyDiagramInit([1,2,3])([[1],[.2,.3],[1.5,2.2,.5]])
finestra21 = assemblyDiagramInit([1,2,3])([[1],[.2,.1],[1.5,2.2,.5]])
finestra4 = assemblyDiagramInit([1,2,3])([[1],[.1,.2],[1.5,2.2,.5]])
finestra1 = assemblyDiagramInit([1,3,2])([[1],[.2,.3,.5],[2.2,.5]])
finestra3 = assemblyDiagramInit([1,3,2])([[1],[.1,.3,.1],[2.2,.5]])

secondoPiano = diagram2cell(finestra21,secondoPiano,151)
secondoPiano = diagram2cell(finestra2,secondoPiano,147)
secondoPiano = diagram2cell(finestra21,secondoPiano,123)
secondoPiano = diagram2cell(porta1,secondoPiano,83)
secondoPiano = diagram2cell(porta2,secondoPiano,79)
secondoPiano = diagram2cell(porta3,secondoPiano,67)
secondoPiano = diagram2cell(porta3,secondoPiano,59)
secondoPiano = diagram2cell(porta2,secondoPiano,43)
secondoPiano = diagram2cell(finestra21,secondoPiano,15)
secondoPiano = diagram2cell(finestra1,secondoPiano,3)

V,CV = secondoPiano
hpc = SKEL_1(STRUCT(MKPOLS(secondoPiano)))
hpc = cellNumbering (secondoPiano,hpc)(range(len(CV)),CYAN,2)
#VIEW(hpc)

emptyChain = [208,19,54,37,57,23,88,86,90,94,96,98,129,
				145,132,148,150,134,131,132,149,147,133,
				151,130,135,128,144,146,121,123,125,104,
				106,108,27,190,69,31,48,64,44,59,61,196,
				178,184,172,165,162,153,201,26]

solidCV = [cell for k,cell in enumerate(secondoPiano[1]) if not (k in emptyChain)]
exteriorCV =  [cell for k,cell in enumerate(secondoPiano[1]) if k in emptyChain]
exteriorCV += exteriorCells(secondoPiano)

#DRAW((secondoPiano[0],solidCV))
ground2 = secondoPiano[0],solidCV

CV = solidCV + exteriorCV
V = secondoPiano[0]
FV = [f for f in larFacets((V,CV),3,len(exteriorCV))[1] if len(f) >= 4]
#VIEW(EXPLODE(1.5,1.5,1.5)(MKPOLS((V,FV))))
BF = boundaryCells(solidCV,FV) 
boundaryFaces = [FV[face] for face in BF] 
B_Rep = V,boundaryFaces 
#VIEW(EXPLODE(1.5,1.5,1.5)(MKPOLS(B_Rep))) 
#VIEW(STRUCT(MKPOLS(B_Rep)))
