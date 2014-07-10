function makeRoomM(scene){
	//letto matr

	//comodino 
      var comodino = createMesh(new THREE.BoxGeometry(5,5,5),"comodino2.jpg");
      comodino.rotation.z = Math.PI/2;
      comodino.position.set(3,46,3);
      scene.add(comodino);
      
      var com_dav = createMesh(new THREE.BoxGeometry(5,0.2,5),"comodino.jpg");
      comodino.add(com_dav);
      com_dav.position.set(0,-2.51,0);
      var letto_matr = new THREE.Object3D();

      var gamba1matrGeometry = new THREE.CylinderGeometry(0.5,0.5,2,4,4);
      var gamba1matr=createMesh(gamba1matrGeometry,"wood-2.jpg");
      gamba1matr.castShadow = true; 
      //letto.add(gamba1matr);
      scene.add(gamba1matr);
      gamba1matr.rotation.x =0.5*Math.PI;
      gamba1matr.rotation.y = 0.25*Math.PI;
      gamba1matr.position.set(2,80,1);

      var gamba2matr = gamba1matr.clone();
      //letto_matr.add(gamba2matr);
      scene.add(gamba2matr);
      gamba2matr.position.set(16,80,1);

      var gamba3matr = gamba1matr.clone();
      //letto_matr.add(gamba3matr);
      gamba3matr.position.set(16,94,1);
      scene.add(gamba3matr);

      var gamba4matr = gamba1matr.clone();
      //letto_matr.add(gamba4matr);
      gamba4matr.position.set(15,8,1);

      var materassomatr = createMeshRep(new THREE.BoxGeometry(15,1,15),"coprilettomatr.jpg");
      materassomatr.rotation.x = 0.5*Math.PI;
      //letto.add(materassomatr);
      scene.add(materassomatr);
      materassomatr.position.set(8.9,87,2.5);

      scene.add(letto_matr);
      letto_matr.position.set(1,100,0);

      //comodino 
      var comodino_matr = comodino.clone();
      scene.add(comodino_matr);
      comodino_matr.position.set(4.6,76.8,2.6);

      var comodino_matr2 = comodino.clone();
      scene.add(comodino_matr2);
      comodino_matr2.position.set(4.6,97.2,2.6);

      var quadro_matr = createMesh(new THREE.PlaneGeometry(20,10),"frame5.jpg");
      scene.add(quadro_matr);
      quadro_matr.rotation.x = Math.PI/2;
      quadro_matr.rotation.y = Math.PI/2;
      quadro_matr.position.set(1,87,13);

      var loaderprova3 = new THREE.OBJMTLLoader();
      loaderprova3.addEventListener('load', function (event) {

        var object = event.content;

        var wing2 = object.children[0];
        var wing1 = object.children[1];

        mesh = object;
        mesh.scale.set(0.01,0.01,0.01);
        mesh.rotation.z = -Math.PI/2;
        mesh.position.set(2,87,4);

        scene.add(mesh);
      
      });

      loaderprova3.load(
        '/camera-matrimoniale/Pillow_Obj.obj',
        '/camera-matrimoniale/Pillow_Obj.mtl',
        {side: THREE.DoubleSide}
      );


      var loader6 = new THREE.OBJMTLLoader();
        loader6.addEventListener('load', function (event) {

            var object = event.content;

            var wing2 = object.children[0];
            var wing1 = object.children[1];

            mesh = object;
            mesh.position.set(15,70,13);
            mesh.rotation.x = Math.PI/2;
            scene.add(mesh);
      
        });


      loader6.load(
        '/sala/hanging-restaurant-light.obj',
        '/sala/hanging-restaurant-light.mtl',
        {side: THREE.DoubleSide}
      );


      var interGeometry = new THREE.BoxGeometry(0.5,1.2,1.2);
      var interMaterial = new THREE.MeshLambertMaterial({color: 0xF5DEB3});
      var inter = new THREE.Mesh(interGeometry,interMaterial);
      inter.position.set(30,80,10);
      scene.add(inter);

      var botGeometry = new THREE.BoxGeometry(0.3,0.5,0.5);
      var botMaterial = new THREE.MeshLambertMaterial({color: 0xF5DEB3});
      var bot = new THREE.Mesh(botGeometry,botMaterial);
      bot.position.set(29.8,80,10);
      scene.add(bot);

      window.location.luceMatrOn = 1 ; // 0=spento
      var pointMatr = new THREE.PointLight(0xffffff);
      pointMatr.position.set(15,75,13);
      pointMatr.castShadow = true;
      pointMatr.intensity = 0.5;
      pointMatr.shadowCameraNear = 10;
      pointMatr.shadowCameraFar = 200;
      scene.add(pointMatr);

      document.addEventListener('mousedown',onDocumentMouseDown,false);
      function onDocumentMouseDown(event) {

        event.preventDefault();
        if(!window.location.pointerLock){
            var vector = new THREE.Vector3((event.clientX / window.innerWidth)*2-1,-(event.clientY/window.innerHeight)*2+1,0.5);
            projector.unprojectVector( vector, camera );
            var raycaster = new THREE.Raycaster(camera.position,vector.sub(camera.position).normalize());
            var intersects = raycaster.intersectObjects([bot])
            if(window.location.campanello){
              if(intersects.length > 0){
                luce6(intersects[0].object);
                if(window.location.luceMatrOn === 1){
                  pointMatr.intensity =0 ;
                  window.location.luceMatrOn = 0;
                }
                else if(window.location.luceMatrOn === 0 ){
                  pointMatr.intensity =0.5;
                  window.location.luceMatrOn = 1;
                }
              }
            }
            
        }
        else{
            event.preventDefault();
            var vector2 = new THREE.Vector3(10,10,10);
            projector.unprojectVector( vector2, camera );
            var raycaster = new THREE.Raycaster(vector2,controls.getDirection(new THREE.Vector3(0, 0, 0)).clone());
            var intersects = raycaster.intersectObjects([bot])
            if(window.location.campanello){
              if(intersects.length > 0){
                luce6(intersects[0].object);
                if(window.location.luceMatrOn === 1){
                  pointMatr.intensity =0 ;
                  window.location.luceMatrOn = 0;
                }
                else if(window.location.luceMatrOn === 0 ){
                  pointMatr.intensity =0.5;
                  window.location.luceMatrOn = 1;
                }
              }
            }
            
        }
      }


}