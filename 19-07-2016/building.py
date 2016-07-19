from larlib import *

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
pianerottolo = T([1,2,3])([-1.5,2.6,1.8])(CUBOID([2.2,1,.2])) 
c = funScala(1,.2,.2,9)

rampa = STRUCT([base,T([2])([.8])(c),T(1)(1.5)(pianerottolo)])
rampa2 = STRUCT([c,T([2,3])([1.8,1.6])(base)])
rampa2 =  R([1,2])(PI)(rampa2)
rampa2 = T([1,2,3])([2.2,2.6,1.8])(rampa2)

scala = STRUCT([rampa,rampa2])
#scala = R([1,3])(2*PI)(scala)
scala = R([1,2])(PI)(scala)
scala = S([1,2,3])([.075,.08,.035])(scala)
scala = T([1,2])([.42,.59])(scala)



filename = "building/trave.svg"
lines = svg2lines(filename)
V,EV = lines2lar(lines,True)

#V,FV,EV,polygons = larFromLines(lines)
#VIEWNumbers(.5)(V,EV,FV)

trave = STRUCT(MKPOLS((V,EV)))
trave = SOLIDIFY(trave)
#VIEW(trave)
trave = OFFSET([.0025,.0025])(trave) 
#VIEW(SKEL_1(trave))
trave = PROD([ trave, H ])
trave = R([2,3])(PI/2)(trave)

base =  CUBOID([1,2,.003])
base2 =  CUBOID([.003,4.5,0.111])

base3 =  CUBOID([1,4.5,0.01])

trave = S(2)(.3)(trave)

fila = STRUCT([trave, T(2)(.35)]*13)
fila = STRUCT([ T(2)(0.15)(fila), T([1,3])([1,0.15])(base2)])
fila = STRUCT([fila, T(3)(0.15)(base2)])

fila = TREE(TOP)([fila,base3,fila,base3,fila,base3])

fila = T(3)(-.145)(fila)

#VIEW(fila)

filename = "building/tettoNord.svg"
lines = svg2lines(filename)
V,EV = lines2lar(lines,True)

tettoNord = STRUCT(MKPOLS((V,EV)))
tettoNord = SOLIDIFY(tettoNord)
tettoNord = PROD([ tettoNord, INTERVALS(0.01)(1) ])
#VIEW(tettoNord)
 
tettoNord2 = R([1,3])(PI)(tettoNord)
tettoNord2 = T([1,3])([1,0.1])(tettoNord2)

filename = "building/tettoSud.svg"
lines = svg2lines(filename)
V,EV = lines2lar(lines,True)

tettoSud = STRUCT(MKPOLS((V,EV)))
tettoSud = SOLIDIFY(tettoSud)
tettoSud = PROD([ tettoSud, INTERVALS(0.01)(1) ])

tettoSud2 = R([1,3])(PI)(tettoSud)
tettoSud2 = T([1,3])([1,0.1])(tettoSud2)
#VIEW(tettoSud)


filename = "building/facciataNord.svg"
lines = svg2lines(filename)
V,EV = lines2lar(lines,True)

#VIEWNumbers(.05)(V,EV)
facciataNord = STRUCT(MKPOLS((V,EV)))

#VIEW(facciataNord)
facciataNord = OFFSET([.0025,.0025])(facciataNord)
#VIEW(facciataNord)
#VIEW(SKEL_1(facciataNord))
facciataNord = PROD([ facciataNord, H ])
 

facciataNord2 = R([1,3])(PI)(facciataNord)
facciataNord2 = T([1,3])([1,0.1])(facciataNord2)


filename = "building/pavimentoNord.svg"
lines = svg2lines(filename)

V,EV = lines2lar(lines,True) 
pavimentoNord = STRUCT(MKPOLS((V,EV)))
pavimentoNord = SOLIDIFY(pavimentoNord)
#VIEW(pavimentoNord)

pavimentoNord = PROD([ pavimentoNord, INTERVALS(0.01)(1) ])

pavimentoNord2 = R([1,3])(PI)(pavimentoNord)
pavimentoNord2 = T([1,3])([1,0.1])(pavimentoNord2)

#VIEW(STRUCT([pavimentoNord,pavimentoNord2]))

torreNord = TREE(TOP)([facciataNord,pavimentoNord ]) 
torreTettoNord = TREE(TOP)([facciataNord,tettoNord ]) 

torreNord = STRUCT([torreNord, T(3)(.13)]*4)
torreNord = TREE(TOP)([torreNord ,torreTettoNord])

torreNord = R([1,2])(PI)(torreNord) 
torreNord = S(1)(1.15)(torreNord) 
torreNord = T([1,2])([1.09,0])(torreNord)

VIEW(torreNord)

torreNord2 = TREE(TOP)([facciataNord2,pavimentoNord2 ]) 
torreTettoNord2 = TREE(TOP)([facciataNord2,tettoNord2 ]) 


torreNord2 = STRUCT([torreNord2, T(3)(.13)]*4)
torreNord2 = TREE(TOP)([torreNord2 ,torreTettoNord2])
VIEW(torreNord2)
 
torreNord2 = R([1,2])(PI)(torreNord2) 
torreNord2 = S(1)(1.15)(torreNord2) 
torreNord2 = T([1,2,3])([1.055,0,.025])(torreNord2)

#VIEW(STRUCT([torreNord2, T(1)(1)(torreNord)]))


filename = "building/facciataSud.svg"
lines = svg2lines(filename)
V,EV = lines2lar(lines,True)
#VIEWNumbers(.05)(V,EV)
facciataSud = STRUCT(MKPOLS((V,EV))) 
facciataSud = OFFSET([.0025,.0025])(facciataSud) 
facciataSud = PROD([ facciataSud, H ])


facciataSud2 = R([1,3])(PI)(facciataSud)
facciataSud2 = T([1,3])([1,0.125])(facciataSud2)
#VIEW(facciataSud2)
 
scala = T([1,2])([1.015,.58])(scala)
scala = S([1,2])([0.65,0.54])(scala)

facciataSud = STRUCT([facciataSud, scala])


filename = "building/pavimentoSud.svg"
lines = svg2lines(filename)

V,EV = lines2lar(lines,True) 
pavimentoSud = STRUCT(MKPOLS((V,EV)))
pavimentoSud = SOLIDIFY(pavimentoSud)

pavimentoSud = PROD([ pavimentoSud, INTERVALS(0.01)(1) ])

pavimentoSud2 = R([1,3])(PI)(pavimentoSud)
pavimentoSud2 = T([1,2,3])([1,-0.14,0.01])(pavimentoSud2)
 

torreSud = STRUCT([facciataSud, T([2,3])([0.105,0.124])(pavimentoSud) ])
torreSud = STRUCT([torreSud, T(3)(.13)]*5)
torreSud = R([1,2])(PI)(torreSud)
torreSud = T([1,2])([1,5.2])(torreSud)

torreSud2 = STRUCT([facciataSud2, T([2,3])([0.245,0.124])(pavimentoSud2) ])
torreSud2 = STRUCT([torreSud2, T(3)(.13)]*5)
torreSud2 = R([1,2])(PI)(torreSud2)
torreSud2 = T([1,2])([1,5.2])(torreSud2) 


palazzo1 = STRUCT([torreSud, fila,torreNord])
#VIEW(palazzo1)
palazzo2 = STRUCT([ torreSud2, fila, torreNord2])
#VIEW(palazzo2)
 