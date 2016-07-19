from pyplasm import *
from scipy import *
import os,sys
sys.path.insert(0, '/Users/dodo/UNI/Grafica\ computazionale/lar-cc/lib/py/') 

from larlib import * 

#from lar2psm import *
#from simplexn import *
#from larcc import *
#from largrid import *
#from mapper import *
#from boolean import *
#from sysml import *
#from myfont import *
#from architectural import *



from scala import *
from pianoTerra import struttura
from primoPiano import struttura1
from secondoPiano import struttura2

DRAW = COMP([VIEW,STRUCT,MKPOLS])
DRAW1 = COMP([STRUCT,MKPOLS])


########################## blocco unico ############################


scala = S(1)(.8)(scala)
scala = R([1,2])(PI/2)(scala)
scala= T([1,2])([2.2,3.3])(scala)

scala1 = S([1,2])([.8,1.1])(scala)
scala1 = T([1,2])([.2,-.4])(scala1)

struttura = STRUCT([struttura,scala])
struttura = S(2)(1.05)(struttura)
#VIEW(struttura)
struttura1 = STRUCT([struttura1,scala1])
#VIEW(struttura1)

pianerottolo = CUBOID([1,1,.1])
pianerottolo = T([1,2])([1.8,4.4])(pianerottolo)

struttura2 = STRUCT([struttura2,pianerottolo])


casa = STRUCT([struttura, T(3)(3)(struttura1), T(3)(6)(struttura2)])

VIEW(casa)


####################################################################




