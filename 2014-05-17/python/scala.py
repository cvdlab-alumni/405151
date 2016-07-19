from pyplasm import *
from scipy import *
import os,sys
sys.path.insert(0, '/Users/dodo/UNI/Grafica\ computazionale/lar-cc/lib/py/') 

from larlib import * 



def funScala(l,h,p,n):
	scalino = CUBOID([l,h,p])
	scala = scalino
	for i in range(1,n):
		scala = STRUCT([scala, T([2,3])([h*i,p*i])(scalino)])
	return scala

piano = T([2,3])([1,1])(CUBOID([1,1,.2]))
a = funScala(1,.2,.2,2)
a = R([1,2])(-PI/2)(a)
a = T([1,2,3])([1,2,1.2])(a)
piano2 = T([1,3])([1.4,.6])(piano)
b = funScala(1,.2,.2,5)
b = R([1,2])(PI)(b)
b = T([1,2,3])([2.4,1,1.8])(b)
c = funScala(1,.2,.2,5)

scala = STRUCT([c,piano,a,piano2,b])

# def objExporter((V,FV), filePath):
#     out_file = open(filePath,"w")
#     out_file.write("# List of Vertices:\n")
#     for v in V:
#         out_file.write("v")
#         for c in v:
#             out_file.write(" " + str(c))
#         out_file.write("\n")
#     out_file.write("# Face Definitions:\n")
#     for f in FV:
#         out_file.write("f")
#         for v in f:
#             out_file.write(" " + str(v+1))
#         out_file.write("\n")
#     out_file.close()






