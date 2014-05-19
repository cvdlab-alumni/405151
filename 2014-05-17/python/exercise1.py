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
from pianoTerra import *
from primoPiano import *
from secondoPiano import *

DRAW = COMP([VIEW,STRUCT,MKPOLS])
DRAW1 = COMP([STRUCT,MKPOLS])

########################## blocco unico ############################

casa = assemblyDiagramInit([1,1,3])([[10],[10],[3.3,3.3,3.3]])

V,CV = casa
hpc = SKEL_1(STRUCT(MKPOLS(casa)))
hpc = cellNumbering (casa,hpc)(range(len(CV)),CYAN,2)
#VIEW(hpc)


casa = diagram2cell(ground2,casa,2)
casa = diagram2cell(ground1,casa,1)
casa = diagram2cell(ground0,casa,0)

V,CV = casa
hpc = SKEL_1(STRUCT(MKPOLS(casa)))
hpc = cellNumbering (casa,hpc)(range(len(CV)),CYAN,2)
#VIEW(hpc)

solidCV = [cell for k,cell in enumerate(casa[1])]
#DRAW((casa[0],solidCV))


first = DRAW1((casa[0],solidCV))
scala = R([1,2])(PI/2)(scala)

pianerottolo = CUBOID([1.2,1.5,.3])
pianerottolo = T([1,2,3])([2,6.5,6.625])(pianerottolo)

first = STRUCT([first, T([1,2,3])([2,5.1,.3])(scala), T([1,2,3])([2,5.3,3.6])(scala), pianerottolo])



VIEW(first)





