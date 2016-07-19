from pyplasm import *
from scipy import *
import os,sys
sys.path.insert(0, '/Users/dodo/UNI/Grafica\ computazionale/lar-cc/lib/py/') 

from larlib import * 

def objExporter((V,FV), filePath):
    out_file = open(filePath,"w")
    out_file.write("# List of Vertices:\n")
    for v in V:
        out_file.write("v")
        for c in v:
            out_file.write(" " + str(c))
        out_file.write("\n")
    out_file.write("# Face Definitions:\n")
    for f in FV:
        out_file.write("f")
        for v in f:
            out_file.write(" " + str(v+1))
        out_file.write("\n")
    out_file.close()

DRAW = COMP([VIEW,STRUCT,MKPOLS])
DRAW1 = COMP([STRUCT,MKPOLS])
glass = [0.1,0.2,0.3,1,  0,0,0,0.5,  2,2,2,1, 0,0,0,1, 100]
BROWN= Color4f([0.83, 0.65, 0.5, 1.0])

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
pareteScale = assemblyDiagramInit([2,1,1])([[.7,.3],[1],[1]])

'''V,CV = secondoPiano
hpc = SKEL_1(STRUCT(MKPOLS(secondoPiano)))
hpc = cellNumbering (secondoPiano,hpc)(range(len(CV)),CYAN,2)
VIEW(hpc)'''

secondoPiano = diagram2cell(finestra21,secondoPiano,151)
secondoPiano = diagram2cell(finestra2,secondoPiano,147)
secondoPiano = diagram2cell(finestra4,secondoPiano,123)
secondoPiano = diagram2cell(porta1,secondoPiano,83)
secondoPiano = diagram2cell(porta2,secondoPiano,79)
secondoPiano = diagram2cell(porta3,secondoPiano,67)
secondoPiano = diagram2cell(porta3,secondoPiano,59)
secondoPiano = diagram2cell(porta2,secondoPiano,43)
secondoPiano = diagram2cell(pareteScale,secondoPiano,27)
secondoPiano = diagram2cell(finestra21,secondoPiano,15)
secondoPiano = diagram2cell(finestra1,secondoPiano,3)

V,CV = secondoPiano
hpc = SKEL_1(STRUCT(MKPOLS(secondoPiano)))
hpc = cellNumbering (secondoPiano,hpc)(range(len(CV)),CYAN,2)
#VIEW(hpc)

emptyChain = [30,47,73,63,132,97,95,133,149,150,
				127,144,128,134,148,131,130,
				146,145,143,129,147,85,87,89,95,97,93,95,
				107,105,103,120,122,124,19,36,53,23,56,58,
				26,43,60,171,202,167,161,152,177,189,195,183,209,25,199]

solidCV = [cell for k,cell in enumerate(secondoPiano[1]) if not (k in emptyChain)]
exteriorCV =  [cell for k,cell in enumerate(secondoPiano[1]) if k in emptyChain]
exteriorCV += exteriorCells(secondoPiano)

struttura2 = DRAW1((secondoPiano[0],solidCV))

finestra1 = MKPOL([secondoPiano[0],[[v+1 for v in  secondoPiano[1][209]]],None])
finestra2 = MKPOL([secondoPiano[0],[[v+1 for v in  secondoPiano[1][202]]],None])
finestra3 = MKPOL([secondoPiano[0],[[v+1 for v in  secondoPiano[1][167]]],None])
finestra4 = MKPOL([secondoPiano[0],[[v+1 for v in  secondoPiano[1][152]]],None])
finestra5 = MKPOL([secondoPiano[0],[[v+1 for v in  secondoPiano[1][161]]],None])

porta1 = MKPOL([secondoPiano[0],[[v+1 for v in  secondoPiano[1][189]]],None])
porta2 = MKPOL([secondoPiano[0],[[v+1 for v in  secondoPiano[1][183]]],None])

porta3 = MKPOL([secondoPiano[0],[[v+1 for v in  secondoPiano[1][195]]],None])
porta4 = MKPOL([secondoPiano[0],[[v+1 for v in  secondoPiano[1][171]]],None])
porta5 = MKPOL([secondoPiano[0],[[v+1 for v in  secondoPiano[1][177]]],None])

finestra1 = S(1)(.1)(finestra1)
finestra2 = S(1)(.1)(finestra2)
finestra3 = S(1)(.1)(finestra3)
finestra4 = S(1)(.1)(finestra4)
finestra5 = S(1)(.1)(finestra5)

porta1 = S(2)(.1)(porta1)
porta2 = S(2)(.1)(porta2)
porta3 = S(1)(.1)(porta3)
porta4 = S(1)(.1)(porta4)
porta5 = S(1)(.1)(porta5)

porta1 = COLOR(BROWN)(T(2)(5.2)(porta1))
porta2 = COLOR(BROWN)(T(2)(2.3)(porta2))
porta3 = COLOR(BROWN)(T(1)(2.55)(porta3))
porta4 = COLOR(BROWN)(T(1)(3.8)(porta4))
porta5 = COLOR(BROWN)(T(1)(3.8)(porta5))

finestra1 =  MATERIAL(glass)(finestra1)
finestra2 =  MATERIAL(glass)(finestra2)
finestra3 =  MATERIAL(glass)(T(1)(6.7)(finestra3))
finestra4 =  MATERIAL(glass)(T(1)(7.8)(finestra4))
finestra5 =  MATERIAL(glass)(T(1)(7.8)(finestra5))

#VIEW(STRUCT([hpc,finestra1,finestra2,finestra3,finestra4,finestra5,porta1,porta2,porta3,porta4,porta5]))

###  utilizzo spline per tagliare piano
controlpoints = [[-0,0],[1,0],[1,1]]
dom = larDomain([32],'simplex')
obj = larMap(larBezier(S1)(controlpoints))(dom)
#VIEW(STRUCT(MKPOLS(obj)))
curva  = STRUCT(MKPOLS(obj))

pts = [[0,0],[0,1],[1,1]]
baseC = JOIN([curva,POLYLINE(pts)])

pareteC = PROD([curva,Q(3)])
pareteC = OFFSET([0.01,0.01,0.01])(pareteC)
pareteC = S([1,2,3])([1.8,1.4,1])(pareteC)
pareteC = T([1,2])([.3,3])(pareteC)

baseC = OFFSET([0.01,0.01,0.01])(baseC)
baseC = S([1,2,3])([1.8,1.4,.3])(baseC)
baseC = T([1,2])([.3,3])(baseC)

#VIEW(STRUCT([pareteC,baseC]))

struttura2 = DIFF([struttura2,baseC])
struttura2 = STRUCT([struttura2,finestra1,finestra2,finestra3,finestra4,finestra5,porta1,porta2,porta3,porta4,porta5,pareteC])

VIEW(struttura2)
ground2 = secondoPiano[0],solidCV

CV = solidCV + exteriorCV
V = secondoPiano[0]
FV = [f for f in larFacets((V,CV),3,len(exteriorCV))[1] if len(f) >= 4]
#VIEW(EXPLODE(1.5,1.5,1.5)(MKPOLS((V,FV))))
BF = boundaryCells(solidCV,FV) 
boundaryFaces = [FV[face] for face in BF] 
B_Rep = V,boundaryFaces 
#VIEW(EXPLODE(1.5,1.5,1.5)(MKPOLS(B_Rep))) 
VIEW(STRUCT(MKPOLS(B_Rep)))
verts,triangles = quads2tria(B_Rep)
C_rep = verts,triangles
VIEW(STRUCT(MKPOLS([verts,triangles])))

#objExporter((verts,triangles), "/Users/andreadodero/Desktop/secondoPiano.obj")
