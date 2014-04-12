from pyplasm import *
from scipy import *
import sys
sys.path.insert(0, 'C:/Users/Valentina/lar-cc/lib/py/')
from simplexn import *
from larcc import *
from lar2psm import *
from largrid import *
from morph import *
from mapper import *
from boolean import *


grigio_granito = [0.803,0.752,0.690]
grigio_cestino = [0.184,0.184,0.184]
marronepanchina = [0.588,0.294,0]
marrone = [0.5,0.4,0.3]
marronealbero = [0.325,0.105,0]
verdeprato = [0.4,1,0]
#definisco gli scalini
xfloor0=QUOTE([60])
yfloor0=QUOTE([103])
floor0=INSR(PROD)([xfloor0,yfloor0,QUOTE([3])])
xfloor1=QUOTE([50])
yfloor1=QUOTE([93])
floor1=T([1,2,3])([5,5,3])(INSR(PROD)([xfloor1,yfloor1,QUOTE([3])]))
xfloor2=QUOTE([39])
yfloor2=QUOTE([83])
floor2=T([1,2,3])([10,10,6])(INSR(PROD)([xfloor2,yfloor2,QUOTE([3])]))
scalinata=COLOR(grigio_granito)(STRUCT([floor0,floor1,floor2]))
#VIEW(scalinata)

#definisco una colonna
def circR2(p): 
	return [2*COS(p[0]),2*SIN(p[0])]

def circR1(p): 
	return [COS(p[0]),SIN(p[0])]
def domaincirc(n): 
	return INTERVALS(2*PI)(n)

circBase=MAP(circR2)(domaincirc(25))
circBase=JOIN([circBase])
circBase=T([1,2,3])([12,12,6])(circBase)

circSopra=MAP(circR1)(domaincirc(25))
circSopra=JOIN([circSopra])
circSopra=T([1,2,3])([12,12,20])(circSopra)
colonna=JOIN([circBase,circSopra])

xcapitello=QUOTE([2.2])
ycapitello=QUOTE([2.5])
capitello=COLOR(grigio_granito)(T([1,2,3])([11,11,20])(INSR(PROD)([xcapitello,ycapitello,QUOTE([0.5])])))
grigio_granito = [0.803,0.752,0.690];

colonna=COLOR(grigio_granito)(STRUCT([colonna,capitello]))
#VIEW(STRUCT([colonna,scalinata]))

#replico le colonne e creo i colonnati
xmov=[T(1)(5),colonna]
ymov=[T([1,2])([0,4.64]),colonna]
colonnato1=STRUCT(NN(7)(xmov))
colonnato2=STRUCT(NN(17)(ymov))
x2mov=[T([1,2])([0,4.64]),T([1,2])([35,0])(colonna)]
colonnato3=STRUCT(NN(17)(x2mov))
y2mov=[T([1])([5]),T([1,2])([0,79])(colonna)]
colonnato4=STRUCT(NN(7)(y2mov))
colonnati=STRUCT([colonna,colonnato1,colonnato2,colonnato3,colonnato4])

#definisco il frontone
xf1=QUOTE([39])
yf1=QUOTE([82])
f1=T([1,2,3])([10,11,20.5])(INSR(PROD)([xf1,yf1,QUOTE([1])]))

xf2=QUOTE([39])
yf2=QUOTE([82])
f2=T([1,2,3])([10,11,21.5])(INSR(PROD)([xf1,yf1,QUOTE([1])]))
#VIEW(STRUCT([f1,f2,scalinata,colonnati]))

#definisco il tetto
xseg=QUOTE([1])
yseg=QUOTE([82])
seg=T([1,2,3])([29,10,31.5])(PROD([xseg,yseg]))
A=JOIN([f2,seg])


#seconda fila di colonne
def circ(p): 
	return [0.5*COS(p[0]),0.5*SIN(p[0])]

circBasedentro=MAP(circR1)(domaincirc(25))
circBasedentro=JOIN([circBasedentro])
circBasedentro=T([1,2,3])([12,12,6])(circBasedentro)

circSopradentro=MAP(circ)(domaincirc(25))
circSopradentro=JOIN([circSopradentro])
circSopradentro=T([1,2,3])([12,12,20])(circSopradentro)

colonnadentro=COLOR(grigio_granito)(T([1,2,3])([5,5])(JOIN([circBasedentro,circSopradentro])))

xcapitello=QUOTE([2.2])
ycapitello=QUOTE([2.5])
capitello=COLOR(grigio_granito)(T([1,2,3])([15.9,15.3,20.2])(INSR(PROD)([xcapitello,ycapitello,QUOTE([0.5])])))

colonnadentro=STRUCT([colonnadentro,capitello])
movint=[T(1)(5),colonnadentro]
colonnatointerno=COLOR(grigio_granito)(STRUCT(NN(5)(movint)))
colonnanike=colonnadentro

#Muro interno
xmuro=QUOTE([1])
ymuro=QUOTE([69])
muro=COLOR(grigio_granito)(T([1,2,3])([15.5,19,6])(INSR(PROD)([xmuro,ymuro,QUOTE([14.5])])))
muro2=COLOR(grigio_granito)(T([1,2,3])([42,19,6])(INSR(PROD)([xmuro,ymuro,QUOTE([14.5])])))
#VIEW(STRUCT([muro,muro2,colonnadentro,scalinata,colonnati,colonnatointerno]))

#muretti
xmuretto1=QUOTE([9])
ymuretto1=QUOTE([1])
muretto1=COLOR(grigio_granito)(T([1,2,3])([16.5,25,6])(INSR(PROD)([xmuretto1,ymuretto1,QUOTE([14.5])])))
g=STRUCT([muro,muro2,colonnadentro,scalinata,colonnati,colonnatointerno])
muretto2=COLOR(grigio_granito)(T([1,2,3])([33,25,6])(INSR(PROD)([xmuretto1,ymuretto1,QUOTE([14.5])])))
xmuretto3=QUOTE([26.8])
ymuretto3=QUOTE([1])
muretto3=COLOR(grigio_granito)(T([1,2,3])([16.5,48,6])(INSR(PROD)([xmuretto3,ymuretto3,QUOTE([14.5])])))
xmuretto4=QUOTE([9])
ymuretto4=QUOTE([1])
muretto4=COLOR(grigio_granito)(T([1,2,3])([16.5,85,6])(INSR(PROD)([xmuretto4,ymuretto4,QUOTE([14.5])])))
muretto5=COLOR(grigio_granito)(T([1,2,3])([33,85,6])(INSR(PROD)([xmuretto4,ymuretto4,QUOTE([14.5])])))
muri=STRUCT([muretto1,muretto2,muretto3,muretto4,muretto5])

#colonne nella stanza piu piccola
circBasedentro2=MAP(circR1)(domaincirc(25))
circBasedentro2=JOIN([circBasedentro2])
circBasedentro2=T([1,2,3])([12,12,6])(circBasedentro2)
circSopradentro2=MAP(circ)(domaincirc(25))
circSopradentro2=JOIN([circSopradentro2])
circSopradentro2=T([1,2,3])([12,12,20])(circSopradentro2)
colonnadentro2=JOIN([circBasedentro2,circSopradentro2])
xcapitellopicc=QUOTE([2])
ycapitellopicc=QUOTE([2])
capitellopicc=T([1,2,3])([11,11,20])(INSR(PROD)([xcapitellopicc,ycapitellopicc,QUOTE([0.5])]))
colonnadentro2=STRUCT([colonnadentro2,capitellopicc])
colonnastanza1=COLOR(grigio_granito)(T([1,2,3])([12,25])(colonnadentro2))
colonnastanza1_2=COLOR(grigio_granito)(T([1,2,3])([22,25])(colonnadentro2))
colonnastanza1_3=COLOR(grigio_granito)(T([1,2,3])([12,30])(colonnadentro2))
colonnastanza1_4=COLOR(grigio_granito)(T([1,2,3])([22,30])(colonnadentro2))
colonnatostanza1=STRUCT([colonnastanza1,colonnastanza1_2,colonnastanza1_3,colonnastanza1_4])

#colonne nella stanza piu grande, le colonne sono piu piccole
def circpicc(p): 
	return [0.25*COS(p[0]),0.25*SIN(p[0])]
circsoprastanza2=MAP(circpicc)(domaincirc(25)) #raggio 0.25
circsoprastanza2=JOIN([circsoprastanza2])
circsoprastanza2=T([1,2,3])([20,53,20])(circsoprastanza2)
circbasestanza2=MAP(circ)(domaincirc(25)) #raggio 0.5
circbasestanza2=JOIN([circbasestanza2])
circbasestanza2=T([1,2,3])([20,53,9])(circbasestanza2)
colonnastanza2=JOIN([circbasestanza2,circsoprastanza2])
xcapitellopicc2=QUOTE([1.5])
ycapitellopicc2=QUOTE([1.5])
capitellopicc2=T([1,2,3])([19.3,52.1,20])(INSR(PROD)([xcapitellopicc2,ycapitellopicc2,QUOTE([0.2])]))
colonnastanza2=STRUCT([colonnastanza2,capitellopicc2])

xmov=[T([1,2])([0,3]),colonnastanza2]
colonnatostanza2=COLOR(grigio_granito)(STRUCT(NN(10)(xmov)))

xmov2=[T([1,2])([3,0]),colonnastanza2]
colonnatostanza2_2=COLOR(grigio_granito)(STRUCT(NN(5)(xmov2)))

xmov3=[T([1,2])([0,3]),T(1)(18)(colonnastanza2)]
colonnatostanza2_3=COLOR(grigio_granito)(STRUCT(NN(10)(xmov3)))

colonnatistanza2=STRUCT([colonnatostanza2,colonnatostanza2_2,colonnatostanza2_3])

#decorazione frontone
xbase=QUOTE([39])
ybase=QUOTE([2])
base=T([1,2,3])([10,11,21.5])(PROD([xbase,ybase]))
xpunta=QUOTE([0.1])
ypunta=QUOTE([2])
punta=T([1,2,3])([29,9,30])(PROD([xpunta,ypunta]))
incavo=COLOR(RED)(JOIN([base,punta]))
o=DIFF([A,incavo])

xbase2=QUOTE([39])
ybase2=QUOTE([2])
base2=T([1,2,3])([10,91.5,21.5])(PROD([xbase2,ybase2]))
xpunta2=QUOTE([0.1])
ypunta2=QUOTE([2])
punta2=T([1,2,3])([29,91.5,30])(PROD([xpunta2,ypunta2]))
incavo2=COLOR(RED)(JOIN([base2,punta2]))
l=DIFF([o,incavo2])
tempio=COLOR(grigio_granito)(STRUCT([g,muri,colonnatostanza1,colonnatistanza2,f1,f2,l]))

p1=MK([0,0,0])
p2=MK([140,0,0])
p3=MK([140,140,0])
p4=MK([0,140,0])
p5=MK([5,135,30])
p6=MK([5,5,30])
p7=MK([135,5,30])
p8=MK([135,135,30])
trapezio=COLOR(marrone)(JOIN([p1,p2,p3,p4,p5,p6,p7,p8]))
prato=COLOR(verdeprato)(T([1,2])([-80,-200])(CUBOID([285,400,0])))

p9=MK([140,4,0])
p10=MK([140,40,0])
p11=MK([138,4,0])
p12=MK([138,40,0])
p13=MK([135,5,30])
p14=MK([135,35,30])
spicchio1=JOIN([p9,p10,p11,p12,p13,p14])
base=COLOR(marrone)(DIFF([trapezio,spicchio1]))

p15=MK([130,140,0])
p16=MK([50,140,0])
p17=MK([130,138,0])
p18=MK([50,138,0])
p19=MK([130,135,30])
p20=MK([50,135,30])
spicchio2=JOIN([p15,p16,p17,p18,p19,p20])
base=COLOR(marrone)(DIFF([base,spicchio2]))

p21=MK([0,6,0])
p22=MK([0,60,0])
p23=MK([2,6,0])
p24=MK([2,60,0])
p25=MK([5,20,30])
p26=MK([5,50,30])
spicchio3=JOIN([p21,p22,p23,p24,p25,p26])
base=COLOR(marrone)(DIFF([base,spicchio3]))


p27=MK([7,0,0])
p28=MK([70,0,0])
p29=MK([7,2,0])
p30=MK([70,2,0])
p31=MK([15,5,30])
p32=MK([60,5,30])
spicchio4=JOIN([p27,p28,p29,p30,p31,p32])
base=COLOR(marrone)(DIFF([base,spicchio4]))

#VIEW(STRUCT([base,T([1,2,3])([73,30,30])(tempio),prato]))

#Tempio di Atena Nike
#definisco gli scalini
xfloor0nike=QUOTE([30])
yfloor0nike=QUOTE([50])
floor0nike=INSR(PROD)([xfloor0nike,yfloor0nike,QUOTE([2])])
xfloor1nike=QUOTE([25])
yfloor1nike=QUOTE([45])
floor1nike=T([1,2,3])([2.5,2.5,2])(INSR(PROD)([xfloor1nike,yfloor1nike,QUOTE([2])]))
xfloor2nike=QUOTE([20])
yfloor2nike=QUOTE([40])
floor2nike=T([1,2,3])([5,5,4])(INSR(PROD)([xfloor2nike,yfloor2nike,QUOTE([2])]))
scalinatanike=T([1,2,3])([15,30,30])(COLOR(grigio_granito)(STRUCT([floor0nike,floor1nike,floor2nike])))

colonnanike=T([1,2,3])([7,21,30])(colonnanike)
colonnenike=STRUCT(NN(3)([T([1])([4]),colonnanike]))

xmuronike=QUOTE([1])
ymuronike=QUOTE([28])
muronike=COLOR(grigio_granito)(T([1,2,3])([23.5,40,36])(INSR(PROD)([xmuronike,ymuronike,QUOTE([14.6])])))
muro2nike=COLOR(grigio_granito)(T([1,2,3])([36,40,36])(INSR(PROD)([xmuronike,ymuronike,QUOTE([14.6])])))
xmuronike2=QUOTE([13.5])
ymuronike2=QUOTE([1])
muro3nike=COLOR(grigio_granito)(T([1,2,3])([23.5,68,36])(INSR(PROD)([xmuronike2,ymuronike2,QUOTE([14.6])])))
murinike=STRUCT([muronike,muro2nike,muro3nike])
colonnanike2_a=T([1,2])([0,35])(colonnanike)
colonnenike2=T([1,2])([0,35])(colonnenike)
colonnenike2=STRUCT([colonnanike2_a,colonnenike2])
colonnenike3=STRUCT(NN(2)([T([1,2])([3.5,0]),T([1,2])([1,5])(colonnanike)]))
colonnenike=STRUCT([colonnanike,colonnenike,murinike,colonnenike2,colonnenike3])

front1=COLOR(grigio_granito)(T([1,2,3])([20,35,50.5])(CUBOID([21,40,1])))
atenaNike=T([1,2])([33,10])(R([1,2])(PI/6)(STRUCT([scalinatanike,colonnenike,front1])))
#VIEW(STRUCT([base,T([1,2,3])([73,30,30])(tempio),prato,atenaNike]))


def circROTTA(p): 
	return [1.5*COS(p[0]),1.5*SIN(p[0])]

circBase=MAP(circR2)(domaincirc(16))
circBase=JOIN([circBase])
circBase=T([1,2,3])([12,12,6])(circBase)

circSopra=MAP(circROTTA)(domaincirc(16))
circSopra=JOIN([circSopra])
circSopra=T([1,2,3])([12,12,12])(circSopra)
pezzocolonna=COLOR(grigio_granito)(T([1,2,3])([30,15,23])(JOIN([circBase,circSopra])))
pezzocolonna2=T([1,2])([4,1])(pezzocolonna)
pezzocolonna3=T([1,2])([-35,105])(pezzocolonna)
pezzocolonna5=T([1,2])([50,-10])(pezzocolonna3)
colonnerotte=STRUCT(NN(5)([T(1)(5),pezzocolonna3]))
colonnerotte2=STRUCT(NN(4)([T([1,2])([0,-5]),pezzocolonna3]))
cubo=COLOR(grigio_granito)(T([1,2,3])([38,28,30])(CUBOID([2,2,2])))
cubo2=COLOR(grigio_granito)(T([1,2,3])([44,29,30])(R([1,2])(PI/4)(CUBOID([2,4,4]))))
cubo3 = COLOR(grigio_granito)(T([1,2,3])([44,21,30])(R([1,2])(PI/4)(CUBOID([4,4,2]))))
cubo4 = STRUCT(NN(3)([T([1,2])([2,2]),T([1,2])([10,100])(cubo3)]))
cubo5 = STRUCT([T([1,2])([70,-10])(cubo3),T([1,2])([70,-15])(cubo2)])
cubo6 = STRUCT([T([1,2])([-30,-10])(cubo3),T([1,2])([-30,-15])(cubo2)])
rovine=STRUCT([pezzocolonna,pezzocolonna2,cubo,cubo2,cubo3])
rovine2=T([1,2])([0,70])(rovine)
rovine3=T([1,2])([50,-10])(rovine)
pezzocolonna4=T([1,2])([-35,0])(pezzocolonna)
pezzocolonna4=STRUCT(NN(5)([T([1,2])([0,5]),pezzocolonna4]))
pezzocolonna6=T([1,2])([125,-20])(pezzocolonna4)

struttura=STRUCT([base,T([1,2,3])([69,29,30])(tempio),pezzocolonna6,pezzocolonna5,cubo6,cubo5,cubo4,pezzocolonna4,prato,atenaNike,rovine,rovine2,rovine3,pezzocolonna3,colonnerotte,colonnerotte2])

def F_scala(altezza,larghezza,alzata,profondita):
	gradini = int(altezza/alzata)
	s = CUBE(0)
	for i in range(1,gradini+1):
		gradino = CUBOID([larghezza,profondita,i*alzata])
		s = STRUCT([s,T(2)(profondita*i)(gradino)])
	return s

scala=COLOR(marrone)(T([1,2])([70,-25])(F_scala(30,50,2,2)))
strada=COLOR(grigio_granito)(T([1,2])([70,-200,0.2])(CUBOID([50,200,1])))
#VIEW(STRUCT([struttura,scala,strada]))

#definizione alberi
def circAlbero(p): 
	return [5*COS(p[0]),5*SIN(p[0])]

al=CYLINDER([1,8])(32)
base=T(3)(8)(MAP(circAlbero)(domaincirc(32)))
punto=MK([0,0,15])
al=STRUCT([COLOR(marronealbero)(al),COLOR(GREEN)(JOIN([base,punto]))])
albero1=al
al=STRUCT(NN(30)([T([1,2])([0,6]),T([1,2,3])([68,-205,0.2])(al)]))
al2=T([1])([53.5])(al)

def larSphere2(radius=1):
	def larSphere0(shape=[18,36]):
		V,CV = larIntervals(shape)([PI,PI])
		V = translatePoints(V,[-PI/2,-PI])
		domain = V,CV
		x = lambda V : [radius*COS(p[0])*SIN(p[1]) for p in V]
		y = lambda V : [radius*COS(p[0])*COS(p[1]) for p in V]
		z = lambda V : [radius*SIN(p[0]) for p in V]
		return larMap([x,y,z])(domain)
	return larSphere0

siepe = T([1,2,3])([70,-4,0.1])(R([1,3])(-PI/2)(STRUCT(MKPOLS(larSphere2(3)()))))
siepe2 = T([1,2,3])([143,-4,0.1])(R([1,3])(-PI/2)(STRUCT(MKPOLS(larSphere2(3)()))))
siepe = STRUCT(NN(13)([T(1)(-5),COLOR(GREEN)(siepe)]))
siepe2=STRUCT(NN(4)([T(1)(-5),COLOR(GREEN)(siepe2)]))

albero=STRUCT(NN(33)([T([1,2])([0,6]),T([1,2])([-8,-1])(albero1)]))
alberobis=STRUCT(NN(11)([T([1,2])([-13,0]),T([1,2])([-8,-1])(albero1)]))
albero2=STRUCT(NN(5)([T([1])(-13),STRUCT(NN(33)([T([1,2])([0,6]),T([1,2])([-7,-1.5])(albero1)]))]))
albero3=STRUCT(NN(5)([T([1,2])([0,10]),T([1,2])([155,145])(alberobis)]))
albero4=T([1])([220])(albero2)

verde= STRUCT([al,al2,siepe,siepe2,albero,albero2,albero3,albero4])


#Panchina
legno1=STRUCT(NN(3)([T(3)(3.5),T([3])([12])(CUBOID([30,2,2]))]))
legnovert=T([1,2,3])([3,0,12])(CUBOID([2,2,13]))
legnovert2=T([1,2,3])([26,0,12])(CUBOID([2,2,13]))
legnosedile=STRUCT(NN(3)([T(2)(-4),T([3])([12])(CUBOID([30,2,2]))]))
legnosedilevert=T([1,2,3])([3,-13,12])(CUBOID([2,13,2]))
legnosedilevert2=T([1,2,3])([26,-13,12])(CUBOID([2,13,2]))
gamba1=T([1,2])([3,-4])(CUBOID([2,2,12]))
gamba2=T([1,2])([3,-12])(CUBOID([2,2,12]))
gamba3=T([1,2])([26,-4])(CUBOID([2,2,12]))
gamba4=T([1,2])([26,-12])(CUBOID([2,2,12]))
panchina=STRUCT([legno1,legnovert,legnovert2,legnosedile,legnosedilevert,legnosedilevert2,gamba1,gamba2,gamba3,gamba4])

panchina1=S([1,2,3])([0.25,0.25,0.25])(panchina)
panchina1=T([1,2])([115,-50])(R([1,2])(-PI/2)(panchina1))
panchina2=T([2])([-50])(panchina1)
panchina3=T([2])([-100])(panchina1)
panchinedx=COLOR(marronepanchina)(STRUCT([panchina1,panchina2,panchina3]))
panchinesx=T([1,2])([195,-230])(R([1,2])(PI)(panchinedx))
#VIEW(STRUCT([struttura,scala,strada,verde,panchinedx,panchinesx]))

#CESTINO
def BASEcest(p): 
	return [0.75*COS(p[0]),0.75*SIN(p[0])]
def SOPRAcest(p):
	return [1*COS(p[0]),1*SIN(p[0])]

basec = MAP(BASEcest)(domaincirc(10))
soprac =T(3)(3)(MAP(SOPRAcest)(domaincirc(10)))
cestino=JOIN([basec,soprac])
cestino2=S([1,2])([0.9,0.9])(cestino)
cestino=STRUCT([JOIN([basec,T(3)(0.5)(MAP(BASEcest)(domaincirc(10)))]),DIFF([cestino,cestino2])])
#VIEW(cestino)

cestino_1=COLOR(grigio_cestino)(T([1,2])([80,-90])(cestino))
cestino_2=T([2])([-50])(cestino_1)
cestino_3=T([2])([-100])(cestino_1)
cestinidx=STRUCT([cestino_1,cestino_2,cestino_3])
cestinisx=T([1,2])([32,10])(cestinidx)
#VIEW(STRUCT([struttura,scala,strada,verde,panchinedx,panchinesx,cestinidx,cestinisx]))

#lampione
def PALO(p): 
	return [0.75*COS(p[0]),0.75*SIN(p[0])]
bpalo=MAP(PALO)(domaincirc(32))
bpalo2=T(3)(0.75)(MAP(PALO)(domaincirc(32)))
bpalo=COLOR(BLACK)(JOIN([bpalo,bpalo2]))
palo=COLOR(BLACK)(CYLINDER([0.5,8])(32))
lamp = COLOR(YELLOW)(T([3])([8.5])(STRUCT(MKPOLS(larSphere(1)()))))
lampione=STRUCT([lamp,palo,bpalo])

lampione1=(T([1,2])([80,-70])(lampione))
lampione2=(T([1,2])([80,-120])(lampione))
lampione3=(T([1,2])([80,-170])(lampione))
lampionidx =STRUCT([lampione1,lampione2,lampione3])
lampionisx=T([1,2])([35,25])(lampionidx)

#SECONDO MONTE
p12=MK([-100,-100,0])
p22=MK([-20,-100,0])
p32=MK([-20,-20,0])
p42=MK([-100,-20,0])
p52=MK([-90,-90,20])
p62=MK([-30,-90,20])
p72=MK([-90,-30,20])
p82=MK([-30,-30,20])
trapezio2=T([1,2])([40,-10])(COLOR(marrone)(JOIN([p12,p22,p32,p42,p52,p62,p72,p82])))
atenaNike2=T([1,2,3])([-100,-120,-9])(S([1,2])([1.2,0.8])(T([1,2])([33,10])(STRUCT([scalinatanike,colonnenike,front1]))))
scalinatanike2=COLOR(marrone)(T([1,2])([-50,-120])(F_scala(20,20,2,2)))
stradanike2=COLOR(grigio_granito)(T([1,2])([-50,-139,0.2])(CUBOID([20,20,1])))
stradanike2a=COLOR(grigio_granito)(T([1,2])([-50,-139,0.2])(CUBOID([120,20,1])))
panchinenike=T([1,2])([110,-20])(R([1,2])(-PI/2)(COLOR(marronepanchina)(STRUCT([panchina1,panchina2,panchina3]))))
lampioninike =T([1,2])([132,-55])(R([1,2])(-PI/2)(STRUCT([lampione1,lampione2,lampione3])))
nike2=STRUCT([trapezio2,atenaNike2,scalinatanike2,stradanike2,stradanike2a,panchinenike,lampioninike])

ROVINE4=COLOR(grigio_granito)(T([1,2,3])([150,-150,-30])(rovine))
ROVINE5=COLOR(grigio_granito)(T([1,2])([-10,-15])(ROVINE4))
ROVINE6=COLOR(grigio_granito)(T([1,2])([-10,15])(ROVINE4))

ROVINE7=T([1,2])([-170,-40])(STRUCT([ROVINE4,ROVINE6,ROVINE5]))
ROVINE8=T([1,2])([-20,60])(STRUCT([ROVINE4,ROVINE6,ROVINE5]))
VIEW(STRUCT([struttura,scala,strada,verde,panchinedx,panchinesx,cestinidx,cestinisx,lampionidx,lampionisx,nike2,ROVINE4,ROVINE5,ROVINE6,ROVINE7,ROVINE8]))