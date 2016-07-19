from larlib import * 

def VIEWNumbers(numberSize):
	def VIEWNumbers0(V,EV,FV=[],CV=[]):
		submodel = STRUCT(MKPOLS((V,EV)))
		VV = AA(LIST)(range(len(V)))
		VIEW(larModelNumbering(1,1,1)(V,[VV,[],FV,CV],submodel,numberSize))
	return VIEWNumbers0

def funScala(l,h,p,n):
	scalino = CUBOID([l,h,p])
	scala = scalino
	for i in range(1,n):
		scala = STRUCT([scala, T([2,3])([h*i,p*i])(scalino)])
	return scala


piano = T([2,3])([1.6,1.6])(CUBOID([1,1,.2])) 
scala = funScala(1,.2,.2,8)
scalaTemp = funScala(1,.2,.2,12)

scala2 = R([1,2])(PI/2)(scalaTemp)
scala2 = T([2,3])([1.6,1.6])(scala2)
scalaLeft = STRUCT([scala,piano,scala2])
scalaLeft = S([1,2,3])([.096,.096,.03])(scalaLeft)
scalaLeft = T([1,2])([.275,.0625])(scalaLeft)


scala3 = R([1,2])(-PI/2)(scalaTemp)
scala3 = T([1,2,3])([1,2.6,1.6])(scala3)
scalaSpec = STRUCT([scala,piano,scala3])
scalaSpec = S([1,2,3])([.096,.096,.03])(scalaSpec)
scalaSpec = T([1,2])([.635,.0625])(scalaSpec)

h = 3./24
H = INTERVALS(h)(1)
 
h2 = 2*( (3./24)/3 )
H2 = INTERVALS(h2)(1)

h3 = 1*( (3./24)/3 )
H3 = INTERVALS(h3)(1)

filename = "building/piscina.svg"
lines = svg2lines(filename)

V,EV,FV,polygons = larFromLines(lines,True)
#VIEWNumbers(.1)(V,EV,FV)
#VIEW(larModelNumbering(1,1,1)(V,[VV,EV,FV],submodel,0.1))
#V,EV = lines2lar(lines,True)
#print [ FV[12], FV[15], FV[21],FV[18], FV[20], FV[17] ]

piscinaGrande = (V,[FV[k] for k in [11,15,16,13,6,14]])
piscinaPiccola = (V,[FV[k] for k in [17,8,4,9,12]])
piscinaPiccolissima = (V,[FV[k] for k in [10,5,7]])

vaso1 = (V,[FV[k] for k in [19,21,18,20]])
vaso2 = (V,[FV[k] for k in [0,1,2,3]])

piscinaGrande = OFFSET([.01,.01])(STRUCT(MKPOLS(piscinaGrande)))
piscinaGrande = PROD([piscinaGrande, H])

vaso1 = OFFSET([.01,.01])(STRUCT(MKPOLS(vaso1)))
vaso1 = PROD([vaso1, H])
vaso2 = OFFSET([.01,.01])(STRUCT(MKPOLS(vaso2)))
vaso2 = PROD([vaso2, H])
#VIEW(piscinaGrande)

piscinaPiccola = OFFSET([.01,.01])(STRUCT(MKPOLS(piscinaPiccola)))
piscinaPiccola = PROD([piscinaPiccola, H2])

piscinaPiccolissima = OFFSET([.01,.01])(STRUCT(MKPOLS(piscinaPiccolissima)))
piscinaPiccolissima = PROD([piscinaPiccolissima, H3])


scalinata = STRUCT([piscinaGrande, piscinaPiccola, piscinaPiccolissima, vaso2,vaso1, scalaLeft, scalaSpec])

 