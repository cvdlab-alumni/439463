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

def DRAW(lar) :
    VIEW(SKEL_1(STRUCT(MKPOLS(lar))))

#appartamento giuliani
master = assemblyDiagramInit([7,9,3])([[.3,3,.3,2,.3,4,.3],[.3,3,.3,2,.3,1,.3,3,.3],[0.2,2,0.2]])
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)
V,CV = master
toRemove = [88]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

toremove =[93]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toremove)]
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

''' Aggiungo una porta nella prima stanza '''
toMerge = 58
door = assemblyDiagramInit([1,3,2])([[.3],[2,1,2],[1.8,.5]])
master = diagram2cell(door,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

''' rimuovo la cella contenente la porta'''
toRemove = [188]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

toMerge = 63
door = assemblyDiagramInit([1,3,2])([[.3],[1,1,1],[1.8,.5]])
master = diagram2cell(door,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

toRemove = [192]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

'''rimuovo un muro che avevo dimenticato di togliere'''
toRemove = [46]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

'''terza porta'''
toMerge = 67
door = assemblyDiagramInit([1,3,2])([[.3],[0.4,0.8,0.4],[1.8,.5]])
master = diagram2cell(door,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,1)
#VIEW(hpc)

''' rimuovo la cella contenente la porta'''
toRemove = [195]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,1)
#VIEW(hpc)

'''terza porta'''
toMerge = 94
door = assemblyDiagramInit([3,1,2])([[0.5,0.8,0.5],[.3],[1.8,.5]])
master = diagram2cell(door,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,1)
#VIEW(hpc)

''' rimuovo la cella contenente la porta'''
toRemove = [199]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,1)
#VIEW(hpc)

'''quarta porta '''
toMerge = 117
door = assemblyDiagramInit([1,3,2])([[0.3],[0.5,0.8,0.5],[1.8,.5]])
master = diagram2cell(door,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,1)
#VIEW(hpc)

''' rimuovo la cella contenente la porta'''
toRemove = [203]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,1)
#VIEW(hpc)

'''Tolgo un muro che prima non ho tolto'''
toRemove = [134]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,1)
#VIEW(hpc)

''' Aggiungo una porta nella prima stanza '''
toMerge = 105
door = assemblyDiagramInit([1,3,2])([[.3],[2,1,2],[1.8,.5]])
master = diagram2cell(door,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,1)
#VIEW(hpc)

toRemove = [206]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,1)
#VIEW(hpc)

'''tolgo le travi sopra e un muro rimanente'''
toRemove = [84,89,133,46,145,144]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,1)
#VIEW(hpc)

'''tolgo il tetto per far visualizzare la struttura 
toRemove = [32,31,80,81,127,128,38,37,84,85,131,132,44,43,89,88,138,137,48,47,94,93,141,142]
strutturasenzatetto = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#VIEW(STRUCT(MKPOLS(strutturasenzatetto)))
hpc = cellNumbering (strutturasenzatetto,hpc)(range(len(strutturasenzatetto[1])),CYAN,1)
#VIEW(hpc)
'''

'''realizzo la prima finestra '''
toMerge = 28
finestra = assemblyDiagramInit([5,1,3])([[1.5,0.9,.2,.9,1.5],[.3],[1,1.4,.3]])
master = diagram2cell(finestra,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,1)
#VIEW(hpc)

toRemove = [206,212]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,1)
#VIEW(hpc)


'''realizzo la seconda finestra '''
toMerge = 123
finestra = assemblyDiagramInit([5,1,3])([[1.5,0.9,.2,.9,1.5],[.3],[1,1.4,.3]])
master = diagram2cell(finestra,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,1)
#VIEW(hpc)

toRemove = [218,224]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,1)
#VIEW(hpc)

'''realizzo la terza finestra '''
toMerge = 166
finestra2 = assemblyDiagramInit([1,5,3])([[.3],[1.5,0.9,.2,.9,1.5],[1,1.4,.3]])
master = diagram2cell(finestra2,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,1)
#VIEW(hpc)

toRemove = [230,236]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,1)
#VIEW(hpc)

'''realizzo la quarta finestra '''
toMerge = 95
finestra = assemblyDiagramInit([5,1,3])([[1.5,0.9,.2,.9,1.5],[.3],[1,1.4,.3]])
master = diagram2cell(finestra,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,1)
#VIEW(hpc)

toRemove = [242,248]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,1)
#VIEW(hpc)

'''realizzo la quinta finestra '''
toMerge = 22
finestra2 = assemblyDiagramInit([1,5,3])([[.3],[1.5,0.9,.2,.9,1.5],[1,1.4,.3]])
master = diagram2cell(finestra2,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,1)
#VIEW(hpc)

toRemove = [254,260]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,1)
#VIEW(hpc)

'''realizzo la sesta finestra '''
toMerge = 10
finestra2 = assemblyDiagramInit([1,5,3])([[.3],[1.5,0.9,.2,.9,1.5],[1,1.4,.3]])
master = diagram2cell(finestra2,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,1)
#VIEW(hpc)

toRemove = [266,272]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,1)
#VIEW(hpc)


'''porta principale '''
toMerge = 74
door = assemblyDiagramInit([3,1,2])([[0.5,0.8,0.5],[.3],[1.8,.5]])
master = diagram2cell(door,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,1)
#VIEW(hpc)

''' rimuovo la cella contenente la porta'''
toRemove = [276]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,1)
#VIEW(hpc)


'''tolgo il tetto per far visualizzare la struttura '''
toRemove = [28,29,77,76,121,122,35,34,81,80,126,125,41,40,84,85,131,132,135,136,90,89,44,45]
strutturasenzatetto = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
VIEW(STRUCT(MKPOLS(strutturasenzatetto)))
hpc = cellNumbering (strutturasenzatetto,hpc)(range(len(strutturasenzatetto[1])),CYAN,1)
#VIEW(hpc)


