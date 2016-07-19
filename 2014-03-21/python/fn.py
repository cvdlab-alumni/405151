
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
