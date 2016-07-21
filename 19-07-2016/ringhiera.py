from larlib import *

def VIEWNumbers(numberSize):
	def VIEWNumbers0(V,EV,FV=[],CV=[]):
		submodel = STRUCT(MKPOLS((V,EV)))
		VV = AA(LIST)(range(len(V)))
		VIEW(larModelNumbering(1,1,1)(V,[VV,[],FV,CV],submodel,numberSize))
	return VIEWNumbers0


from pyplasm import *

# point function
def sphere1(p): 
	return [COS(p[0]), SIN(p[0])]

# generator of domain decomp
def domain(n): 
		return INTERVALS(2*PI)(n)

# geometric value (HPC type)
#VIEW( MAP(sphere1)(domain(100)) ) 

# point function
def disk2D(p): 
	u,v = p
	return [v*COS(u), v*SIN(u)] # coordinate functions

# point function
def disk3D(p): 
	u,v,h = p
	return [v*COS(u), v*SIN(u), h] # coordinate functions

# 2D domain decompos	
domain2D = PROD([INTERVALS(2*PI)(100), INTERVALS(1)(3)]) 
#VIEW( MAP(disk2D)(domain2D) ) 
# 3D domain 



def cilindro(n):
	domain3D = INSR(PROD)([INTERVALS(2*PI)(32), INTERVALS(1)(3), INTERVALS(3)(1)]) 
	cilindro =  MAP(disk3D)(domain3D)
	cilindro = S([1,2,3])([.05,.05,1])(cilindro)
	cilindro = COLOR(GRAY)(cilindro)
	return T([2])([n])(cilindro)

 

def ringhiera(n):
	my_list = list()
	for i in range(n):
		my_list.append(cilindro(i))

	top = R([2,3])(PI/2)(cilindro(0))
	top = S(2)(3)(top)
	top = T([2,3])([9,3])(top)
	my_list.append(top)
	return my_list


 
#VIEW(STRUCT( ringhiera(10) ))


 