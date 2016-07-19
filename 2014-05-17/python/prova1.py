from pyplasm import *
from scipy import *
import os,sys
sys.path.insert(0, '/Users/dodo/UNI/Grafica\ computazionale/lar-cc/lib/py/') 

from larlib import * 
  
DRAW = COMP([VIEW,STRUCT,MKPOLS])
DRAW1 = COMP([STRUCT,MKPOLS])

BROWN= Color4f([0.83, 0.65, 0.5, 1.0])
P_GREEN = Color4f([0.05, 0.6, 0.08, 1.0])
P_DGREEN = Color4f([0.06, 0.25, 0, 1.0])
P_DGRAY	= Color4f([0.6, 0.6, 0.6, 1.0])


# piano terra
pianoTerra = assemblyDiagramInit([1,1,1])([[1,1,1,1,1,1,1],[1,1,1,1,1,2,1],[1,1]])
hpc = SKEL_1(STRUCT(MKPOLS(pianoTerra)))
VIEW(hpc)

