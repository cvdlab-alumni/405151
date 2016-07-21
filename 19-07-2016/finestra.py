from larlib import *

def VIEWNumbers(numberSize):
	def VIEWNumbers0(V,EV,FV=[],CV=[]):
		submodel = STRUCT(MKPOLS((V,EV)))
		VV = AA(LIST)(range(len(V)))
		VIEW(larModelNumbering(1,1,1)(V,[VV,[],FV,CV],submodel,numberSize))
	return VIEWNumbers0


from pyplasm import *

def finestra():
	faccia = CUBOID([1,.03,1]) 
	faccia = MATERIAL([1,0,0,1,  0,1,0,1,  0,0,1,0, 0,0,0,1, 100])(faccia)
	finestra = CUBOID([0.3,.03,0.6])
	finestra = T([1,3])([.1,.3])(finestra)
	finestra = COLOR(BLUE)(finestra)
	finestra = STRUCT([faccia,finestra])
	return finestra


 