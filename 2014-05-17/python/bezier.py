
dom1D = INTERVALS(1)(32)
dom2D = PROD([dom1D,dom1D])

def bezierS1(controlpoints):
   return BEZIER(S1)(controlpoints)

def bezierS2(f):
   return BEZIER(S2)(f)

def bezierMappata_1D(controlpoints):
   return MAP(bezierS1(controlpoints))(INTERVALS(1)(32))


def bezierMappata_2D(functions):
   return MAP(BEZIER(S2)(functions))(dom2D)

def ColorPlasm(color):
# curve

m1r = [[0, 0,0], [4.55, -6.26,0], [10, -9.39,0], [14,0,0]]
r1 = BEZIER(S1)(m1r)


m1r = [[0, 0,0], [14,0,0]]
r2 = BEZIER(S1)(m1r)
r1 = bezierMappata_2D([r1,r2])
VIEW(r1)

m1r = [[0, 0,0.5], [14,0,0.5]]
r2 = BEZIER(S1)(m1r)

i2 = [[0, 0,0.5], [4.55, -6.26,0.5], [10, -9.39,0.5], [14,0,0.5]]
r22 = BEZIER(S1)(i2)

r2 = bezierMappata_2D([r22,r2])
VIEW(r2)
r2=STRUCT([r2,r1])
i2 = [[0, 0,0.5], [4.55, -6.26,0.5], [10, -9.39,0.5], [14,0,0.5]]
r11 = BEZIER(S1)(i2)

m1r = [[0, 0,0], [4.55, -6.26,0], [10, -9.39,0], [14,0,0]]
r22 = BEZIER(S1)(m1r)

r3 = bezierMappata_2D([r22,r11])
VIEW(r3)
r2=STRUCT([r2,r3])

a = [[0, 0,0], [14,0,0]]
aa = BEZIER(S1)(a)

b = [[0, 0,0.5], [14,0,0.5]]
bb = BEZIER(S1)(b)

r3 = bezierMappata_2D([aa,bb])
VIEW(r3)
r2=STRUCT([r2,r3])
giardino1 = COLOR(ColorPlasm([23,114,69]))(r2)

m1r = [[25, 10,0],[10,5,0],[16, 0,0], [38, -30.26,0], [38, -30.26,0], [38, -30.26,0], [38, -30.26,0],[38, -30.26,0],[38, -30.26,0], [45, -2.39,0], [55,-40,0],[60,0,0],[56,10,0]]
r1 = BEZIER(S1)(m1r)
m1r = [[25, 0,0], [45,0,0]]
r2 = BEZIER(S1)(m1r)
r1 = bezierMappata_2D([r1,r2])
VIEW(r1)
m1r = [[25, 0,0.5], [45,0,0.5]]
r2 = BEZIER(S1)(m1r)
i2 = [[25, 10,0.5],[10,5,0.5],[16, 0,0.5], [38, -30.26,0.5], [38, -30.26,0.5], [38, -30.26,0.5], [38, -30.26,0.5], [38, -30.26,0.5], [38, -30.26,0.5], [45, -2.39,0.5], [55,-40,0.5],[60,0,0.5],[56,10,0.5]]
r22 = BEZIER(S1)(i2)
r2 = bezierMappata_2D([r22,r2])
VIEW(r2)
r2=STRUCT([r2,r1])
r11 = BEZIER(S1)(i2)
m1r = [[25, 10,0],[10,5,0],[16, 0,0], [38, -30.26,0], [38, -30.26,0], [38, -30.26,0], [38, -30.26,0],[38, -30.26,0],[38, -30.26,0], [45, -2.39,0], [55,-40,0],[60,0,0],[56,10,0]]
r22 = BEZIER(S1)(m1r)
r3 = bezierMappata_2D([r22,r11])
VIEW(r3)
r2=STRUCT([r2,r3])
a = [[25, 0,0], [45,0,0]]
aa = BEZIER(S1)(a)
b = [[25, 0,0.5], [45,0,0.5]]
bb = BEZIER(S1)(b)
r3 = bezierMappata_2D([aa,bb])
VIEW(r3)
giardino2=STRUCT([r2,r3])
giardino2 = R([1,2])(PI/2)(giardino2)
giardino2 = T([1,2])([60,-20])(giardino2)
giardino2 = COLOR(ColorPlasm([23,114,69]))(giardino2)


piccolosopra = [[0, 5,0.5], [-20, 18,0.5], [0,31,0.5]]
piccolosopra = BEZIER(S1)(piccolosopra)
piccolosotto = [[0, 5,0], [-20, 18,0], [0,31,0]]
piccolosotto = BEZIER(S1)(piccolosotto)


r1 = bezierMappata_2D([piccolosotto,piccolosopra])
VIEW(r1)

grandesopra = [[0, 0,0.5], [-25, 18,0.5], [0,36,0.5]]
grandesopra = BEZIER(S1)(grandesopra)
grandesotto = [[0, 0,0], [-25, 18,0], [0,36,0]]
grandesotto = BEZIER(S1)(grandesotto)

r2 = bezierMappata_2D([grandesotto,grandesotto])
VIEW(r2)
r3 = bezierMappata_2D([grandesotto,piccolosotto])
VIEW(r3)
r4 = bezierMappata_2D([grandesopra,piccolosopra])
VIEW(r4)

giardino3=STRUCT([r1,r2,r3,r4])
grandesopra2 = [[0, 0,40], [-25, 18,40], [0,36,40]]
grandesopra2 = BEZIER(S1)(grandesopra2)

#giardino4 = T([3])([41])(giardino3)

r5 = bezierMappata_2D([grandesopra2,grandesotto])
VIEW(r5)
giardino3=STRUCT([giardino3,r5])

piccolosopra2 = [[0, 5,40], [-20, 18,40], [0,31,40]]
piccolosopra2 = BEZIER(S1)(piccolosopra2)

#giardino4 = T([3])([41])(giardino3)

r5 = bezierMappata_2D([piccolosotto,piccolosopra2])
VIEW(r5)
giardino3=STRUCT([giardino3,r5])

r5 = bezierMappata_2D([grandesopra2,piccolosopra2])
VIEW(r5)
giardino3=STRUCT([giardino3,r5])
giardino3 = COLOR(ColorPlasm([23,114,69]))(giardino3)
VIEW(giardino3)
