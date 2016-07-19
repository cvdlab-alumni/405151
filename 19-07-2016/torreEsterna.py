from larlib import *

def VIEWNumbers(numberSize):
	def VIEWNumbers0(V,EV,FV=[],CV=[]):
		submodel = STRUCT(MKPOLS((V,EV)))
		VV = AA(LIST)(range(len(V)))
		VIEW(larModelNumbering(1,1,1)(V,[VV,[],FV,CV],submodel,numberSize))
	return VIEWNumbers0

h = 3./24
H = INTERVALS(h)(1)

""" creazione torri """

filename = "torreesterna/esterna.svg"
lines = svg2lines(filename)
V,EV = lines2lar(lines,True)

#VIEWNumbers(.05)(V,EV)
esterna = STRUCT(MKPOLS((V,EV))) 
esterna = OFFSET([.0025,.0025])(esterna) 
esternaWalls = PROD([ esterna, H ]) 

esternaWallsSpec = R([1,3])(PI)(esternaWalls)
esternaWallsSpec = T(3)(0.125)(esternaWallsSpec)


filename = "torreesterna/pavimento2.svg"
lines = svg2lines(filename)

V,EV = lines2lar(lines,True) 
pavimento2 = STRUCT(MKPOLS((V,EV)))
towerFloor2 = SOLIDIFY(pavimento2) 

pavimento2 = PROD([ towerFloor2, INTERVALS(0.01)(1) ])

pavimento2Spec = R([1,3])(PI)(pavimento2)
pavimento2Spec = T(3)(0.01)(pavimento2Spec)


torreEsterna = TREE(TOP)([ esternaWalls, pavimento2, esternaWalls, 
	pavimento2, esternaWalls, pavimento2, esternaWalls, 
	pavimento2, esternaWalls, pavimento2 ])

torreEsternaSpec = TREE(TOP)([ esternaWallsSpec, pavimento2Spec, esternaWallsSpec, 
	pavimento2Spec, esternaWallsSpec, pavimento2Spec, esternaWallsSpec, 
	pavimento2Spec, esternaWallsSpec, pavimento2Spec ])

torreEsterna = R([1,2])(PI/2)(torreEsterna)
torreEsterna = S([1,2])([.45,.45])(torreEsterna)

torreEsternaSpec = R([1,2])(PI/2)(torreEsternaSpec)
torreEsternaSpec = S([1,2])([.45,.45])(torreEsternaSpec)
