from pyplasm import *
from scipy import *
import os,sys
""" import modules from larcc/lib """
sys.path.insert(0, 'C:/Users/Valentina/lar-cc/lib/py/')
from lar2psm import *
from simplexn import *
from larcc import *
from largrid import *
from mapper import *
from boolean import vertexSieve
from sysml import *
from architectural import *
from myfont import *
from splines import *
def DRAW(lar) :
    VIEW(SKEL_1(STRUCT(MKPOLS(lar))))
    
'''
Automatize the loop "merging-numbering-elimination" of blocks,
shown in  lar-cc/test/py/sysml/text04.py , providing a software
interface where a single 3-array of blocks is mapped at the same
time against a number of master's blocks '''

from larcc import *

master = assemblyDiagramInit([5,5,2])([[.3,3.2,.1,5,.3],[.3,4,.1,2.9,.3],[.3,2.7]])

#prende come parametri un diagramma, un master,una lista toRemove ed un elemento toMerge
def mergingNumberingElimination(diagram,master,toRemove,toMerge):
	master=diagram2cell(diagram,master,toMerge)
	master= master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
	hpc = SKEL_1(STRUCT(MKPOLS(master)))
	hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,1)
	VIEW(hpc)
	return master

'''master = assemblyDiagramInit([5,5,2])([[.3,3.2,.1,5,.3],[.3,4,.1,2.9,.3],[.3,2.7]])
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)'''
toMerge = 31
diagram= assemblyDiagramInit([3,1,2])([[0.5,0.8,0.5],[0.3],[1.8,.5]])
'''master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,1)
#VIEW(hpc)'''
toRemove = [51]
'''master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,1)
VIEW(hpc)'''

master = mergingNumberingElimination(diagram,master,toRemove,toMerge)
