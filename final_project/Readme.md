
<!-- saved from url=(0081)https://raw.githubusercontent.com/cvdlab-cg/438541/master/final-project/Readme.md -->
<html><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">**COMPUTATIONAL GRAPHICS - FINAL PROJECT**
=======================================

Valentina Giuliani - 439463
--------------------------

[Avvia il progetto] (https://valentinagiuliani.github.io/)
, [Piantina casa] (piantina.jpg)

**Code organization :**

* [index](index.html): pagina html di avvio in cui viene inizializzata la scena.
* [makeHouse](script/makeHouse.js):crea la casa importanto l'obj provaCasa.obj realizzato in lar.
* [makeBalcone] (script/makeBalcone.js): crea il balcone dell'appartamento.
* [makeCarpet] (script/makeCarpet.js) : realizza tutti i tappeti presenti nella casa.
* [makeWall] (script/makeWall.js) : applica le texture di tutte le pareti.
* [makeRoof] (script/makeRoof.js) : realizza il tetto.
* [makeWindows] (script/makeWindows.js) : realizza le finestre della casa.
* [makeDoor] (script/makeDoor.js) : realizza ttte le porte della casa gestendo anche le aperture e le chiusure
* [makeFloor] (script/makeFloor.js) : realizza tutti i pavimenti della casa applicando specifiche texture.
* [makeGiardino] (script/makeGiardino.js) : realizza una palma nel giardino.
* [makeBath](script/makeBath.js),[makeKitchen] (script/makeKitchen.js) ,[makePierRoom] (script/makePierRoom), [makeValeRoom] (script/makeValeRoom), [makeRoomM] (script/makeRoomM), [makeSala] (script/makeSala) : realizzano rispettivamente il bagno,la cucina, la camera di Pierpaolo, camera di valentina, camera matrimoniale e il salotto

=======

**Graphic techniques :**

* STATIC TEXTURES: per pareti,pavimenti e oggetti vari.
* VIDEO TEXTURE: per la tv
* AUDIO: per lo stereo, teiera, aspirapolvere, citofono.
* SKYBOX: per lo switch tra giorno/notte
* AUDIO FADING: per il video
* SPOTLIGH: presenti in ogni stanza e all'esterno della casa
* GUI CONTROLS
* OBJ + MTL IMPORT for room detailing
* **AUTOMATIZED ROOM LIGHTS** 
* **MIRROR EFFECT** 
* **POINTER LOCK CAMERA**  con possibilità di switch tra una visuale e l'altra
* **PARTICLE ENGINE**: per il fuoco nel camino e per il fuoco sui fornelli
* **OBJECT PICKING**: si possono aprire porte e finestre e interagire con gli oggetti in casa
* **TWEEN: utilizzato per animazioni**

</pre></body></html>