from pyplasm import *
from fn import *

####################################################################################################
####################################################################################################
# ottagono di raggio 10

lato = 10*SQRT(2-SQRT(2))
lato = Q(lato)

fun = ruota(40)

pts1 = [0,10]
pts2 = [0,-10]
pts3 = [10,0]
pts4 = [-10,0]

obj1 = MKPOL([[pts1], [[1]] ,None])
obj2 = MKPOL([[pts2], [[1]] ,None])
obj3 = MKPOL([[pts3], [[1]] ,None])
obj4 = MKPOL([[pts4], [[1]] ,None])

obj5 = MAP(fun)(obj1)
obj6 = MAP(fun)(obj2)
obj7 = MAP(fun)(obj3)
obj8 = MAP(fun)(obj4)


lista = STRUCT([obj1,obj2,obj3,obj4,obj5,obj6,obj7,obj8])

lato1 = JOIN([obj1,obj6])
lato2 = JOIN([obj2,obj5])
lato3 = JOIN([obj3,obj8])
lato4 = JOIN([obj4,obj7])
lato5 = JOIN([obj5,obj4])
lato6 = JOIN([obj6,obj3])
lato7 = JOIN([obj7,obj1])
lato8 = JOIN([obj8,obj2])

perimetro = STRUCT([lato1,lato2,lato3,lato4,lato5,lato6,lato7,lato8])

parete_north = STRUCT([lato1,lato6])
parete_south = STRUCT([lato3,lato8])
parete_east = STRUCT([lato5,lato2])
parete_west = STRUCT([lato7,lato4])

north3d = PROD([parete_north, Q(10)])
south3d = PROD([parete_south, Q(10)])
east3d = PROD([parete_east, Q(10)])
west3d = PROD([parete_west, Q(10)])

VIEW(north3d)
VIEW(STRUCT([north3d,south3d]))
VIEW(STRUCT([north3d,west3d,south3d]))
VIEW(STRUCT([north3d,south3d,west3d,east3d]))

mura_esterne = STRUCT([north3d,south3d,west3d,east3d])

####################################################################################################
####################################################################################################
# ottagono di raggio 5

lato_1 = 5*SQRT(2-SQRT(2))
lato_1 = Q(lato_1)

pts_1 = [0,5]
pts_2 = [0,-5]
pts_3 = [5,0]
pts_4 = [-5,0]

obj_1 = MKPOL([[pts_1], [[1]] ,None])
obj_2 = MKPOL([[pts_2], [[1]] ,None])
obj_3 = MKPOL([[pts_3], [[1]] ,None])
obj_4 = MKPOL([[pts_4], [[1]] ,None])

obj_5 = MAP(fun)(obj_1)
obj_6 = MAP(fun)(obj_2)
obj_7 = MAP(fun)(obj_3)
obj_8 = MAP(fun)(obj_4)


lista = STRUCT([obj_1,obj_2,obj_3,obj_4,obj_5,obj_6,obj_7,obj_8])

lato_1 = JOIN([obj_1,obj_6])
lato_2 = JOIN([obj_2,obj_5])
lato_3 = JOIN([obj_3,obj_8])
lato_4 = JOIN([obj_4,obj_7])
lato_5 = JOIN([obj_5,obj_4])
lato_6 = JOIN([obj_6,obj_3])
lato_7 = JOIN([obj_7,obj_1])
lato_8 = JOIN([obj_8,obj_2])

perimetro_1 = STRUCT([lato_1,lato_2,lato_3,lato_4,lato_5,lato_6,lato_7,lato_8])

parete_north_1 = STRUCT([lato_1,lato_6])
parete_south_1 = STRUCT([lato_3,lato_8])
parete_east_1 = STRUCT([lato_5,lato_2])
parete_west_1 = STRUCT([lato_7,lato_4])

north3d_1 = PROD([parete_north_1, Q(10)])
south3d_1 = PROD([parete_south_1, Q(10)])
east3d_1 = PROD([parete_east_1, Q(10)])
west3d_1 = PROD([parete_west_1, Q(10)])

VIEW(north3d_1)
VIEW(STRUCT([north3d_1,south3d_1]))
VIEW(STRUCT([north3d_1,west3d_1,south3d_1]))
VIEW(STRUCT([north3d_1,south3d_1,west3d_1,east3d_1]))

mura_interne = STRUCT([north3d_1,south3d_1,west3d_1,east3d_1])

####################################################################################################
####################################################################################################
# ottagono di raggio 2

lato_1b = 2*SQRT(2-SQRT(2))
lato_1b = Q(lato_1b)

pts_1b = [0,2]
pts_2b = [0,-2]
pts_3b = [2,0]
pts_4b = [-2,0]

obj_1b = MKPOL([[pts_1b], [[1]] ,None])
obj_2b = MKPOL([[pts_2b], [[1]] ,None])
obj_3b = MKPOL([[pts_3b], [[1]] ,None])
obj_4b = MKPOL([[pts_4b], [[1]] ,None])

obj_5b = MAP(fun)(obj_1b)
obj_6b = MAP(fun)(obj_2b)
obj_7b = MAP(fun)(obj_3b)
obj_8b = MAP(fun)(obj_4b)


lista = STRUCT([obj_1b,obj_2b,obj_3b,obj_4b,obj_5b,obj_6b,obj_7b,obj_8b])

lato_1b = JOIN([obj_1b,obj_6b])
lato_2b = JOIN([obj_2b,obj_5b])
lato_3b = JOIN([obj_3b,obj_8b])
lato_4b = JOIN([obj_4b,obj_7b])
lato_5b = JOIN([obj_5b,obj_4b])
lato_6b = JOIN([obj_6b,obj_3b])
lato_7b = JOIN([obj_7b,obj_1b])
lato_8b = JOIN([obj_8b,obj_2b])

perimetro_2 = STRUCT([lato_1b,lato_2b,lato_3b,lato_4b,lato_5b,lato_6b,lato_7b,lato_8b])

parete_north_1b = STRUCT([lato_1b,lato_6b])
parete_south_1b = STRUCT([lato_3b,lato_8b])
parete_east_1b = STRUCT([lato_5b,lato_2b])
parete_west_1b = STRUCT([lato_7b,lato_4b])

north3d_1b = PROD([parete_north_1b, Q(10)])
south3d_1b = PROD([parete_south_1b, Q(10)])
east3d_1b = PROD([parete_east_1b, Q(10)])
west3d_1b = PROD([parete_west_1b, Q(10)])

mura_torre = STRUCT([north3d_1b,south3d_1b,west3d_1b,east3d_1b])

VIEW(north3d_1b)
VIEW(STRUCT([north3d_1b,south3d_1b]))
VIEW(STRUCT([north3d_1b,west3d_1b,south3d_1b]))
VIEW(STRUCT([north3d_1b,south3d_1b,west3d_1b,east3d_1b]))

####################################################################################################
####################################################################################################

mura_castello = STRUCT([mura_interne,mura_esterne])

VIEW(mura_castello)

mura_torri = STRUCT([T([1,2])([7.5,6.8])(mura_torre), T([1,2])([-7.5,6.8])(mura_torre),
	T([1,2])([7.5,-6.8])(mura_torre), T([1,2])([-7.5,-6.8])(mura_torre),
	T([1,2])([0,10])(mura_torre), T([1,2])([0,-10])(mura_torre),
	T([1,2])([10,0])(mura_torre),T([1,2])([-10,0])(mura_torre) ])

VIEW(STRUCT([mura_castello,mura_torri]))


####################################################################################################
####################################################################################################


#parete_porta = PROD([parete_north,Q(10)])
#ptsX = [0,0]
#ptsY = [0,2.3]
#ptsX = MK(ptsX)
#ptsY = MK(ptsY)
#lato_porta = JOIN([ptsX,ptsY])

#fun = ruota(20)

#lato_porta = MAP(fun)(lato_porta)
#lato_porta = T(1)(5)(lato_porta)
#lato_porta = T(2)(7.76)(lato_porta)

#VIEW(STRUCT([lato_porta,lato1]))

#porta = PROD([lato_porta,Q(4)])
#muro_con_porta = STRUCT([COLOR(RED)(porta), parete_porta])

#VIEW(muro_con_porta)





