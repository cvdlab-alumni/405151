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
from pianoTerra import *
from primoPiano import *
from secondoPiano import *

DRAW = COMP([STRUCT,MKPOLS])


casa = STRUCT([DRAW(pianoTerra),T(3)(3),DRAW(primoPiano),T(3)(3),DRAW(secondoPiano)])

tetto = S([1,2,3])([8.7,6.7,-.1])(CUBOID([1,1,1]))	
tetto = T(3)(9)(tetto)

casa = STRUCT([casa,tetto])
VIEW(SKEL_1(casa))
VIEW(casa)
