function makeWindows(scene){

      //finestre vale
      var fin = createMesh(new THREE.BoxGeometry(5.32,8.87,0.3),"bordo.jpg");
      fin.aperta = false;
      var plane = createMesh(new THREE.BoxGeometry(5.32,8.87,0.01),"finestra1vetro.jpg");
      var plane2 = createMesh(new THREE.BoxGeometry(5.32,8.87,0.01),"finestra2vetro.jpg");
      fin.add(plane);
      fin.add(plane2);
      plane.position.set(0,0,-0.16);
      plane2.position.set(0,0,0.16);
      var fin_cuc = fin.clone();
      fin_cuc.aperta = false;
      var fin_matr = fin.clone();
      fin_matr.aperta = false;
      var fin_bag = fin.clone();
      fin_bag.aperta = false;
      var fin_pier = fin.clone();
      fin_pier.aperta = false;
      var fin_salotto = fin.clone();
      fin_salotto.aperta = false;
      fin.rotation.x = 0.5*Math.PI;
      fin.rotation.y = 0.5*Math.PI;
      fin.position.set(0.1,-2.65,4.13);
      //scene.add(fin);

      var pernoFinDx = new THREE.Object3D();
      pernoFinDx.add(fin);
      scene.add(pernoFinDx);
      pernoFinDx.position.set(0,51.55,10.5);


      var fin2 = createMesh(new THREE.BoxGeometry(5.32,8.87,0.3),"bordo.jpg");
      fin2.aperta= false;
      var plane3 = createMesh(new THREE.BoxGeometry(5.32,8.87,0.01),"finestra2vetro.jpg");
      var plane4 = createMesh(new THREE.BoxGeometry(5.32,8.87,0.01),"finestra1vetro.jpg");
      fin2.add(plane3);
      fin2.add(plane4);
      plane3.position.set(0,0,-0.16);
      plane4.position.set(0,0,0.16);
      var fin2_cuc = fin2.clone();
      var fin2_matr = fin2.clone();
      var fin2_bag = fin2.clone();
      var fin2_pier = fin2.clone();
      var fin2_salotto = fin2.clone();
      fin2_cuc.aperta = false;
      fin2_matr.aperta = false;
      fin2_bag.aperta = false;
      fin2_pier.aperta = false;
      fin2_salotto.aperta = false;
      fin2.rotation.x = 0.5*Math.PI;
      fin2.rotation.y = 0.5*Math.PI;
      fin2.position.set(0.1,2.65,4.13);
      //scene.add(fin2);

      var pernoFinSx = new THREE.Object3D();
      pernoFinSx.add(fin2);
      scene.add(pernoFinSx);
      pernoFinSx.position.set(0.1,39.68,10.5);


      //finestre cucina
      fin_cuc.rotation.x = 0.5*Math.PI;
      fin_cuc.position.set(-2.66,0,4);

      
      var pernoFinDx_cuc = new THREE.Object3D();
      pernoFinDx_cuc.add(fin_cuc);
      scene.add(pernoFinDx_cuc);
      pernoFinDx_cuc.position.set(21.2,0.2,10.8);

      fin2_cuc.rotation.x = 0.5*Math.PI;
      fin2_cuc.position.set(2.66,0,4);

      var pernoFinSx_cuc = new THREE.Object3D();
      //var pernoFinSx_cuc = createMesh(new THREE.BoxGeometry(1,1,1),"prato.jpg");
      pernoFinSx_cuc.add(fin2_cuc);
      scene.add(pernoFinSx_cuc);
      pernoFinSx_cuc.position.set(9.35,0.2,10.7);

      //finestra camera matrimoniale
      fin_matr.rotation.x = 0.5*Math.PI;
      fin_matr.position.set(-2.66,0,4);

      var pernoFinDx_matr = new THREE.Object3D();
      pernoFinDx_matr.add(fin_matr);
      scene.add(pernoFinDx_matr);
      pernoFinDx_matr.position.set(21.2,109,10.7);

      fin2_matr.rotation.x = 0.5*Math.PI;
      fin2_matr.position.set(2.66,0,4);

      var pernoFinSx_matr = new THREE.Object3D();
      pernoFinSx_matr.add(fin2_matr);
      scene.add(pernoFinSx_matr);
      pernoFinSx_matr.position.set(9.2,109,10.7);

      //finestre bagno
      fin_bag.rotation.x = 0.5*Math.PI;
      fin_bag.position.set(-2.66,0,4);
      fin_bag.scale.set(0.865,1,1);

      var pernoFinDx_bag =  new THREE.Object3D();
      pernoFinDx_bag.add(fin_bag);
      scene.add(pernoFinDx_bag);
      pernoFinDx_bag.position.set(49.1,109.3,10.5);

      fin2_bag.scale.set(0.87,1,1);
      fin2_bag.rotation.x = 0.5*Math.PI;
      fin2_bag.position.set(2.66,0,4);

      var pernoFinSx_bag =  new THREE.Object3D();
      pernoFinSx_bag.add(fin2_bag);
      scene.add(pernoFinSx_bag);
      pernoFinSx_bag.position.set(38.1,109.3,10.5);

      //camera pierpaolo
      fin_pier.rotation.x = 0.5*Math.PI;
      fin_pier.position.set(-2.66,0,4);

      var pernoFinDx_pier = new THREE.Object3D();
      pernoFinDx_pier.add(fin_pier);
      scene.add(pernoFinDx_pier);
      pernoFinDx_pier.position.set(77,109,10.5);


      fin2_pier.scale.set(0.9,1,1);
      fin2_pier.rotation.x = 0.5*Math.PI;
      fin2_pier.position.set(2.66,0,4);

      var pernoFinSx_pier = createMesh(new THREE.BoxGeometry(1,1,1),"prato.jpg");
      pernoFinSx_pier.add(fin2_pier);
      scene.add(pernoFinSx_pier);
      pernoFinSx_pier.position.set(65.3,109,10.5);

      var pernoFinDx_bag = createMesh(new THREE.BoxGeometry(1,1,1),"prato.jpg");


      //salotto
      fin_salotto.rotation.x = 0.5*Math.PI;
      fin_salotto.position.set(-2.66,0,4);

      
      var pernoFinDx_salotto = new THREE.Object3D();
      pernoFinDx_salotto.add(fin_salotto);
      scene.add(pernoFinDx_salotto);
      pernoFinDx_salotto.position.set(76.5,0.2,10.8);

      fin2_salotto.rotation.x = 0.5*Math.PI;
      fin2_salotto.position.set(2.66,0,4);

      var pernoFinSx_salotto = new THREE.Object3D();
      //var pernoFinSx_cuc = createMesh(new THREE.BoxGeometry(1,1,1),"prato.jpg");
      pernoFinSx_salotto.add(fin2_salotto);
      scene.add(pernoFinSx_salotto);
      pernoFinSx_salotto.position.set(65.2,0.2,10.7);


      //per il balcone

      document.addEventListener('mousedown',onDocumentMouseDown,false);
      function onDocumentMouseDown(event) {

        event.preventDefault();
        if(!window.location.pointerLock){
            var vector = new THREE.Vector3((event.clientX / window.innerWidth)*2-1,-(event.clientY/window.innerHeight)*2+1,0.5);
            projector.unprojectVector( vector, camera );
            var raycaster = new THREE.Raycaster(camera.position,vector.sub(camera.position).normalize());
            var intersects = raycaster.intersectObjects([fin,fin2_cuc,fin_bag,fin_matr,fin_pier,fin2_salotto]);
            var intersects2 = raycaster.intersectObjects([fin2,fin_cuc,fin2_bag,fin2_matr,fin2_pier,fin_salotto]);
            if(window.location.campanello){
              if ( intersects.length > 0 ) {
                if(!intersects[0].object.aperta){
                    apri(intersects[0].object.parent);
                    intersects[0].object.aperta = true;
                }
                else{
                    chiudi(intersects[0].object.parent);
                    intersects[0].object.aperta = false;
                }
              }

              if ( intersects2.length > 0 ) {
                if(!intersects2[0].object.aperta){
                    apri2(intersects2[0].object.parent);
                    intersects2[0].object.aperta = true;
                }
                else{
                    chiudi(intersects2[0].object.parent);
                    intersects2[0].object.aperta = false;
                }
              }
            }
            
        }
        else{
            event.preventDefault();
            var vector2 = new THREE.Vector3(10,10,10);
            projector.unprojectVector( vector2, camera );
            var raycaster = new THREE.Raycaster(vector2,controls.getDirection(new THREE.Vector3(0, 0, 0)).clone());
            var intersects = raycaster.intersectObjects([fin,fin2_cuc,fin_bag,fin_matr,fin_pier,fin2_salotto]);
            var intersects2 = raycaster.intersectObjects([fin2,fin_cuc,fin2_bag,fin2_matr,fin2_pier,fin_salotto]);

            if(window.location.campanello){
              if ( intersects.length > 0 ) {
                if(!intersects[0].object.aperta){
                    apri(intersects[0].object.parent);
                    intersects[0].object.aperta = true;
                }
                else{
                    chiudi(intersects[0].object.parent);
                    intersects[0].object.aperta = false;
                }
              }

              if ( intersects2.length > 0 ) {
                if(!intersects2[0].object.aperta){
                    apri2(intersects2[0].object.parent);
                    intersects2[0].object.aperta = true;
                }
                else{
                    chiudi(intersects2[0].object.parent);
                    intersects2[0].object.aperta = false;
                }
              }
            }
        }


    }
}
