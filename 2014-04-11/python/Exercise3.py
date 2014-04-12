from pyplasm import *
from scipy import *

grigio_granito = [0.803,0.752,0.690];
marrone = [0.5,0.4,0.3]
marronealbero = [0.8,0.4,0.3]
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
prato=COLOR(GREEN)(T([1,2])([-30,-30])(CUBOID([200,200,0])))

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

VIEW(struttura)