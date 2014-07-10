function makeWall(scene){
	//camera valentina
	//carta da parati
      var carta = createMesh(new THREE.BoxGeometry(30.35,20.1,0.2),"carta_parati_vale.jpg");
      carta.rotation.x = 0.5 * Math.PI;
      carta.position.set(15.2,60.55,10.2);
      scene.add(carta);

      var carta2 = carta.clone();
      carta2.position.set(15.2,30.7,10.2);
      scene.add(carta2);


      //shape sulla porta
      var shape = new THREE.Shape();
      shape.moveTo(0,0);
      shape.lineTo(0.303,0);
      shape.lineTo(0.303,0.202);
      shape.lineTo(0,0.202);
      shape.lineTo(0,0);

      var hole = new THREE.Path();
      hole.moveTo(0.113,0);
      hole.lineTo(0.193,0);
      hole.lineTo(0.193,0.14);
      hole.lineTo(0.113,0.14);
      hole.lineTo(0.113,0);
      shape.holes.push(hole);
      var options = {amount: 0.002,bevelThickness: 2,bevelSize: 1,bevelSegments: 3,bevelEnabled: false,curveSegments: 12,steps: 1};
      var shape2 = createMeshRep(new THREE.ExtrudeGeometry(shape,options),"carta_parati_vale.jpg");
      shape2.rotation.x = 0.5*Math.PI;
      shape2.rotation.y = 0.5*Math.PI;
      shape2.position.set(30.2,30.3,0);
      shape2.scale.set(100,100,100);
      scene.add(shape2);

      //shape sulla finestra
      var shapeFin = new THREE.Shape();
      shapeFin.moveTo(0,0);
      shapeFin.lineTo(0.303,0);
      shapeFin.lineTo(0.303,0.202);
      shapeFin.lineTo(0,0.202);
      shapeFin.lineTo(0,0);

      var hole = new THREE.Path();
      hole.moveTo(0.093,0.102);
      hole.lineTo(0.146,0.102);
      hole.lineTo(0.146,0.19);
      hole.lineTo(0.093,0.19);
      hole.lineTo(0.093,0.102);
      shapeFin.holes.push(hole);

      var hole2 = new THREE.Path();
      hole2.moveTo(0.159,0.102);
      hole2.lineTo(0.212,0.102);
      hole2.lineTo(0.212,0.19);
      hole2.lineTo(0.159,0.19);
      hole2.lineTo(0.159,0.102);
      shapeFin.holes.push(hole2);

      var shapeFin2 = createMeshRep(new THREE.ExtrudeGeometry(shapeFin,options),"carta_parati_vale.jpg");
      shapeFin2.rotation.x = 0.5*Math.PI;
      shapeFin2.rotation.y = 0.5*Math.PI;
      shapeFin2.position.set(0.35,30.3,0);
      shapeFin2.scale.set(100,100,100);
      scene.add(shapeFin2);

      //cucina
      var pav_cuc = createMeshRep2(new THREE.BoxGeometry(30.3,30.3,0.1),"piastrelle4.jpg",12);
      scene.add(pav_cuc);
      pav_cuc.position.set(15.15,15.15,0.3);

      var carta_cuc1 = createMeshRep2(new THREE.BoxGeometry(30.35,20.1,0.2),"piastrelle3.jpg",6);
      scene.add(carta_cuc1);
      carta_cuc1.rotation.x = Math.PI/2;
      carta_cuc1.position.set(15.2,30.2,10.05);

      var carta_cuc2 = createMeshRep2(new THREE.BoxGeometry(30.3,20.1,0.2),"piastrelle3.jpg",6);
      scene.add(carta_cuc2);
      carta_cuc2.rotation.x = Math.PI/2;
      carta_cuc2.rotation.y = Math.PI/2;
      carta_cuc2.position.set(0.35,15.16,10);

      var shapeFin_cuc = createMeshRep2(new THREE.ExtrudeGeometry(shapeFin,options),"piastrelle3.jpg",20);
      scene.add(shapeFin_cuc);
      shapeFin_cuc.rotation.x = Math.PI/2;
      shapeFin_cuc.position.set(0,0.5,0);
      shapeFin_cuc.scale.set(100,100,100);

      var shapePorta_fin = createMeshRep2(new THREE.ExtrudeGeometry(shape,options),"piastrelle3.jpg",20);
      shapePorta_fin.rotation.x = 0.5*Math.PI;
      shapePorta_fin.rotation.y = 0.5*Math.PI;
      shapePorta_fin.position.set(30.2,0.16,0);
      shapePorta_fin.scale.set(100,100,100);
      scene.add(shapePorta_fin);

      var carta_matr = createMesh(new THREE.PlaneGeometry(30.3,20.1,0),"cartamatr.jpg");
      scene.add(carta_matr);
      carta_matr.rotation.x = Math.PI/2;
      carta_matr.position.set(15.2,60.91,10.05);

      var carta_matr2 = createMesh(new THREE.PlaneGeometry(48.5,20.1,0),"cartamatr.jpg");
      scene.add(carta_matr2);
      carta_matr2.rotation.x = Math.PI/2;
      carta_matr2.rotation.y = Math.PI/2;
      carta_matr2.position.set(0.4,85,10.05);

      //TO DO : SHAPE SULLA FINESTRA E SULLA PORTA
      var shapeFin_matr = createMeshRep2(new THREE.ExtrudeGeometry(shapeFin,options),"cartamatr.jpg",2);
      scene.add(shapeFin_matr);
      shapeFin_matr.rotation.x = Math.PI/2;
      shapeFin_matr.position.set(0,109.3,0);
      shapeFin_matr.scale.set(100,100,100);

      //shape sulla porta
      var shapePorta = new THREE.Shape();
      shapePorta.moveTo(0,0);
      shapePorta.lineTo(0.483,0);
      shapePorta.lineTo(0.483,0.202);
      shapePorta.lineTo(0,0.202);
      shapePorta.lineTo(0,0);

      var holep = new THREE.Path();
      holep.moveTo(0.083,0);
      holep.lineTo(0.143,0);
      holep.lineTo(0.143,0.14);
      holep.lineTo(0.083,0.14);
      holep.lineTo(0.083,0);
      shapePorta.holes.push(holep);


      var shapePorta_matr = createMeshRep2(new THREE.ExtrudeGeometry(shapePorta,options),"cartamatr.jpg",2);
      shapePorta_matr.rotation.x = 0.5*Math.PI;
      shapePorta_matr.rotation.y = 0.5*Math.PI;
      shapePorta_matr.position.set(30.19,60.5,0);
      shapePorta_matr.scale.set(100,100,100);
      scene.add(shapePorta_matr);
	  
      //bagno
	  var carta_bag = createMeshRep2(new THREE.BoxGeometry(26.3,20.2,0.2),"bagno.jpg",5);
      carta_bag.rotation.x = Math.PI/2;
      carta_bag.rotation.y = Math.PI/2;
      carta_bag.position.set(30.7,96.1,10.1);
      scene.add(carta_bag);

      var carta_bag2 = carta_bag.clone();
      scene.add(carta_bag2);
      carta_bag2.position.set(56.55,96.1,10.1);

      var shapeFin_bag = new THREE.Shape();
      shapeFin_bag.moveTo(0,0);
      shapeFin_bag.lineTo(0.303,0);
      shapeFin_bag.lineTo(0.303,0.202);
      shapeFin_bag.lineTo(0,0.202);
      shapeFin_bag.lineTo(0,0);

      var hole = new THREE.Path();
      hole.moveTo(0.081,0.102);
      hole.lineTo(0.127,0.102);
      hole.lineTo(0.127,0.19);
      hole.lineTo(0.081,0.19);
      hole.lineTo(0.081,0.102);
      shapeFin_bag.holes.push(hole);

      var hole2 = new THREE.Path();
      hole2.moveTo(0.1375,0.102);
      hole2.lineTo(0.185,0.102);
      hole2.lineTo(0.185,0.19);
      hole2.lineTo(0.1375,0.19);
      hole2.lineTo(0.1375,0.102);
      shapeFin_bag.holes.push(hole2);

      var shapeFin2_bag = createMeshRep2(new THREE.ExtrudeGeometry(shapeFin_bag,options),"bagno.jpg",20);
      shapeFin2_bag.rotation.x = 0.5*Math.PI;
      shapeFin2_bag.position.set(30.35,109,0);
      shapeFin2_bag.scale.set(100,100,100);
      scene.add(shapeFin2_bag);

      var shapePorta_bag = createMeshRep2(new THREE.ExtrudeGeometry(shape,options),"bagno.jpg",20);
      shapePorta_bag.rotation.x = 0.5*Math.PI;
      shapePorta_bag.position.set(30.6,83.3,0);
      shapePorta_bag.scale.set(85,100,100);
      scene.add(shapePorta_bag);

      //camera pierpaolo
      var shapePorta_pier = createMeshRep2(new THREE.ExtrudeGeometry(shapePorta,options),"cartaparati_pier.jpg",20);
      shapePorta_pier.rotation.x = 0.5*Math.PI;
      shapePorta_pier.rotation.y = 0.5*Math.PI;
      shapePorta_pier.position.set(56.95,60.7,0);
      shapePorta_pier.scale.set(100,100,100);
      scene.add(shapePorta_pier);

      var shapeFiny = new THREE.Shape();
      shapeFiny.moveTo(0,0);
      shapeFiny.lineTo(0.303,0);
      shapeFiny.lineTo(0.303,0.202);
      shapeFiny.lineTo(0,0.202);
      shapeFiny.lineTo(0,0);

      var hole = new THREE.Path();
      hole.moveTo(0.093,0.102);
      hole.lineTo(0.144,0.102);
      hole.lineTo(0.144,0.19);
      hole.lineTo(0.093,0.19);
      hole.lineTo(0.093,0.102);
      shapeFiny.holes.push(hole);

      var hole2 = new THREE.Path();
      hole2.moveTo(0.157,0.102);
      hole2.lineTo(0.21,0.102);
      hole2.lineTo(0.21,0.19);
      hole2.lineTo(0.157,0.19);
      hole2.lineTo(0.157,0.102);
      shapeFiny.holes.push(hole2);

      var shapeFin_pier = createMeshRep2(new THREE.ExtrudeGeometry(shapeFiny,options),"cartaparati_pier.jpg",20);
      scene.add(shapeFin_pier);
      shapeFin_pier.rotation.x = Math.PI/2;
      shapeFin_pier.position.set(56.95,108.862,0);
      shapeFin_pier.scale.set(93,100,100);

      carta_pier = createMeshRep2(new THREE.BoxGeometry(48.5,20.1,0.2),"cartaparati_pier.jpg",9);
      scene.add(carta_pier);
      carta_pier.rotation.x = Math.PI/2;
      carta_pier.rotation.y = Math.PI/2;
      carta_pier.position.set(84.7,85,10.05);

      carta2_pier = createMeshRep2(new THREE.BoxGeometry(28,20.1,0.2),"cartaparati_pier.jpg",9);
      scene.add(carta2_pier);
      carta2_pier.rotation.x = Math.PI/2;
      carta2_pier.position.set(71,60.91,10.05);


      //salotto
      carta_salotto = createMeshRep2(new THREE.BoxGeometry(28,20.1,0.2),"carta_salotto.jpg",2);
      scene.add(carta_salotto);
      carta_salotto.rotation.x = Math.PI/2;
      carta_salotto.position.set(71,60.5,10.05);

      //shape sulla porta
      var shapeP = new THREE.Shape();
      shapeP.moveTo(0,0);
      shapeP.lineTo(0.5015,0);
      shapeP.lineTo(0.5015,0.202);
      shapeP.lineTo(0,0.202);
      shapeP.lineTo(0,0);

      var hole = new THREE.Path();
      hole.moveTo(0.064,0);
      hole.lineTo(0.189,0);
      hole.lineTo(0.189,0.14);
      hole.lineTo(0.064,0.14);
      hole.lineTo(0.064,0);
      shapeP.holes.push(hole);

      var options = {amount: 0.002,bevelThickness: 2,bevelSize: 1,bevelSegments: 3,bevelEnabled: false,curveSegments: 12,steps: 1};
      var shapeP2 = createMeshRep(new THREE.ExtrudeGeometry(shapeP,options),"carta_salotto.jpg");

      var shapePorta_salotto = createMeshRep2(new THREE.ExtrudeGeometry(shapeP,options),"carta_salotto.jpg",10);
      shapePorta_salotto.rotation.x = 0.5*Math.PI;
      shapePorta_salotto.rotation.y = 0.5*Math.PI;
      shapePorta_salotto.position.set(84.7,0.16,0);
      shapePorta_salotto.scale.set(120,100,100);
      scene.add(shapePorta_salotto);

      //shape sulla porta
      var shapePbis = new THREE.Shape();
      shapePbis.moveTo(0,0);
      shapePbis.lineTo(0.5015,0);
      shapePbis.lineTo(0.5015,0.202);
      shapePbis.lineTo(0,0.202);
      shapePbis.lineTo(0,0);

      var hole = new THREE.Path();
      hole.moveTo(0.0925,0);
      hole.lineTo(0.16,0);
      hole.lineTo(0.16,0.14);
      hole.lineTo(0.0925,0.14);
      hole.lineTo(0.0925,0);
      shapePbis.holes.push(hole);

      var shapePortabis_salotto = createMeshRep2(new THREE.ExtrudeGeometry(shapePbis,options),"carta_salotto.jpg",10);
      shapePortabis_salotto.rotation.x = 0.5*Math.PI;
      shapePortabis_salotto.rotation.y = 0.5*Math.PI;
      shapePortabis_salotto.position.set(56.8,0.17,0);
      shapePortabis_salotto.scale.set(120,100,100);
      scene.add(shapePortabis_salotto);

      var shapeFin_salotto = createMeshRep2(new THREE.ExtrudeGeometry(shapeFin,options),"carta_salotto.jpg",10);
      scene.add(shapeFin_salotto);
      shapeFin_salotto.rotation.x = Math.PI/2;
      shapeFin_salotto.position.set(56.8,0.5,0);
      shapeFin_salotto.scale.set(93,100,100);


      //corridoio
      var shapeC = new THREE.Shape();
      shapeC.moveTo(0,0);
      shapeC.lineTo(0.8515,0);
      shapeC.lineTo(0.8515,0.202);
      shapeC.lineTo(0,0.202);
      shapeC.lineTo(0,0);

      var hole = new THREE.Path();
      hole.moveTo(0.113,0);
      hole.lineTo(0.191,0);
      hole.lineTo(0.191,0.14);
      hole.lineTo(0.113,0.14);
      hole.lineTo(0.113,0);
      shapeC.holes.push(hole);

      var hole2 = new THREE.Path();
      hole2.moveTo(0.415,0);
      hole2.lineTo(0.49,0);
      hole2.lineTo(0.49,0.14);
      hole2.lineTo(0.415,0.14);
      hole2.lineTo(0.415,0);
      shapeC.holes.push(hole2);

      var hole3 = new THREE.Path();
      hole3.moveTo(0.686,0);
      hole3.lineTo(0.745,0);
      hole3.lineTo(0.745,0.14);
      hole3.lineTo(0.686,0.14);
      hole3.lineTo(0.686,0);
      shapeC.holes.push(hole3);

      var shapeC2 = createMeshRep2(new THREE.ExtrudeGeometry(shapeC,options),"carta_corridoio.jpg",6);
      shapeC2.rotation.x = 0.5*Math.PI;
      shapeC2.rotation.y = 0.5*Math.PI;
      shapeC2.position.set(30.5,0.3,0);
      shapeC2.scale.set(100,100,100);
      scene.add(shapeC2);

      var shapePorta_corridoio = createMeshRep2(new THREE.ExtrudeGeometry(shape,options),"carta_corridoio.jpg",6);
      shapePorta_corridoio.rotation.x = 0.5*Math.PI;
      shapePorta_corridoio.position.set(30.6,83,0);
      shapePorta_corridoio.scale.set(85,100,100);
      scene.add(shapePorta_corridoio);


      var shapeCo = new THREE.Shape();
      shapeCo.moveTo(0,0);
      shapeCo.lineTo(0.8515,0);
      shapeCo.lineTo(0.8515,0.202);
      shapeCo.lineTo(0,0.202);
      shapeCo.lineTo(0,0);

      var hole = new THREE.Path();
      hole.moveTo(0.113,0);
      hole.lineTo(0.191,0);
      hole.lineTo(0.191,0.14);
      hole.lineTo(0.113,0.14);
      hole.lineTo(0.113,0);
      shapeCo.holes.push(hole);

      var hole3 = new THREE.Path();
      hole3.moveTo(0.686,0);
      hole3.lineTo(0.745,0);
      hole3.lineTo(0.745,0.14);
      hole3.lineTo(0.686,0.14);
      hole3.lineTo(0.686,0);
      shapeCo.holes.push(hole3);

      var shapeCo2 = createMeshRep2(new THREE.ExtrudeGeometry(shapeCo,options),"carta_corridoio.jpg",6);
      shapeCo2.rotation.x = 0.5*Math.PI;
      shapeCo2.rotation.y = 0.5*Math.PI;
      shapeCo2.position.set(56.5,0.3,0);
      shapeCo2.scale.set(100,100,100);
      scene.add(shapeCo2);

      var shapex = new THREE.Shape();
      shapex.moveTo(0,0);
      shapex.lineTo(0.303,0);
      shapex.lineTo(0.303,0.202);
      shapex.lineTo(0,0.202);
      shapex.lineTo(0,0);

      var hole = new THREE.Path();
      hole.moveTo(0.0765,0);
      hole.lineTo(0.23,0);
      hole.lineTo(0.23,0.14);
      hole.lineTo(0.0765,0.14);
      hole.lineTo(0.0765,0);
      shapex.holes.push(hole);

      var shapePorta_corridoio2 = createMeshRep2(new THREE.ExtrudeGeometry(shapex,options),"carta_corridoio.jpg",6);
      shapePorta_corridoio2.rotation.x = 0.5*Math.PI;
      shapePorta_corridoio2.position.set(30.6,0.5,0);
      shapePorta_corridoio2.scale.set(85,100,100);
      scene.add(shapePorta_corridoio2);


//MURO ESTERNO

//facciata principale
      var shapeMuro = new THREE.Shape();
      shapeMuro.moveTo(0,0);
      shapeMuro.lineTo(0.8515,0);
      shapeMuro.lineTo(0.8515,0.202);
      shapeMuro.lineTo(0,0.202);
      shapeMuro.lineTo(0,0);

//le prime due finestre
      var hole = new THREE.Path();
      hole.moveTo(0.093,0.102);
      hole.lineTo(0.146,0.102);
      hole.lineTo(0.146,0.19);
      hole.lineTo(0.093,0.19);
      hole.lineTo(0.093,0.102);
      shapeMuro.holes.push(hole);

      var hole2 = new THREE.Path();
      hole2.moveTo(0.159,0.102);
      hole2.lineTo(0.212,0.102);
      hole2.lineTo(0.212,0.19);
      hole2.lineTo(0.159,0.19);
      hole2.lineTo(0.159,0.102);
      shapeMuro.holes.push(hole2);

      //portone

      var hole3 = new THREE.Path();
      hole3.moveTo(0.372,0.003);
      hole3.lineTo(0.501,0.003);
      hole3.lineTo(0.501,0.14);
      hole3.lineTo(0.372,0.14);
      hole3.lineTo(0.372,0.003);
      shapeMuro.holes.push(hole3);

      var hole4 = new THREE.Path();
      hole4.moveTo(0.653,0.102);
      hole4.lineTo(0.7035,0.102);
      hole4.lineTo(0.7035,0.19);
      hole4.lineTo(0.653,0.19);
      hole4.lineTo(0.653,0.102);
      shapeMuro.holes.push(hole4);

      var hole5 = new THREE.Path();
      hole5.moveTo(0.715,0.102);
      hole5.lineTo(0.765,0.102);
      hole5.lineTo(0.765,0.19);
      hole5.lineTo(0.715,0.19);
      hole5.lineTo(0.715,0.102);
      shapeMuro.holes.push(hole5);

      var shapeMuro2 = createMeshRep2(new THREE.ExtrudeGeometry(shapeMuro,options),"muro.jpg",10);
      shapeMuro2.rotation.x = 0.5*Math.PI;
      shapeMuro2.position.set(0,0,0);
      shapeMuro2.scale.set(100,100,100);
      scene.add(shapeMuro2);


      //muro sinistra
      var shapeMuroSx = new THREE.Shape();
      shapeMuroSx.moveTo(0,0);
      shapeMuroSx.lineTo(1.096,0);
      shapeMuroSx.lineTo(1.096,0.202);
      shapeMuroSx.lineTo(0,0.202);
      shapeMuroSx.lineTo(0,0);

      var hole = new THREE.Path();
      hole.moveTo(0.398,0.102);
      hole.lineTo(0.451,0.102);
      hole.lineTo(0.451,0.19);
      hole.lineTo(0.398,0.19);
      hole.lineTo(0.398,0.102);
      shapeMuroSx.holes.push(hole);

      var hole2 = new THREE.Path();
      hole2.moveTo(0.464,0.102);
      hole2.lineTo(0.517,0.102);
      hole2.lineTo(0.517,0.19);
      hole2.lineTo(0.464,0.19);
      hole2.lineTo(0.464,0.102);
      shapeMuroSx.holes.push(hole2);

      var shapeMuro2Sx = createMeshRep2(new THREE.ExtrudeGeometry(shapeMuroSx,options),"muro.jpg",10);
      shapeMuro2Sx.rotation.x = 0.5*Math.PI;
      shapeMuro2Sx.rotation.y = Math.PI/2;
      shapeMuro2Sx.position.set(-0.2,-0.2,0);
      shapeMuro2Sx.scale.set(100,100,100);
      scene.add(shapeMuro2Sx);

      //muro dietro

      var shapeMuroDietro = new THREE.Shape();
      shapeMuroDietro.moveTo(0,0);
      shapeMuroDietro.lineTo(0.8515,0);
      shapeMuroDietro.lineTo(0.8515,0.202);
      shapeMuroDietro.lineTo(0,0.202);
      shapeMuroDietro.lineTo(0,0);

      //le prime due finestre
      var hole = new THREE.Path();
      hole.moveTo(0.093,0.102);
      hole.lineTo(0.146,0.102);
      hole.lineTo(0.146,0.19);
      hole.lineTo(0.093,0.19);
      hole.lineTo(0.093,0.102);
      shapeMuroDietro.holes.push(hole);
      var hole2 = new THREE.Path();
      hole2.moveTo(0.159,0.102);
      hole2.lineTo(0.212,0.102);
      hole2.lineTo(0.212,0.19);
      hole2.lineTo(0.159,0.19);
      hole2.lineTo(0.159,0.102);
      shapeMuroDietro.holes.push(hole2);

      var hole3 = new THREE.Path();
      hole3.moveTo(0.384,0.102);
      hole3.lineTo(0.431,0.102);
      hole3.lineTo(0.431,0.19);
      hole3.lineTo(0.384,0.19);
      hole3.lineTo(0.384,0.102);
      shapeMuroDietro.holes.push(hole3);

      var hole4 = new THREE.Path();
      hole4.moveTo(0.441,0.102);
      hole4.lineTo(0.488,0.102);
      hole4.lineTo(0.488,0.19);
      hole4.lineTo(0.441,0.19);
      hole4.lineTo(0.441,0.102);
      shapeMuroDietro.holes.push(hole4);

      //le prime due finestre
      var hole5 = new THREE.Path();
      hole5.moveTo(0.655,0.1025);
      hole5.lineTo(0.703,0.1025);
      hole5.lineTo(0.703,0.189);
      hole5.lineTo(0.655,0.189);
      hole5.lineTo(0.655,0.1025);
      shapeMuroDietro.holes.push(hole5);


      var hole6 = new THREE.Path();
      hole6.moveTo(0.715,0.103);
      hole6.lineTo(0.765,0.103);
      hole6.lineTo(0.765,0.189);
      hole6.lineTo(0.715,0.189);
      hole6.lineTo(0.715,0.103);
      shapeMuroDietro.holes.push(hole6);

      var shapeMuro2Dietro = createMeshRep2(new THREE.ExtrudeGeometry(shapeMuroDietro,options),"muro.jpg",10);
      shapeMuro2Dietro.rotation.x = 0.5*Math.PI;
      shapeMuro2Dietro.position.set(0,109.55,0);
      shapeMuro2Dietro.scale.set(100,100,100);
      scene.add(shapeMuro2Dietro);

      //muro dx
      var shapeDX = new THREE.Shape();
      shapeDX.moveTo(0,0);
      shapeDX.lineTo(0.912,0);
      shapeDX.lineTo(0.915,0.202);
      shapeDX.lineTo(0,0.202);
      shapeDX.lineTo(0,0);

      var hole = new THREE.Path();
      hole.moveTo(0.066,0);
      hole.lineTo(0.19,0);
      hole.lineTo(0.19,0.14);
      hole.lineTo(0.066,0.14);
      hole.lineTo(0.066,0);
      shapeDX.holes.push(hole);

      var options = {amount: 0.002,bevelThickness: 2,bevelSize: 1,bevelSegments: 3,bevelEnabled: false,curveSegments: 12,steps: 1};
      var shapeP2 = createMeshRep(new THREE.ExtrudeGeometry(shapeP,options),"carta_salotto.jpg");

      var shapeDX = createMeshRep2(new THREE.ExtrudeGeometry(shapeDX,options),"muro.jpg",10);
      shapeDX.rotation.x = 0.5*Math.PI;
      shapeDX.rotation.y = 0.5*Math.PI;
      shapeDX.position.set(85.1,-0.05,0);
      shapeDX.scale.set(120,100,100);
      scene.add(shapeDX);

      //balcone

      var cartab = createMeshRep2(new THREE.BoxGeometry(24.35,10.3,0.2),"muro.jpg",2);
      cartab.rotation.x = 0.5 * Math.PI;
      cartab.position.set(97.3,0.08,5.15);
      scene.add(cartab);

      cartab4 = cartab.clone();
      cartab4.position.set(97.3,0.32,5.15);
      scene.add(cartab4);

      cartab2 = cartab.clone();
      cartab2.position.set(97.3,30.29,5.15);
      scene.add(cartab2);

      cartab3 = cartab.clone();
      cartab3.position.set(97.3,30.52,5.15);
      scene.add(cartab3);


      cartab5 = cartab.clone();
      cartab5.rotation.y = Math.PI/2;
      cartab5.position.set(109.45,15.2,5.15);
      cartab5.scale.set(1.25,1,1);
      scene.add(cartab5);

      cartab6 = cartab5.clone();
      cartab6.position.set(109.25,15.2,5.15);
      scene.add(cartab6);
      
}