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

    
''' ***************************ESERCIZIO 1 *************'''
#appartamento giuliani
master = assemblyDiagramInit([7,9,3])([[.3,3,.3,2,.3,4,.3],[.3,3,.3,2,.3,1,.3,3,.3],[0.2,2,0.2]])
copertura = master
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
#VIEW(STRUCT(MKPOLS(strutturasenzatetto)))
hpc = cellNumbering (strutturasenzatetto,hpc)(range(len(strutturasenzatetto[1])),CYAN,1)
#VIEW(hpc)





''' *********************** ESERCIZIO 2 ************************* '''
#DEFINIZIONE DELLE SCALE
def rampa():
	element = CUBOID([0.6,0.4,0.1])
	column = STRUCT(CAT(N(24)([element, T([2,3])([0.1,0.1])])))
	return column
#VIEW(rampa(2))
ingresso =assemblyDiagramInit([3,3,3])([[0.3,2,0.3],[0.3,4,0.3],[0.2,2,0.2]])
toRemove = [13]
ingresso = ingresso[0], [cell for k,cell in enumerate(ingresso[1]) if not (k in toRemove)]
ingressosenzaporta = ingresso
hpc = SKEL_1(STRUCT(MKPOLS(ingresso)))
hpc = cellNumbering (ingresso,hpc)(range(len(ingresso[1])),CYAN,2)
#VIEW(hpc)

'''CREO LA PORTA PER L'INGRESSO'''
toMerge = 21
door = assemblyDiagramInit([1,3,2])([[.2],[0.5,0.8,0.4],[1.8,.5]])
ingresso = diagram2cell(door,ingresso,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(ingresso)))
hpc = cellNumbering (ingresso,hpc)(range(len(ingresso[1])),CYAN,1)
#VIEW(hpc)
toRemove = [27]
ingresso = ingresso[0], [cell for k,cell in enumerate(ingresso[1]) if not (k in toRemove)]
hpc = SKEL_1(STRUCT(MKPOLS(ingressosenzaporta)))
hpc = cellNumbering (ingressosenzaporta,hpc)(range(len(ingressosenzaporta[1])),CYAN,1)
#VIEW(hpc)

'''creo la porta per l'appartamento'''
toMerge = 15
door = assemblyDiagramInit([3,1,2])([[0.5,0.8,0.5],[.3],[1.8,.5]])
ingresso = diagram2cell(door,ingresso,toMerge)
ingressosenzaporta = diagram2cell(door,ingressosenzaporta,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(ingressosenzaporta)))
hpc = cellNumbering (ingressosenzaporta,hpc)(range(len(ingressosenzaporta[1])),CYAN,1)
#VIEW(hpc)
toRemove = [31]
toRemove2 = [27] #per senza porta
ingresso = ingresso[0], [cell for k,cell in enumerate(ingresso[1]) if not (k in toRemove)]
ingressosenzaporta = ingressosenzaporta[0], [cell for k,cell in enumerate(ingressosenzaporta[1]) if not (k in toRemove2)]
hpc = SKEL_1(STRUCT(MKPOLS(ingressosenzaporta)))
hpc = cellNumbering (ingressosenzaporta,hpc)(range(len(ingressosenzaporta[1])),CYAN,1)
#VIEW(hpc)

vuoto = assemblyDiagramInit([3,3,3])([[0.1,1,0.3],[0.4,0.8,0.5],[0.2,2,0.2]])
toMerge = 13
ingresso = diagram2cell(vuoto,ingresso,toMerge)
ingressosenzaporta = diagram2cell(vuoto,ingressosenzaporta,toMerge)
toRemove = [45,46,47]
toRemove2 = [41,42,43]
ingresso = ingresso[0], [cell for k,cell in enumerate(ingresso[1]) if not (k in toRemove)]
ingressosenzaporta = ingressosenzaporta[0], [cell for k,cell in enumerate(ingressosenzaporta[1]) if not (k in toRemove2)]
hpc = SKEL_1(STRUCT(MKPOLS(ingressosenzaporta)))
#VIEW(STRUCT(MKPOLS(ingressosenzaporta)))
hpc = cellNumbering (ingressosenzaporta,hpc)(range(len(ingressosenzaporta[1])),CYAN,1)
#VIEW(hpc)

toMerge = 12
ingressosenzaporta = diagram2cell(vuoto,ingressosenzaporta,toMerge)
toRemove = [64,65,66]
ingressosenzaporta = ingressosenzaporta[0], [cell for k,cell in enumerate(ingressosenzaporta[1]) if not (k in toRemove)]
#VIEW(STRUCT(MKPOLS(ingressosenzaporta)))
hpc = SKEL_1(STRUCT(MKPOLS(ingressosenzaporta)))
hpc = cellNumbering (ingressosenzaporta,hpc)(range(len(ingressosenzaporta[1])),CYAN,1)
#VIEW(hpc)

scale = T([1,2])([0.5,0.5])(rampa())
ingresso = STRUCT(MKPOLS(ingresso))
ingresso = STRUCT([scale,ingresso])
ingressosenzaporta = STRUCT(MKPOLS(ingressosenzaporta))
ingressosenzaportasenzascale = ingressosenzaporta
ingressosenzaporta = STRUCT([scale,ingressosenzaporta])
ingressosenzaporta = STRUCT([scale,ingressosenzaporta])
ingresso = T([1,2])([3.3,-4.5])(ingresso)
ingressosenzaporta = T([1,2])([3.3,-4.5])(ingressosenzaporta)
ingressosenzaportasenzascale = T([1,2])([3.3,-4.5])(ingressosenzaportasenzascale)
#VIEW(hpc)

E=STRUCT(MKPOLS(strutturasenzatetto))
struttura = STRUCT([E,ingresso])
strutturasenzaporta = STRUCT([E,ingressosenzaporta])
strutturasenzaportasenzascale = STRUCT([E,ingressosenzaportasenzascale])
#VIEW(struttura)

appartamento = struttura
appartamento2 = T(3)(2.4)(strutturasenzaporta)
appartamento3 = T(3)(4.8)(strutturasenzaporta)
appartamento4 = T(3)(7.2)(strutturasenzaportasenzascale)
copertura = assemblyDiagramInit([1,1,1])([[10.2],[10.5],[1]])
copertura = T(3)(9.6)(STRUCT(MKPOLS(copertura)))
copertura2 = assemblyDiagramInit([1,1,1])([[2.6],[4.5],[0.2]])
copertura2 = T([1,2,3])([3.3,-4.5,9.6])(STRUCT(MKPOLS(copertura2)))
palazzo = STRUCT([appartamento,appartamento2,appartamento3,appartamento4,copertura,copertura2])
#VIEW(palazzo)

palazzo2 = T([1,2])([10,5])(palazzo)
palazzo2 = R([1,2])(-PI/6)(palazzo2)
palazzo3 = T([1,2])([10,5])(palazzo)
palazzo3 = T([1,2])([16,3])(R([1,2])(-PI/2)(palazzo3))
#VIEW(STRUCT([palazzo,palazzo2,palazzo3]))


lardom1 =larIntervals([32])([1])
dom1 = INTERVALS(1)(20)
dom2 = PROD([dom1,dom1])
a = BEZIER(S1)([[0.52, 5.96], [0.6, 8.64], [2.23, 11.53], [6.44, 11.49]])
b = BEZIER(S1)([[6.44, 11.49], [8.96, 11.43], [11.88, 8.88], [11.45, 5.48]])
c = BEZIER(S1)([[11.45, 5.48], [11.41, 3.41], [9.49, 0.43], [5.72, 0.5]])
d = BEZIER(S1)([[5.72, 0.5], [3.62, 0.51], [0.53, 2.37], [0.52, 5.96]])
obj1 = MAP(a)(dom1)
obj2 = MAP(b)(dom1)
obj3 = MAP(c)(dom1)
obj4 = MAP(d)(dom1)
prato = COLOR(GREEN)(SOLIDIFY(STRUCT([obj1,obj2,obj3,obj4])))
prato = T([1,2])([-5,-30])(S([1,2])([5,5])(prato))
#VIEW(STRUCT([palazzo,palazzo2,palazzo3,prato]))


#realizzo le macchine parcheggiate..
domain = INTERVALS(1)(30)
xy1 = BEZIER(S1)([[0.29, 0.46], [0.01, 1.44], [0.25, 1.82], [1.7, 2.1]])
xy2 = BEZIER(S1)([[1.7, 2.1], [3.51, 2.95], [3.78, 3.44], [6.87, 2.92]])
xy3 = BEZIER(S1)([[6.87, 2.92], [7.59, 2.04], [7.93, 0.87], [7.29, 0.63]])
xy4 = BEZIER(S1)([[0.29, 0.46], [1, 0.47], [1.01, 0.46], [1.01, 0.52]])
xy5 = BEZIER(S1)([[2.42, 0.52], [2.57, 1.68], [0.95, 1.84], [1, 0.52]])
xy6 = BEZIER(S1)([[2.42, 0.52], [5.66, 0.54], [2.42, 0.53], [5.69, 0.54]])
xy7 = BEZIER(S1)([[7.15, 0.68], [7.19, 1.51],[5.78, 1.96], [5.69, 0.54]])
xy8 = BEZIER(S1)([[7.15, 0.68], [7.18, 0.64], [7.29, 0.63]])

aaa = STRUCT([MAP(xy1)(domain),MAP(xy2)(domain),MAP(xy3)(domain),MAP(xy4)(domain),MAP(xy5)(domain),MAP(xy6)(domain),MAP(xy7)(domain),MAP(xy8)(domain)])
AAA = SOLIDIFY(aaa)
modello = PROD([AAA,Q(3)])
def ruota():
    cyG = CYLINDER([0.6,0.5])(100)
    cyP = CYLINDER([0.4,0.5])(100)
    r = DIFF([cyG,cyP])
    return R([1,2])(PI/4)(r)

r1 =COLOR(BLACK)(T([1,2])([1.7,0.8])(ruota()))
r2 = COLOR(BLACK)(T([1,2])([6.5,0.8])(ruota()))
r3 =COLOR(BLACK)(T([1,2,3])([1.7,0.8,2.5])(ruota()))
r4 = COLOR(BLACK)(T([1,2,3])([6.5,0.8,2.5])(ruota()))
f1= BEZIER(S1)([[2.26, 1.9], [3.05, 2.65], [3.78, 2.98], [5.01, 2.93]])
f2= BEZIER(S1)([[5.02, 2.93], [5, 2.84], [4.91, 2.07], [4.91, 2.14]])
f3= BEZIER(S1)([[4.91, 2.14], [4.43, 2.05], [3, 1.87], [2.26, 1.9]])

finestrino = STRUCT([MAP(f1)(domain),MAP(f2)(domain),MAP(f3)(domain)])
FIN = COLOR(BLUE)(SOLIDIFY(finestrino))
FIN2 = COLOR(BLUE)(T(3)(3)(FIN))
APP = COLOR(RED)(STRUCT([modello,r1,r2,r3,r4]))
APP2 =COLOR(YELLOW)(STRUCT([modello,r1,r2,r3,r4]))
car = R([2,3])(PI/2)(STRUCT([FIN,FIN2,APP]))
car2 = R([2,3])(PI/2)(STRUCT([FIN,FIN2,APP2]))
car = T([1,2,3])([10,-16,-0.25])(car)
car2 = T([1,2,3])([10,-16,-0.25])(car2)
car = S([1,2,3])([0.5,0.5,0.5])(car)
car2 = S([1,2,3])([0.5,0.5,0.5])(car2)
car2 = T([1,2])([10,-10])(car2)
#modelloFIN = COLOR(RED)(PROD([FIN,Q(0.5)]))

VIEW(STRUCT([palazzo,palazzo2,palazzo3,prato,car,car2]))
