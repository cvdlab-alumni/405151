from larlib import *
from building import *
from torreInterna import *
from torreEsterna import *
from piscina import *

def VIEWNumbers(numberSize):
	def VIEWNumbers0(V,EV,FV=[],CV=[]):
		submodel = STRUCT(MKPOLS((V,EV)))
		VV = AA(LIST)(range(len(V)))
		VIEW(larModelNumbering(1,1,1)(V,[VV,[],FV,CV],submodel,numberSize))
	return VIEWNumbers0

h = 3./24
H = INTERVALS(h)(1)

base =  CUBOID([10,10,.003])
base2 =  CUBOID([2.2,4.2,.003])

 
torreInterna = R([1,2])(PI/2)(torreInterna)
torreInterna = T([1,2])([2,-.256])(torreInterna)
torriInterne = STRUCT([torreInterna, T(2)(1)]*4)

torrettaInterna = R([1,2])(PI/2)(torrettaInterna)
torrettaInterna = T([1,2])([2,4])(torrettaInterna) 
torriInterne = STRUCT([torriInterne, torrettaInterna])

torreEsterna = R([1,2])(PI/2)(torreEsterna)
torreEsterna = T(2)(.5)(torreEsterna)
torriEsterne = STRUCT([torreEsterna, T(2)(1)]*5)

torreInternaSpec = R([1,2])(PI/2)(torreInternaSpec)
torreInternaSpec = T([1,2])([2,-.256])(torreInternaSpec)
torriInterneSpec = STRUCT([torreInternaSpec, T(2)(1)]*4)
torriInterneSpec = R([1,2])(PI)(torriInterneSpec)
torriInterneSpec =  T([1,2])([1 ,2.5])(torriInterneSpec)


torrettaInternaSpec = R([1,2])(-PI/2)(torrettaInternaSpec)
torrettaInternaSpec = T([1,2,3])([-1,4,.125])(torrettaInternaSpec) 
torriInterneSpec = STRUCT([torriInterneSpec, torrettaInternaSpec])
 

torreEsternaSpec = R([1,2])(PI/2)(torreEsternaSpec)
torreEsternaSpec = T([1,2])([1,.5])(torreEsternaSpec)
torriEsterneSpec = STRUCT([torreEsternaSpec, T(2)(1)]*5)
 
palazzo1 = STRUCT([palazzo1, torriInterne, torriEsterne])
palazzo2 =  STRUCT([palazzo2, torriInterneSpec, torriEsterneSpec ]) 

scalinata = T([1,2])([1.85,-.36])(scalinata)
scalinata = S([1,2,3])([1.06,1.01,1.1])(scalinata)

building = STRUCT([palazzo1, T(1)(4)(palazzo2)])

base2 = T([1,2,3])([1.4,.28,.125])(base2)
building =  STRUCT([ base2, building, scalinata ])
#VIEW(STRUCT([base, T([1,2])([2,2])(building)]))
VIEW(building)
 