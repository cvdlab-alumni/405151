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

BROWN= Color4f([0.83, 0.65, 0.5, 1.0])
P_GREEN = Color4f([0.05, 0.6, 0.08, 1.0])
P_DGREEN = Color4f([0.06, 0.25, 0, 1.0])
P_DGRAY	= Color4f([0.6, 0.6, 0.6, 1.0])


# piano terra
pianoTerra = assemblyDiagramInit([7,7,2])([[.3,3,.1,4,.1,1,.3],[.3,2.7,.1,1,.1,2,.3],[.3,2.7]])
hpc = SKEL_1(STRUCT(MKPOLS(pianoTerra)))
VIEW(hpc)


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
				73,87,48,93,70,101,107,145,150,113]
			
solidCV = [cell for k,cell in enumerate(pianoTerra[1]) if not (k in emptyChain)]
exteriorCV =  [cell for k,cell in enumerate(pianoTerra[1]) if k in emptyChain]
exteriorCV += exteriorCells(pianoTerra)


## garage chiuso
cell = MKPOL([pianoTerra[0],[[v+1 for v in  pianoTerra[1][146]]],None])
portaGarC = S(1)(.1)(cell)
portaGar = R([1,3])(PI/2)(portaGarC)
portaGar = T([1,3])([2.3,2.3])(portaGar)
### garage aperto
portaGar = COLOR(P_GREEN)(portaGar)



finestra1 = MKPOL([pianoTerra[0],[[v+1 for v in  pianoTerra[1][101]]],None])
finestra2 = MKPOL([pianoTerra[0],[[v+1 for v in  pianoTerra[1][107]]],None])
finestra3 = MKPOL([pianoTerra[0],[[v+1 for v in  pianoTerra[1][113]]],None])
finestra4 = MKPOL([pianoTerra[0],[[v+1 for v in  pianoTerra[1][137]]],None])

porta1 =MKPOL([pianoTerra[0],[[v+1 for v in  pianoTerra[1][123]]],None])
porta2 =MKPOL([pianoTerra[0],[[v+1 for v in  pianoTerra[1][150]]],None])
porta3 =MKPOL([pianoTerra[0],[[v+1 for v in  pianoTerra[1][129]]],None])
porta4 =MKPOL([pianoTerra[0],[[v+1 for v in  pianoTerra[1][93]]],None])


# Materials(want a list of 17 elements(ambientRGBA, diffuseRGBA, specularRGBA, emissionRGBA, shininess)

glass = [0.1,0.2,0.3,1,  0,0,0,0.5,  2,2,2,1, 0,0,0,1, 100]
water = [0.05,0.4,0.4,1,  0,0.3,0.3,0.5,  2,2,2,1, 0,0,0,1, 100]


finestra1 = S(2)(.1)(finestra1)
finestra2 = S(2)(.1)(finestra2)
finestra3 = S(2)(.1)(finestra3)
finestra4 = S(2)(.1)(finestra4)

porta1 = S(2)(.2)(porta1)
porta2 = S(2)(.2)(porta2)
porta3 = S(1)(.2)(porta3)
porta4 = S(1)(.2)(porta4)


finestra1 = MATERIAL(glass)(T(2)(5.8)(finestra1))
finestra2 =  MATERIAL(glass)(T(2)(5.8)(finestra2))
finestra3 =  MATERIAL(glass)(T(2)(5.8)(finestra3))
finestra4 =  MATERIAL(glass)(T(2)(5.8)(finestra4))

porta1 =  COLOR(BROWN)(T(2)(3.4)(porta1))
porta2 =  COLOR(BROWN)(T(2)(3.4)(porta2))
porta3 =  COLOR(BROWN)(T(1)(2.7)(porta3))
porta4 =  COLOR(BROWN)(T(1)(5.9)(porta4))

#VIEW(STRUCT([hpc,porta3,porta4,porta2,porta1,portaGar,finestra4,finestra2,finestra1,finestra3]))

##  finestre salette

struttura = DRAW1((pianoTerra[0],solidCV))
struttura = STRUCT([struttura,porta3,porta4,porta2,porta1,portaGar,finestra4,finestra2,finestra1,finestra3])

#VIEW(struttura)


first = DRAW1((pianoTerra[0],solidCV))
scala = R([1,2])(PI/2)(scala)
first = STRUCT([first, T([1,2,3])([2,3.4,.3])(scala)])
ground0 = pianoTerra[0],solidCV
VIEW(first)

CV = solidCV + exteriorCV
V = pianoTerra[0]
FV = [f for f in larFacets((V,CV),3,len(exteriorCV))[1] if len(f) >= 4]
#VIEW(EXPLODE(1.5,1.5,1.5)(MKPOLS((V,FV))))
BF = boundaryCells(solidCV,FV) 
boundaryFaces = [FV[face] for face in BF] 
B_Rep = V,boundaryFaces 


#VIEW(EXPLODE(1.5,1.5,1.5)(MKPOLS(B_Rep))) 
#VIEW(STRUCT(MKPOLS(B_Rep)))
verts,triangles = quads2tria(B_Rep)


#objExporter((verts,triangles), "/Users/andreadodero/Desktop/pianoTerra.obj")

# orderedObj( "/Users/andreadodero/Desktop/pianoTerra.obj")

