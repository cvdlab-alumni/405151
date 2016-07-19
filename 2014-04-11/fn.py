
from pyplasm import *

# point function
def cerchio(r):
	def cerchio1(p): 
		return [r*COS(p[0]), r*SIN(p[0])]
	return cerchio1

# generator of domain decomp
def domain(n): 
		return INTERVALS(2*PI)(n)

def disco(p):
	u,v = p
	return [v*COS(u), v*SIN(u)]

	# point function
def ruota(p): 
	alfa = p
	def punti(pt):
		u,v=pt
		x = u*COS(alfa)-v*SIN(alfa)
		y = u*SIN(alfa)+v*COS(alfa)
		return [x,y] # coordinate functions
	return punti


def ROTN (args):
	alpha , n = args
	n = UNITVECT(n)
	qx = UNITVECT((VECTPROD([[0,0,1], n])))
	qz = UNITVECT(n)
	qy = VECTPROD([qz,qx])
	Q = MATHOM([qx, qy, qz])
	if n[0]==0 and n[1]==0:
		return R([1, 2])(alpha)
	else:
		return COMP([MAT(TRANS(Q)),R([1,2])(alpha),MAT(Q)])

		