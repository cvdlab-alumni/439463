from pyplasm import *
from scipy import *

grigio_granito = [0.803,0.752,0.690];

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
r=STRUCT([g,muri,colonnatostanza1,colonnatistanza2,f1,f2,l])
VIEW(r)
