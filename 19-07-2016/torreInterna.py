from larlib import *
from ringhiera import *
from finestra import *

def VIEWNumbers(numberSize):
	def VIEWNumbers0(V,EV,FV=[],CV=[]):
		submodel = STRUCT(MKPOLS((V,EV)))
		VV = AA(LIST)(range(len(V)))
		VIEW(larModelNumbering(1,1,1)(V,[VV,[],FV,CV],submodel,numberSize))
	return VIEWNumbers0

h = 3./24
H = INTERVALS(h)(1)


""" creazione scala """

def funScala(l,h,p,n):
	scalino = CUBOID([l,h,p])
	scala = scalino
	for i in range(1,n):
		scala = STRUCT([scala, T([2,3])([h*i,p*i])(scalino)])
	return scala


base =  CUBOID([1,.8,.2])
piano = T([2,3])([1.8,1.8])(CUBOID([1,1,.2])) 
pianerottolo = T([1,2,3])([-1.5,2.6,1.8])(CUBOID([2.5,1,.2])) 
c = funScala(1,.2,.2,9)
rampa = STRUCT([base,T([2])([.8])(c),pianerottolo])
rampaSpec = STRUCT([base,T([2])([.8])(c),T(1)(1.5)(pianerottolo)])


rampa2 = STRUCT([c,T([2,3])([1.8,1.6])(base)])
rampa2 =  R([1,2])(PI)(rampa2)
rampa2 = T([1,2,3])([-.5,2.6,1.8])(rampa2)
rampa2Spec = T(1)(3)(rampa2)
scala = STRUCT([rampa,rampa2])

scalaSpec = STRUCT([rampaSpec,rampa2Spec])
#VIEW(STRUCT([scalaSpec,T(1)(6)(scala)]))


scala = S([1,2,3])([.075,.08,.033])(scala)
scala = T([1,2])([.42,.59])(scala)

scalaSpec = S([1,2,3])([.075,.08,.035])(scalaSpec)
scalaSpec = T([1,2,3])([-.495,.59,-.125])(scalaSpec)

""" creazione torre interna """

filename = "torreinterna/tettoTorretta.svg"
lines = svg2lines(filename)
V,EV = lines2lar(lines,True) 
#VIEWNumbers(.05)(V,EV)
tettoTorretta = STRUCT(MKPOLS((V,EV)))
tettoTorretta = SOLIDIFY(tettoTorretta)
tettoTorretta = PROD([ tettoTorretta, INTERVALS(0.01)(1) ])
#VIEW(tettoTorretta)
tettoTorrettaSpec = R([1,3])(PI)(tettoTorretta)
tettoTorrettaSpec = T(3)(.01)(tettoTorrettaSpec)


filename = "torreinterna/pavimentoTorretta.svg"
lines = svg2lines(filename)
V,EV = lines2lar(lines,True) 
#VIEWNumbers(.05)(V,EV)
pavimentoTorretta = STRUCT(MKPOLS((V,EV)))
pavimentoTorretta = SOLIDIFY(pavimentoTorretta)
pavimentoTorretta = PROD([ pavimentoTorretta, INTERVALS(0.01)(1) ])
pavimentoTorrettaSpec = R([1,3])(PI)(pavimentoTorretta)
pavimentoTorrettaSpec = T(3)(.01)(pavimentoTorrettaSpec)
#VIEW(pavimentoTorretta)

filename = "torreinterna/tetto.svg"
lines = svg2lines(filename)
V,EV = lines2lar(lines,True) 
#VIEWNumbers(.05)(V,EV)
tetto = STRUCT(MKPOLS((V,EV)))
tetto = SOLIDIFY(tetto)
tetto = PROD([ tetto, INTERVALS(0.01)(1) ])
tettoSpec = R([1,3])(PI)(tetto)
tettoSpec = T(3)(.01)(tettoSpec)

filename = "torreinterna/pavimento.svg"
lines = svg2lines(filename)
V,EV = lines2lar(lines,True) 
#VIEWNumbers(.05)(V,EV)
towerFloor = STRUCT(MKPOLS((V,EV)))
towerFloor = SOLIDIFY(towerFloor)
pavimento = PROD([ towerFloor, INTERVALS(0.01)(1) ])
pavimentoSpec = R([1,3])(PI)(pavimento)
pavimentoSpec = T(3)(.01)(pavimentoSpec)


filename = "torreinterna/pavimentoSecondo.svg"
lines = svg2lines(filename)
V,EV = lines2lar(lines,True) 
#VIEWNumbers(.05)(V,EV)
pavimentoSecondo = STRUCT(MKPOLS((V,EV)))
pavimentoSecondo = SOLIDIFY(pavimentoSecondo)
pavimentoSecondo = PROD([ pavimentoSecondo, INTERVALS(0.01)(1) ])

pavimentoSecondoSpec = R([1,3])(PI)(pavimentoSecondo)
pavimentoSecondoSpec = T(3)(.01)(pavimentoSecondoSpec) 

#VIEW(pavimentoSecondo)

filename = "torreinterna/pavimentoPrimo.svg"
lines = svg2lines(filename)
V,EV = lines2lar(lines,True) 
#VIEWNumbers(.05)(V,EV)
pavimentoPrimo = STRUCT(MKPOLS((V,EV)))
pavimentoPrimo = SOLIDIFY(pavimentoPrimo)
pavimentoPrimo = PROD([ pavimentoPrimo, INTERVALS(0.01)(1) ])
pavimentoPrimoSpec = R([1,3])(PI)(pavimentoPrimo)
pavimentoPrimoSpec = T(3)(.01)(pavimentoPrimoSpec) 


#VIEW(pavimentoPrimo)


filename = "torreinterna/torretta.svg"
lines = svg2lines(filename)
V,EV = lines2lar(lines,True)

torretta = STRUCT(MKPOLS((V,EV)))
torretta = OFFSET([.0025,.0025])(torretta)
torrettaWalls = PROD([ torretta, H ])
torrettaWallsSpec = R([1,3])(PI)(torrettaWalls)


torrettaWalls = STRUCT([torrettaWalls, T(1)(-.08)(scala)])
torrettaWallsSpec = STRUCT([torrettaWallsSpec,T(1)(.08)(scalaSpec)])
#VIEW(torrettaWalls)
#VIEW(torrettaWallsSpec)

filename = "torreinterna/fondamenta.svg"
lines = svg2lines(filename)
V,EV = lines2lar(lines,True)

muraOblique = (V,[EV[k] for k in [8,18]])
muraOblique = OFFSET([.01,.01])(STRUCT(MKPOLS(muraOblique)))
muraOblique = PROD([muraOblique, H ])

fondamenta = STRUCT(MKPOLS((V,EV)))
fondamenta = OFFSET([.0025,.0025])(fondamenta)
fondamentaWalls = PROD([ fondamenta, H ])
fondamentaWalls = STRUCT([muraOblique, fondamentaWalls])

fondamentaWallsSpec = R([1,3])(PI)(fondamentaWalls)


fondamentaWalls = STRUCT([fondamentaWalls,scala])
fondamentaWallsSpec = STRUCT([fondamentaWallsSpec,scalaSpec])

#VIEW(fondamentaWallsSpec)

fondamentaWallsSpec = T(3)(.125)(fondamentaWallsSpec)
  
lines = svg2lines("torreinterna/terra.svg")
V,EV = lines2lar(lines,True)
pianoterra = STRUCT(MKPOLS((V,EV)))
pianoterra = OFFSET([.0025,.0025])(pianoterra)
pianoterraWalls = PROD([ pianoterra, H ])
pianoterraWalls = STRUCT([pianoterraWalls,scala])

pianoterraWallsSpec = R([1,3])(PI)(pianoterraWalls)
pianoterraWallsSpec = STRUCT([pianoterraWallsSpec,scalaSpec])

pianoterraWallsSpec = T(3)(.125)(pianoterraWallsSpec)

#VIEW(pianoterraWalls)

filename = "torreinterna/pavimentoTerra_1.svg"
lines = svg2lines(filename)
V,FV,EV,polygons = larFromLines(lines,True)
#VIEWNumbers(1)(V,EV,FV)
 
muretto = (V,[EV[k] for k in [0,3,4,5]])
mura = (V,[EV[k] for k in [1,2,6,7]])

#VIEW(STRUCT([COLOR(CYAN)(STRUCT(MKPOLS(muretto))),STRUCT(MKPOLS(mura))]))

muretto = OFFSET([.003,.0025])(STRUCT(MKPOLS(muretto)))
muretto = PROD([muretto, Q(0.05)])
murettoSpec =  R([1,3])(PI)(muretto)
murettoSpec = T(3)(0.05)(murettoSpec) 

V,EV = lines2lar(lines,True) 
towerFloor2 = STRUCT(MKPOLS((V,EV)))
towerFloor2 = SOLIDIFY(towerFloor2)
  
pavimentoTerra = PROD([ towerFloor2, INTERVALS(0.005)(1) ])

pavimentoTerraSpec = R([1,3])(PI)(pavimentoTerra)
pavimentoTerraSpec = T(3)(.005)(pavimentoTerraSpec)

pavimentoTerraSpec = STRUCT([pavimentoTerraSpec, murettoSpec])

pavimentoTerra = STRUCT([ pavimentoTerra,muretto ])
pianoTerra = STRUCT([ pavimentoTerra , T([3])([-.001])(pianoterraWalls) ])
pianoTerraSpec = STRUCT([ pavimentoTerraSpec , pianoterraWallsSpec ])

#VIEW(STRUCT([pianoTerra,pianoTerraSpec]))

lines = svg2lines("torreinterna/primo.svg")
V,EV = lines2lar(lines,True) 
primopiano = STRUCT(MKPOLS((V,EV)))

#VIEW(primopiano)
primopiano = OFFSET([.0025,.0025])(primopiano)
#VIEW(SKEL_1(primopiano))
primopianoWalls = PROD([ primopiano, H ])
primopianoWalls = STRUCT([primopianoWalls,scala])
primopianoWallsSpec = R([1,3])(PI)(primopianoWalls)
primopianoWallsSpec = T(3)(0.125)(primopianoWallsSpec)

primoPiano = STRUCT([ pavimentoSecondo , T([3])([-.001])(primopianoWalls) ])
#VIEW(primoPiano)

primoPianoSpec = STRUCT([ pavimentoSecondoSpec , T([3])([-.001])(primopianoWallsSpec) ])

#VIEW(STRUCT([primoPiano, primoPianoSpec]))

lines = svg2lines("torreinterna/secondopiano.svg")
V,EV = lines2lar(lines,True) 
 
secondopiano = STRUCT(MKPOLS((V,EV)))
#VIEW(secondopiano)
secondopiano = OFFSET([.0025,.0025])(secondopiano)
#VIEW(SKEL_1(secondopiano))
secondopianoWalls = PROD([ secondopiano, H ])

secondopianoWallsSpec = R([1,3])(PI)(secondopianoWalls)
secondopianoWallsSpec =  STRUCT([ secondopianoWallsSpec, scalaSpec ])


secondopianoWalls = STRUCT([ secondopianoWalls,scala])
secondopianoWalls = STRUCT([ secondopianoWalls, muretto ])


secondopianoWallsSpec = T(3)(0.125)(secondopianoWallsSpec)
pavimentoPrimoSpec = STRUCT([pavimentoPrimoSpec, murettoSpec])


#VIEW(STRUCT([ secondopianoWalls, secondopianoWallsSpec ]))

secondoPiano = STRUCT([ pavimentoPrimo , T([3])([-.001])(secondopianoWalls) ])
secondoPianoSpec = STRUCT([ pavimentoPrimoSpec , secondopianoWallsSpec ])

ringhiera1 = STRUCT(ringhiera(10))
ringhiera1 = S([1,2,3])([.025,.025,.02])(ringhiera1)
ringhiera1 = R([1,2])(PI/2)(ringhiera1)
ringhiera1 = T([1,2])([-.15,.22])(ringhiera1)

ringhiera2 = STRUCT(ringhiera(10))
ringhiera2 = S([1,2,3])([.018,.018,.02])(ringhiera2)
ringhiera2 = R([1,2])(PI/2)(ringhiera2)
ringhiera2 = T([1,2])([-.59,.19])(ringhiera2)

ringhiera3 = STRUCT(ringhiera(10))
ringhiera3 = S([1,2,3])([.025,.025,.02])(ringhiera3)
ringhiera3 = R([1,2])(PI/2)(ringhiera3)
ringhiera3 = T([1,2])([.375,.22])(ringhiera3)

ringhiera4 = STRUCT(ringhiera(10))
ringhiera4 = S([1,2,3])([.018,.018,.02])(ringhiera4)
ringhiera4 = R([1,2])(PI/2)(ringhiera4)
ringhiera4 = T([1,2])([.75,.19])(ringhiera4)

secondoPiano = STRUCT([secondoPiano, ringhiera3, ringhiera4])
#VIEW(secondoPiano)

secondoPianoSpec = STRUCT([secondoPianoSpec, ringhiera2, ringhiera1])
#VIEW(secondoPianoSpec)


#VIEW(STRUCT([secondoPianoSpec, secondoPiano]))
 
lines = svg2lines("torreinterna/ultimo.svg")
V,EV = lines2lar(lines,True) 

ultimopiano = STRUCT(MKPOLS((V,EV)))
#VIEW(ultimopiano)
ultimopiano = OFFSET([.0025,.0025])(ultimopiano)
#VIEW(SKEL_1(ultimopiano))
ultimopianoWalls = PROD([ ultimopiano, H ])
ultimopianoWallsSpec = R([1,3])(PI)(ultimopianoWalls)
ultimopianoWallsSpec =  T(3)(0.125)(ultimopianoWallsSpec) 

ultimopiano = STRUCT([ pavimentoSecondo , T([3])([-.001])(ultimopianoWalls), T([3])([.12])(tetto) ])
ultimopianoSpec = STRUCT([ pavimentoSecondoSpec , T([3])([-.001])(ultimopianoWallsSpec), T([3])([.12])(tettoSpec) ])

finestra1 = finestra()
finestra1 = S([1,2,3])([.17,.1,.11])(finestra1)
finestra1 = T([1,2,3])([-.75,.19,.01])(finestra1)
 
finestra2 = finestra()
finestra2 = S([1,2,3])([.25,.1,.11])(finestra2)
finestra2 = T([1,2,3])([-.38,.2,.01])(finestra2)

finestra3 = finestra()
finestra3 = S([1,2,3])([.17,.1,.11])(finestra3)
finestra3 = T([1,2,3])([.585,.19,.01])(finestra3)
 
finestra4 = finestra()
finestra4 = S([1,2,3])([.25,.1,.11])(finestra4)
finestra4 = T([1,2,3])([.14,.2,.01])(finestra4)

ultimopiano = STRUCT([ultimopiano, finestra3, finestra4])
ultimopianoSpec = STRUCT([ultimopianoSpec, finestra1, finestra2])

torretta = STRUCT([ torrettaWalls , T(3)(.115)(pavimentoTorretta) ])
lasttorretta = STRUCT([ torrettaWalls , T(3)(.115)(tettoTorretta) ])
#VIEW(torretta)

torrettaSpec = STRUCT([ torrettaWallsSpec , T([3])([-.01])(pavimentoTorrettaSpec) ])
lasttorrettaSpec = STRUCT([ torrettaWallsSpec , tettoTorrettaSpec ])
 

torrettaInterna = TREE(TOP)([ torretta, torretta , torretta, torretta, lasttorretta])
#VIEW(torrettaInterna)

torrettaInternaSpec = TREE(TOP)([ torrettaSpec, torrettaSpec , torrettaSpec, torrettaSpec, lasttorrettaSpec])

torreInterna = TREE(TOP)([ fondamentaWalls, pianoTerra , primoPiano, secondoPiano, ultimopiano])

torreInternaSpec = TREE(TOP)([ fondamentaWallsSpec, pianoTerraSpec, primoPianoSpec, secondoPianoSpec, ultimopianoSpec ])
#VIEW(torreInternaSpec)

 