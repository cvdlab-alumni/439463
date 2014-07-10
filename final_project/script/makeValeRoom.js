function makeValeRoom(scene){
	var letto = new THREE.Object3D();

      var gamba1Geometry = new THREE.CylinderGeometry(0.5,0.5,2,4,4);
      var gamba1=createMesh(gamba1Geometry,"wood-2.jpg");
      gamba1.castShadow = true; 
      letto.add(gamba1);
      gamba1.rotation.x =0.5*Math.PI;
      gamba1.rotation.y = 0.25*Math.PI;
      gamba1.position.set(0.7,0.7,1);

      var gamba2 = gamba1.clone();
      letto.add(gamba2);
      gamba2.position.set(15,0.7,1);

      var gamba3 = gamba1.clone();
      letto.add(gamba3);
      gamba3.position.set(0.7,8,1);

      var gamba4 = gamba1.clone();
      letto.add(gamba4);
      gamba4.position.set(15,8,1);

      var letto_pier = letto.clone();

      var materasso = createMeshRep(new THREE.BoxGeometry(15,1,8),"trapuntabis.jpg");
      materasso.rotation.x = 0.5*Math.PI;
      letto.add(materasso);
      materasso.position.set(8,4.3,2);

      scene.add(letto);
      letto.position.set(1,50,0);

      var cuscinoGeometry = new THREE.BoxGeometry(3,1,6);
      var cuscinoMaterial = new THREE.MeshLambertMaterial({color: 0xFFFFF0});
      var cuscino = new THREE.Mesh(cuscinoGeometry,cuscinoMaterial);
      cuscino.rotation.x = 0.5*Math.PI;
      letto.add(cuscino);
      cuscino.position.set(2,4.3,3);
      letto.castShadow = true;

      //armadio 
      var armadio = new THREE.Object3D();
      var anta1 = createMesh(new THREE.BoxGeometry(14,18,1),"parquet.jpg");
      anta1.rotation.x = 0.5*Math.PI;
      scene.add(anta1);
      anta1.position.set(10,31,9.1);

      var anta2 = createMesh(new THREE.BoxGeometry(5,18,1),"parquet.jpg");
      anta2.rotation.x = 0.5*Math.PI;
      anta2.rotation.y = 0.5*Math.PI;
      scene.add(anta2);
      anta2.position.set(16.5,33.5,9.1)

      var anta3 = anta2.clone();
      armadio.add(anta3);
      anta3.position.set(3.5,33.5,9.1);

      var anta4 = createMesh(new THREE.BoxGeometry(14,5,1),"parquet.jpg");
      scene.add(anta4);
      anta4.position.set(10,33.5,0.5);
      
      var anta5 = anta4.clone();
      scene.add(anta5);
      anta5.position.set(10,33.5,17.6);

      var anta6 = createMesh(new THREE.BoxGeometry(7,18,1),"parquet.jpg");
      anta6.rotation.x = 0.5 * Math.PI;
      anta6.position.set(3.5,0,9);
      var perno = new THREE.Object3D();
      scene.add(perno);
      perno.position.set(3,36,0);
      perno.add(anta6);

      var anta7 = createMesh(new THREE.BoxGeometry(7,18,1),"parquet.jpg");
      anta7.rotation.x = 0.5 *Math.PI;
      anta7.position.set(-3.5,0,9);
      var perno2 = new THREE.Object3D();
      scene.add(perno2);
      perno2.position.set(17,36,0);
      perno2.add(anta7);
      armadio.castShadow = true;

      scene.add(armadio);

      //comodino 
      var comodino = createMesh(new THREE.BoxGeometry(5,5,5),"comodino2.jpg");
      comodino.rotation.z = Math.PI/2;
      comodino.position.set(3,46,3);
      scene.add(comodino);
      
      var com_dav = createMesh(new THREE.BoxGeometry(5,0.2,5),"comodino.jpg");
      comodino.add(com_dav);
      com_dav.position.set(0,-2.51,0);


      //quadro
      var quadro = createMesh(new THREE.PlaneGeometry(10,10),"cornice3.jpg");
      scene.add(quadro);
      quadro.rotation.x = Math.PI/2;
      quadro.position.set(15,60.5,15);


      var loader6 = new THREE.OBJMTLLoader();
        loader6.addEventListener('load', function (event) {

            var object = event.content;

            var wing2 = object.children[0];
            var wing1 = object.children[1];

            mesh = object;
            mesh.position.set(15,45,13);
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
      inter.position.set(30,58,10);
      scene.add(inter);

      var botGeometry = new THREE.BoxGeometry(0.3,0.5,0.5);
      var botMaterial = new THREE.MeshLambertMaterial({color: 0xF5DEB3});
      var bot = new THREE.Mesh(botGeometry,botMaterial);
      bot.position.set(29.8,58,10);
      scene.add(bot);

      window.location.luceValeOn = 1 ; // 0=spento
      var pointVale = new THREE.PointLight(0xffffff);
      pointVale.position.set(15,45,13);
      pointVale.castShadow = true;
      pointVale.intensity = 0.5;
      pointVale.shadowCameraNear = 10;
      pointVale.shadowCameraFar = 200;
      scene.add(pointVale);

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
                luce4(intersects[0].object);
                if(window.location.luceValeOn === 1){
                  pointVale.intensity =0 ;
                  window.location.luceValeOn = 0;
                }
                else if(window.location.luceValeOn === 0 ){
                  pointVale.intensity =0.5;
                  window.location.luceValeOn = 1;
                }
              }
            }
            
        }
        else{
            event.preventDefault();
            var vector2 = new THREE.Vector3(10,10,10);
            projector.unprojectVector( vector2, camera );
            var raycaster = new THREE.Raycaster(vector2,controls.getDirection(new THREE.Vector3(0, 0, 0)).clone());
            var intersects = raycaster.intersectObjects([prova])
            var intersects2 = raycaster.intersectObjects([bot])
            var intersects3 = raycaster.intersectObjects([bot2])
            if(window.location.campanello){
              if(intersects.length > 0){
                luce4(intersects[0].object);
                if(window.location.luceValeOn === 1){
                  pointVale.intensity =0 ;
                  window.location.luceValeOn = 0;
                }
                else if(window.location.luceSalaOn === 0 ){
                  pointVale.intensity =0.5;
                  window.location.luceValeOn = 1;
                }
              }
            }
            
        }
      }


}