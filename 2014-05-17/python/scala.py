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



def funScala(l,h,p,n):
	scalino = CUBOID([l,h,p])
	scala = scalino
	for i in range(1,n):
		scala = STRUCT([scala, T([2,3])([h*i,p*i])(scalino)])
	return scala



piano = T([2,3])([1,1])(CUBOID([1,1,.2]))
a = funScala(1,.2,.2,2)
a = R([1,2])(-PI/2)(a)
a = T([1,2,3])([1,2,1.2])(a)
piano2 = T([1,3])([1.4,.6])(piano)
b = funScala(1,.2,.2,5)
b = R([1,2])(PI)(b)
b = T([1,2,3])([2.4,1,1.8])(b)
c = funScala(1,.2,.2,5)

scala = STRUCT([c,piano,a,piano2,b])


