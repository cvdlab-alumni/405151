
from pyplasm import *
from fn import *

#perimetro mura esterne
wall1 = MAP(cerchio(10))(domain(8))
#perimetro mura interne
wall2 = MAP(cerchio(5))(domain(8))
# perimetro mura torri
wall3 = MAP(cerchio(2))(domain(8))

domainfloor1 = PROD([domain(8), INTERVALS(10)(3)])
domainfloor2 = PROD([domain(8), INTERVALS(5)(3)])
domainfloor3 = PROD([domain(8), INTERVALS(2)(3)])

floor1 = MAP(disco)(domainfloor1)
floor2 = MAP(disco)(domainfloor2)
floor3 = MAP(disco)(domainfloor3)

VIEW(floor1)
VIEW(floor2)
VIEW(floor3)


floor = DIFF([floor1,floor2])

VIEW(floor)

floor3 = STRUCT([T([1,2])([7.5,6.8])(floor3), T([1,2])([-7.5,6.8])(floor3),
	T([1,2])([7.5,-6.8])(floor3), T([1,2])([-7.5,-6.8])(floor3),
	T([1,2])([0,10])(floor3), T([1,2])([0,-10])(floor3),
	T([1,2])([10,0])(floor3),T([1,2])([-10,0])(floor3) ])
VIEW(floor3)

floor_3 = T(3)(5)(floor3)
VIEW(floor_3)

#tetto torri
roof3 = T(3)(10)(floor3)
VIEW(roof3)

floor_2 = T(3)(5)(floor)
VIEW(floor_2)

roof =T(3)(10)(floor)
VIEW(roof)

piani_castello = STRUCT([COLOR(RED)(floor),COLOR(GREEN)(floor_2),COLOR(BLUE)(roof),floor3,floor_3,roof3])

#VIEW( STRUCT([floor,COLOR(RED)(floor3)]) )

VIEW(piani_castello)

