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

'''appartamento giuliani'''
'''aggiungiamo 10 a tutto ,ad altezza aggiugno 5'''
master_block = assemblyDiagramInit([9,9,3])([[.3,30,.3,26,.3,28,.3,24,.3],[.3,30,.3,30,.3,22,.3,26,.3],[0.2,10,10]])
hpc = SKEL_1(STRUCT(MKPOLS(master_block)))
hpc = cellNumbering (master_block,hpc)(range(len(master_block[1])),CYAN,2)
#VIEW(hpc)

'''aggiungo tutte le porte'''
door = assemblyDiagramInit([3,1,2])([[1,2,1],[.3],[1.8,.3]])
door2 = assemblyDiagramInit([3,1,2])([[1,2,1],[.3],[0.2,0.3]])

doorx = assemblyDiagramInit([3,1,2])([[3,2,3],[.3],[1.8,.3]])
door2x = assemblyDiagramInit([3,1,2])([[3,2,3],[.3],[0.2,0.3]])

doora = assemblyDiagramInit([1,3,2])([[.3],[2,1.5,2],[1.8,.3]])
doora2 = assemblyDiagramInit([1,3,2])([[.3],[2,1.5,2],[0.2,0.3]])

doorb = assemblyDiagramInit([1,3,2])([[.3],[1,2,1],[1.8,.3]])
doorb2 = assemblyDiagramInit([1,3,2])([[.3],[1,2,1],[0.2,0.3]])

doorc = assemblyDiagramInit([1,3,2])([[.3],[0.5,2,0.5],[1.8,.3]])
doorc2 = assemblyDiagramInit([1,3,2])([[.3],[0.5,2,0.5],[0.2,0.3]])

master_block = diagram2cell(door,master_block,82)
master_block = diagram2cell(door2,master_block,82)
master_block = diagram2cell(doorx,master_block,98)
master_block = diagram2cell(door2x,master_block,98)
hpc = SKEL_1(STRUCT(MKPOLS(master_block)))
hpc = cellNumbering (master_block,hpc)(range(len(master_block[1])),CYAN,4)
VIEW(hpc)
master_block = diagram2cell(doora,master_block,58)
master_block = diagram2cell(doora2,master_block,58)
master_block = diagram2cell(doora,master_block,62)
master_block = diagram2cell(doora2,master_block,62)
master_block = diagram2cell(doora,master_block,104)
master_block = diagram2cell(doora2,master_block,104)
master_block = diagram2cell(doora,master_block,66)
master_block = diagram2cell(doora2,master_block,66)
master_block = diagram2cell(doora,master_block,112)
master_block = diagram2cell(doora2,master_block,112)
master_block = diagram2cell(doorb,master_block,152)
master_block = diagram2cell(doorb2,master_block,152)

'''aggiungo tutte le finestre '''
finestra = assemblyDiagramInit([5,1,3])([[1.5,0.9,.2,.9,1.5],[.3],[1,1.4,.3]])
finestra2 = assemblyDiagramInit([1,5,3])([[.3],[1.5,0.9,.2,.9,1.5],[1,1.4,.3]])

master_block = diagram2cell(finestra,master_block,29)
master_block = diagram2cell(finestra,master_block,122)
master_block = diagram2cell(finestra,master_block,145)
master_block = diagram2cell(finestra,master_block,96)
master_block = diagram2cell(finestra,master_block,52)
master_block = diagram2cell(finestra2,master_block,11)

hpc = SKEL_1(STRUCT(MKPOLS(master_block)))
hpc = cellNumbering (master_block,hpc)(range(len(master_block[1])),CYAN,1)
VIEW(hpc)

emptyChain = [220,219,218,217,216,215,214,213,212,211,210,209,208,207,206,205,204,203,202,199,196,193,192,191,190,189,188,187,186,185,184,183,182,181,180,179,178,177,176,175,172,171,169,307,308,313,121,120,124,123,127,126,133,132,135,136,138,139,350,351,356,357,335,336,341,342,271,272,277,295,296,301,223,224,229,74,75,77,78,80,81,83,84,86,87,235,236,241,90,91,365,366,371,372,247,248,253,259,260,265,283,284,289,320,321,326,327,29,30,35,36,401,402,395,396,41,42,44,45,47,48,380,381,386,387]
solidCV = [cell for k,cell in enumerate(master_block[1]) if not (k in emptyChain)]
#DRAW((master_block[0],solidCV))

exteriorCV =  [cell for k,cell in enumerate(master_block[1]) if k in emptyChain]
exteriorCV += exteriorCells(master_block)
CV = solidCV + exteriorCV
V = master_block[0]
FV = [f for f in larFacets((V,CV),3,len(exteriorCV))[1] if len(f) >= 4]
#VIEW(EXPLODE(1.5,1.5,1.5)(MKPOLS((V,FV))))

BF = boundaryCells(solidCV,FV)
boundaryFaces = [FV[face] for face in BF]
B_Rep = V,boundaryFaces
#VIEW(EXPLODE(1.1,1.1,1.1)(MKPOLS(B_Rep)))
#VIEW(STRUCT(MKPOLS(B_Rep)))


verts, triangles = quads2tria(B_Rep)
B_Rep = V,boundaryFaces
#VIEW(EXPLODE(1.1,1.1,1.1)(MKPOLS((verts, triangles))))
#VIEW(STRUCT(MKPOLS((verts, triangles))))

def objExporter((V,FV), filePath):
    out_file = open(filePath,"w")
    out_file.write("# List of Vertices:\n")
    for v in V:
        out_file.write("v")
        for c in v:
            out_file.write(" " + str(c))
        out_file.write("\n")
    out_file.write("# Face Definitions:\n")
    for f in FV:
        out_file.write("f")
        for v in f:
            out_file.write(" " + str(v+1))
        out_file.write("\n")
    out_file.close()

filePath="C:/Users/Valentina/static-file-server/public/casaprova.obj"
objExporter((verts, triangles),filePath)