from pyplasm import *
from scipy import *

grigio_granito = [0.803,0.752,0.690];

#definisco una colonna
def circR2(p): 
	return [2*COS(p[0]),0]

def circR1(p): 
	return [COS(p[0]),0]
def domaincirc(n): 
	return INTERVALS(2*PI)(n)

circBase=MAP(circR2)(domaincirc(25))
circBase=JOIN([circBase])
circBase=T([1,2,3])([12,12,6])(circBase)

circSopra=MAP(circR1)(domaincirc(25))
circSopra=JOIN([circSopra])
circSopra=T([1,2,3])([12,12,20])(circSopra)
colonna=JOIN([circBase,circSopra])

colonna=COLOR(grigio_granito)(STRUCT([colonna]))
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

#seconda fila di colonne
def circ(p): 
	return [0.5*COS(p[0]),0]

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

#colonne nella stanza piu piccola
circBasedentro2=MAP(circR1)(domaincirc(25))
circBasedentro2=JOIN([circBasedentro2])
circBasedentro2=T([1,2,3])([12,12,6])(circBasedentro2)
circSopradentro2=MAP(circ)(domaincirc(25))
circSopradentro2=JOIN([circSopradentro2])
circSopradentro2=T([1,2,3])([12,12,20])(circSopradentro2)
colonnadentro2=JOIN([circBasedentro2,circSopradentro2])
colonnastanza1=COLOR(grigio_granito)(T([1,2,3])([12,25])(colonnadentro2))
colonnastanza1_2=COLOR(grigio_granito)(T([1,2,3])([22,25])(colonnadentro2))
colonnastanza1_3=COLOR(grigio_granito)(T([1,2,3])([12,30])(colonnadentro2))
colonnastanza1_4=COLOR(grigio_granito)(T([1,2,3])([22,30])(colonnadentro2))
colonnatostanza1=STRUCT([colonnastanza1,colonnastanza1_2,colonnastanza1_3,colonnastanza1_4])

#colonne nella stanza piu grande, le colonne sono piu piccole
def circpicc(p): 
	return [0.25*COS(p[0]),0]
circsoprastanza2=MAP(circpicc)(domaincirc(25)) #raggio 0.25
circsoprastanza2=JOIN([circsoprastanza2])
circsoprastanza2=T([1,2,3])([20,53,20])(circsoprastanza2)
circbasestanza2=MAP(circ)(domaincirc(25)) #raggio 0.5
circbasestanza2=JOIN([circbasestanza2])
circbasestanza2=T([1,2,3])([20,53,9])(circbasestanza2)
colonnastanza2=JOIN([circbasestanza2,circsoprastanza2])

xmov=[T([1,2])([0,3]),colonnastanza2]
colonnatostanza2=COLOR(grigio_granito)(STRUCT(NN(10)(xmov)))

xmov2=[T([1,2])([3,0]),colonnastanza2]
colonnatostanza2_2=COLOR(grigio_granito)(STRUCT(NN(5)(xmov2)))

xmov3=[T([1,2])([0,3]),T(1)(18)(colonnastanza2)]
colonnatostanza2_3=COLOR(grigio_granito)(STRUCT(NN(10)(xmov3)))

colonnatistanza2=STRUCT([colonnatostanza2,colonnatostanza2_2,colonnatostanza2_3])


r=STRUCT([colonnatostanza1,colonnatistanza2])
VIEW(r)
