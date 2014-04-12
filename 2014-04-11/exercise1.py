import sys
sys.path.insert(0, '/Users/andreadodero/lar-cc/lib/py') 
from pyplasm import *
from larcc import *
from mapper import *
from fn import *

#######################################################################################################
#########################################     base   #################################################

base = S([1,2,3])([200,200,-.1])(CUBOID([1,1,1]))	
base = T([1,2])([-100,-100])(base)

#######################################################################################################
#########################################     piani   #################################################


floor1 = checkModel(larCircle(23)(8))
floor2 = checkModel(larCircle(9)(8))
floor3 = checkModel(larCircle(4)(8))

floor1 = JOIN(MKPOLS(floor1))# base castello
floor2 = JOIN(MKPOLS(floor2)) # base cortile
floor3 = JOIN(MKPOLS(floor3)) # base torri

groundFloor = DIFF([floor1,floor2])
#groundFloor = DIFF([groundFloor,torri])
groundFloor = PROD([Q(0.5),groundFloor])
groundFloor = ROTN([PI,[1,0,1]])(groundFloor) 

firstFloor = T(3)(3)(groundFloor)
secondFloor = T(3)(12)(groundFloor)
roof = T(3)(24)(groundFloor)

cortile = T(3)(3)(floor2)


floor3 = PROD([Q(0.5),floor3])
floor3 = ROTN([PI,[1,0,1]])(floor3)

firstFloorTower = T(3)(3)(floor3)
seconFloorTower = T(3)(12)(floor3)
thirdFloorTower = T(3)(25)(floor3)

piani = STRUCT([groundFloor,firstFloor,secondFloor,roof])

###############################################################################################################
#########################################     mura e torri    #################################################

#perimetro mura esterne
wall1 = MAP(cerchio(23))(domain(8))
wall11 = MAP(cerchio(22.5))(domain(8))
#perimetro mura interne
wall2 = MAP(cerchio(9))(domain(8))
wall22 = MAP(cerchio(8.5))(domain(8))
# perimetro mura torri
wall3 = MAP(cerchio(4))(domain(8))
wall33 = MAP(cerchio(3.5))(domain(8))

mura_esterne = STRUCT([wall1, wall11])
mura_esterne = SOLIDIFY(mura_esterne)
mura_esterne = PROD([Q(24),mura_esterne])
mura_esterne = ROTN([PI,[1,0,1]])(mura_esterne)

mura_interne = STRUCT([wall2, wall22])
mura_interne = SOLIDIFY(mura_interne)
mura_interne = PROD([Q(24),mura_interne])
mura_interne = ROTN([PI,[1,0,1]])(mura_interne)

mura_torri = STRUCT([wall3, wall33])
mura_torri = SOLIDIFY(mura_torri)
mura_torri = PROD([Q(25),mura_torri])
mura_torri = ROTN([PI,[1,0,1]])(mura_torri)

torre = STRUCT([floor3,mura_torri,firstFloorTower,seconFloorTower,thirdFloorTower])

torri = STRUCT([T([1,2])([0,23])(torre),T([1,2])([-23,0])(torre),
	T([1,2])([0,-23])(torre),T([1,2])([23,0])(torre),
	T([1,2])([-17,17])(torre),T([1,2])([17,-17])(torre),
	T([1,2])([-17,-17])(torre),T([1,2])([17,17])(torre)])

piani = DIFF([piani,torri])

castello = STRUCT([base,mura_interne, mura_esterne, piani, torri])

#VIEW(castello)