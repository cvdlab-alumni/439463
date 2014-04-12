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

#Muro interno
xmuro=QUOTE([1])
ymuro=QUOTE([69])
muro=COLOR(grigio_granito)(T([1,2,3])([15.5,19,6])(INSR(PROD)([xmuro,ymuro,QUOTE([14.5])])))
muro2=COLOR(grigio_granito)(T([1,2,3])([42,19,6])(INSR(PROD)([xmuro,ymuro,QUOTE([14.5])])))

#muretti
xmuretto1=QUOTE([9])
ymuretto1=QUOTE([1])
muretto1=COLOR(grigio_granito)(T([1,2,3])([16.5,25,6])(INSR(PROD)([xmuretto1,ymuretto1,QUOTE([14.5])])))
muretto2=COLOR(grigio_granito)(T([1,2,3])([33,25,6])(INSR(PROD)([xmuretto1,ymuretto1,QUOTE([14.5])])))
xmuretto3=QUOTE([26.8])
ymuretto3=QUOTE([1])
muretto3=COLOR(grigio_granito)(T([1,2,3])([16.2,48,6])(INSR(PROD)([xmuretto3,ymuretto3,QUOTE([14.5])])))
xmuretto4=QUOTE([9])
ymuretto4=QUOTE([1])
muretto4=COLOR(grigio_granito)(T([1,2,3])([16.5,85,6])(INSR(PROD)([xmuretto4,ymuretto4,QUOTE([14.5])])))
muretto5=COLOR(grigio_granito)(T([1,2,3])([33,85,6])(INSR(PROD)([xmuretto4,ymuretto4,QUOTE([14.5])])))
muri=STRUCT([muro,muro2,muretto1,muretto2,muretto3,muretto4,muretto5])
#frontone
xf1=QUOTE([39])
yf1=QUOTE([82])
f1=T([1,2,3])([10,11,20.5])(INSR(PROD)([xf1,yf1,QUOTE([1])]))

xf2=QUOTE([39])
yf2=QUOTE([82])
f2=T([1,2,3])([10,11,21.5])(INSR(PROD)([xf1,yf1,QUOTE([1])]))

#definisco il tetto
xseg=QUOTE([1])
yseg=QUOTE([82])
seg=T([1,2,3])([29,10,31.5])(PROD([xseg,yseg]))
A=JOIN([f2,seg])

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

struttura = STRUCT([muri,scalinata,l,f1])
VIEW(struttura)