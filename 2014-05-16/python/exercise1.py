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

#appartamento giuliani
master = assemblyDiagramInit([9,9,4])([[.3,3,.3,2,.3,4,.3,2,.3],[.3,3,.3,2,.3,1,.3,3,.3],[0.2,1,1,0.2]])
copertura = master

'''rimuovo le celle per definire la struttura complessiva '''
toRemove = [254,255,290,291,294,295,257,258,259,294,295,262,263,264,265,298,299,262,265,266,267,268,269,270,271,272,273,274,275,276,277,278,279,280,281,282,283,284,285,286,287,
			300,301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,319,320,321,322,323]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,1)
#VIEW(hpc)

''' Aggiungo le porte '''
toMerge = 77
door = assemblyDiagramInit([1,3,2])([[.3],[2,1,2],[1.8,.3]])
door2 = assemblyDiagramInit([1,3,2])([[.3],[2,1,2],[0.2,0.3]])
master = diagram2cell(door,master,toMerge)
master = diagram2cell(door2,master,toMerge)
toMerge =83
master = diagram2cell(door,master,toMerge)
master = diagram2cell(door2,master,toMerge)
toMerge = 89
doorpic = assemblyDiagramInit([1,3,2])([[.3],[0.5,1.5,0.5],[1.8,.3]])
door2pic = assemblyDiagramInit([1,3,2])([[.3],[0.5,1.5,0.5],[0.2,0.3]])
master = diagram2cell(doorpic,master,toMerge)
master = diagram2cell(door2pic,master,toMerge)
toMerge = 159 
master = diagram2cell(doorpic,master,toMerge)
master = diagram2cell(door2pic,master,toMerge)
toMerge = 143
master = diagram2cell(door,master,toMerge)
master = diagram2cell(door2,master,toMerge)
toMerge = 211
master = diagram2cell(door,master,toMerge)
master = diagram2cell(door2,master,toMerge)
door2 = assemblyDiagramInit([3,1,2])([[0.5,0.8,0.5],[.3],[1.8,.3]])
door2a = assemblyDiagramInit([3,1,2])([[0.5,0.8,0.5],[0.3],[0.2,0.3]])
toMerge=103
master = diagram2cell(door2,master,toMerge)
master = diagram2cell(door2a,master,toMerge)
toMerge=125
master = diagram2cell(door2,master,toMerge)
master = diagram2cell(door2a,master,toMerge)

''' aggiungo le finestre '''
toMerge = 168
finestra = assemblyDiagramInit([5,1,3])([[1.5,0.9,.2,.9,1.5],[.3],[1,1.4,.3]])
master = diagram2cell(finestra,master,toMerge)

toMerge = 38
finestra = assemblyDiagramInit([5,1,3])([[1.5,0.9,.2,.9,1.5],[.3],[1,1.4,.3]])
master = diagram2cell(finestra,master,toMerge)

toMerge = 198
finestra = assemblyDiagramInit([5,1,3])([[1.5,0.9,.2,.9,1.5],[.3],[1,1.4,.3]])
master = diagram2cell(finestra,master,toMerge)

toMerge = 69
finestra = assemblyDiagramInit([5,1,3])([[1.5,0.9,.2,.9,1.5],[.3],[1,1.4,.3]])
master = diagram2cell(finestra,master,toMerge)

toMerge = 130
finestra = assemblyDiagramInit([5,1,3])([[1.5,0.9,.2,.9,1.5],[.3],[1,1.4,.3]])
master = diagram2cell(finestra,master,toMerge)

toMerge = 14
finestra = assemblyDiagramInit([1,5,3])([[.3],[1.5,0.9,.2,.9,1.5],[1,1.4,.3]])
master = diagram2cell(finestra,master,toMerge)

'''elimino muri di troppo e le celle contenenti finestre e porte,lascio il tetto '''
toRemove =[166,167,170,171,172,174,175,183,182,186,187,188,190,191,102,103,106,107,108,110,111,114,115,116,118,119,124,125,39,40,47,48,55,56,59,60,61,63,64
			,303,304,309,377,371,401,407,386,392,416,422,321,315,316,341,347,291,292,297,315,316,321,243,244,249,255,256,261,267,268,273,327,328,333,279,280,285,356,362]
appartamentocontetto = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
toRemove = [141,144,150,153,91,94,97,101,39,45,51,54,386,392]
appartamentosenzatetto = appartamentocontetto[0], [cell for k,cell in enumerate(appartamentocontetto[1]) if not (k in toRemove)]
VIEW(STRUCT(MKPOLS(appartamentosenzatetto)))
