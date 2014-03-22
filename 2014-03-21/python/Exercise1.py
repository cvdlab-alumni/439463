from pyplasm import *
grigio_granito = [0.803,0.752,0.690];
#definisco gli scalini
xfloor0=QUOTE([60])
yfloor0=QUOTE([103])
floor0=PROD([xfloor0,yfloor0])
xfloor1=QUOTE([50])
yfloor1=QUOTE([93])
floor1=COLOR(RED)(T([1,2])([5,5])(PROD([xfloor1,yfloor1])))
xfloor2=QUOTE([39])
yfloor2=QUOTE([83])
floor2=COLOR(GREEN)(T([1,2])([10,10])(PROD([xfloor2,yfloor2])))
scalinata=STRUCT([floor0,floor1,floor2])


#definisco una colonna
def circR2(p): 
	return [2*COS(p[0]),2*SIN(p[0])]
def circR1(p): 
	return [COS(p[0]),SIN(p[0])]
def domaincirc(n): 
	return INTERVALS(2*PI)(n)

#la base della colonna
circBase=MAP(circR2)(domaincirc(25))
circBase=JOIN([circBase])
circBase=COLOR(BLACK)(T([1,2])([12,12])(circBase))

#cima della colonna
circSopra=MAP(circR1)(domaincirc(25))
circSopra=JOIN([circSopra])
circSopra=COLOR(YELLOW)(T([1,2])([12,12])(circSopra))

#le colonne della facciata davanti con i capitelli
circmov=[T(1)(5),circBase]
x=STRUCT(NN(7)(circmov))
circmov2=[T(1)(5),circSopra]
y=STRUCT(NN(7)(circmov2))
xcapitello=QUOTE([2.2])
ycapitello=QUOTE([2])
capitello=COLOR(grigio_granito)(T([1,2])([11,11])(PROD([xcapitello,ycapitello])))
xmov=[T(1)(5),capitello]
colonnato1=STRUCT(NN(7)(xmov))

#facciata laterale
ymovb=[T([1,2])([0,4.64]),circBase]
colonnato2b=STRUCT(NN(17)(ymovb))
ymovs=[T([1,2])([0,4.64]),circSopra]
colonnato2s=STRUCT(NN(17)(ymovs))
movint=[T([1,2])([0,4.64]),capitello]
colonnatointerno=STRUCT(NN(17)(movint))

#facciata laterale 2

x2movb=[T([1,2])([0,4.64]),T([1,2])([35,0])(circBase)]
colonnato3b=STRUCT(NN(17)(x2movb))
x2movs=[T([1,2])([0,4.64]),T([1,2])([35,0])(circSopra)]
colonnato3s=STRUCT(NN(17)(x2movs))
y3movb=[T([1])([5]),T([1,2])([0,79])(circBase)]
colonnato4b=STRUCT(NN(7)(y3movb))
y3movs=[T([1])([5]),T([1,2])([0,79])(circSopra)]
colonnato4s=STRUCT(NN(7)(y3movs))
movint2=[T([1,2])([0,4.64]),T([1,2])([35,0])(capitello)]
movint3=[T([1])([5]),T([1,2])([0,79])(capitello)]
colonnatointerno2a=STRUCT(NN(17)(movint2))
colonnatointerno2b=STRUCT(NN(7)(movint3))

a=STRUCT([scalinata,capitello,colonnato1,x,y,circBase,circSopra,colonnato2b,colonnato2s,colonnatointerno,colonnato3b,colonnato3s,colonnato4b,colonnato4s,colonnatointerno2a,colonnatointerno2b])

#colonne interne
def circ(p): 
	return [0.5*COS(p[0]),0.5*SIN(p[0])]

circBasedentro=MAP(circR1)(domaincirc(25))
circBasedentro=JOIN([circBasedentro])
circBasedentro=COLOR(BLACK)(T([1,2])([11,17])(circBasedentro))

circSopradentro=MAP(circ)(domaincirc(25))
circSopradentro=JOIN([circSopradentro])
circSopradentro=COLOR(YELLOW)(T([1,2])([11,17])(circSopradentro))

movintb=[T(1)(6),circBasedentro]
movints=[T(1)(6),circSopradentro]
colonnatointerno3b=STRUCT(NN(5)(movintb))
colonnatointerno3s=STRUCT(NN(5)(movints))

capitelloint=T([1,2])([4,16])(PROD([xcapitello,ycapitello]))
uuu=[T(1)(6),T(1)(6)(capitelloint)]
uuy=COLOR(RED)(STRUCT(NN(5)(uuu)))
#muri
xmuro=QUOTE([1])
ymuro=QUOTE([69])
muro=COLOR(BLUE)(T([1,2])([15.5,19])(PROD([xmuro,ymuro])))
muro2=COLOR(BLACK)(T([1,2])([42,19])(PROD([xmuro,ymuro])))
xmuretto1=QUOTE([9])
ymuretto1=QUOTE([1])
muretto1=T([1,2])([16.5,25])(PROD([xmuretto1,ymuretto1]))
muretto2=T([1,2])([33,25])(PROD([xmuretto1,ymuretto1]))
xmuretto3=QUOTE([26.8])
ymuretto3=QUOTE([1])
muretto3=T([1,2])([16.5,48])(PROD([xmuretto3,ymuretto3]))
xmuretto4=QUOTE([9])
ymuretto4=QUOTE([1])
muretto4=T([1,2])([16.5,85])(PROD([xmuretto4,ymuretto4]))
muretto5=T([1,2])([33,85])(PROD([xmuretto4,ymuretto4]))
muri=STRUCT([muretto1,muretto2,muretto3,muretto4,muretto5])

#colonne stanza piccola
circBasedentro2=MAP(circR1)(domaincirc(25))
circBasedentro2=JOIN([circBasedentro2])
circBasedentro2=T([1,2])([12,12])(circBasedentro2)
circSopradentro2=MAP(circ)(domaincirc(25))
circSopradentro2=JOIN([circSopradentro2])
circSopradentro2=T([1,2])([12,12])(circSopradentro2)
xcapitellopicc=QUOTE([2])
ycapitellopicc=QUOTE([2])
capitellopicc=T([1,2])([23,36])(INSR(PROD)([xcapitellopicc,ycapitellopicc]))
capitellopicc2=T([1,2])([33,36])(INSR(PROD)([xcapitellopicc,ycapitellopicc]))
capitellopicc3=T([1,2])([33,41])(INSR(PROD)([xcapitellopicc,ycapitellopicc]))
capitellopicc4=T([1,2])([23,41])(INSR(PROD)([xcapitellopicc,ycapitellopicc]))
colonnastanza1=T([1,2])([12,25])(circBasedentro2)
colonnastanza1_2=T([1,2])([22,25])(circBasedentro2)
colonnastanza1_3=T([1,2])([12,30])(circBasedentro2)
colonnastanza1_4=T([1,2])([22,30])(circBasedentro2)
colonnastanza1s=COLOR(BLACK)(T([1,2])([12,25])(circSopradentro2))
colonnastanza1_2s=COLOR(BLACK)(T([1,2])([22,25])(circSopradentro2))
colonnastanza1_3s=COLOR(BLACK)(T([1,2])([12,30])(circSopradentro2))
colonnastanza1_4s=COLOR(BLACK)(T([1,2])([22,30])(circSopradentro2))
colonnatostanza1=STRUCT([colonnastanza1,colonnastanza1_2,colonnastanza1_3,colonnastanza1_4,colonnastanza1s,colonnastanza1_2s,colonnastanza1_3s,colonnastanza1_4s])

#COLONNE STANZA GRANDE
def circpicc(p): 
	return [0.25*COS(p[0]),0.25*SIN(p[0])]
circsoprastanza2=MAP(circpicc)(domaincirc(25)) #raggio 0.25
circsoprastanza2=JOIN([circsoprastanza2])
circsoprastanza2=T([1,2])([20,53])(circsoprastanza2)
circbasestanza2=MAP(circ)(domaincirc(25)) #raggio 0.5
circbasestanza2=JOIN([circbasestanza2])
circbasestanza2=T([1,2])([20,53])(circbasestanza2)
colonnastanza2=JOIN([circbasestanza2,circsoprastanza2])
xcapitellopicc2=QUOTE([1.5])
ycapitellopicc2=QUOTE([1.5])
capitellopicc2=T([1,2,3])([19.3,52.1])(INSR(PROD)([xcapitellopicc2,ycapitellopicc2]))
colonnastanza2=STRUCT([colonnastanza2,capitellopicc2])

xmov=[T([1,2])([0,3]),colonnastanza2]
colonnatostanza2=COLOR(grigio_granito)(STRUCT(NN(10)(xmov)))

xmov2=[T([1,2])([3.5,0]),colonnastanza2]
colonnatostanza2_2=COLOR(grigio_granito)(STRUCT(NN(5)(xmov2)))

xmov3=[T([1,2])([0,3]),T(1)(18)(colonnastanza2)]
colonnatostanza2_3=COLOR(grigio_granito)(STRUCT(NN(10)(xmov3)))

colonnatistanza2=STRUCT([colonnatostanza2,colonnatostanza2_2,colonnatostanza2_3])

#definisco il frontone
xf1=QUOTE([39])
yf1=QUOTE([82])
f1=T([1,2])([10,11])(INSR(PROD)([xf1,yf1]))

xf2=QUOTE([39])
yf2=QUOTE([82])
f2=T([1,2])([10,11])(INSR(PROD)([xf1,yf1]))

#definisco il tetto
xseg=QUOTE([1])
yseg=QUOTE([82])
seg=T([1,2])([29,10])(PROD([xseg,yseg]))

#**************************
g=STRUCT([f1,f1,seg,colonnastanza2,colonnatistanza2,a,muro,muro2,muri,colonnatointerno3b,colonnatointerno3s,uuy,colonnatostanza1,capitellopicc,capitellopicc2,capitellopicc3,capitellopicc4])
VIEW(g)
VIEW(SKELETON(1)(g))