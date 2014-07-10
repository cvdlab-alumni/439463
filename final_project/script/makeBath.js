function makeBath(scene){
//carico il lavandino
      var loaderbagno = new THREE.OBJMTLLoader();
      loaderbagno.addEventListener('load', function (event) {

        var object = event.content;

        var wing2 = object.children[0];
        var wing1 = object.children[1];

        mesh = object;
        mesh.scale.set(0.02,0.02,0.02);
        mesh.rotation.x = Math.PI/2;
        mesh.rotation.y = Math.PI/2;
        mesh.position.set(34.3,103,6);

        scene.add(mesh);
      
      });

      loaderbagno.load(
        '/bagno/lavandinobagno.obj',
        {side: THREE.DoubleSide}
      );

      //carico la vasca
      var loaderbagno2 = new THREE.OBJMTLLoader();
      loaderbagno2.addEventListener('load', function (event) {

        var object = event.content;
        var wing2 = object.children[0];
        var wing1 = object.children[1];

        mesh = object;
        mesh.scale.set(0.04,0.04,0.04);
        mesh.rotation.x = Math.PI/2;
        mesh.rotation.y = Math.PI/2;
        mesh.position.set(52,96,1);

        scene.add(mesh);
      
      });

      loaderbagno2.load(
        '/bagno/vasca.obj',
        {side: THREE.DoubleSide}
      );

      //carico il water
      var loaderbagno3 = new THREE.OBJMTLLoader();
      loaderbagno3.addEventListener('load', function (event) {

        var object = event.content;
        var wing2 = object.children[0];
        var wing1 = object.children[1];

        mesh = object;
        mesh.scale.set(0.4,0.4,0.4);
        mesh.rotation.x = Math.PI/2;
        mesh.rotation.y = Math.PI/2;
        mesh.position.set(34,96,1);

        scene.add(mesh);
      
      });

      loaderbagno3.load(
        '/bagno/water.obj',
        {side: THREE.DoubleSide}
      );

      var cubeGeom = new THREE.CubeGeometry(1, 5, 5, 1, 1, 1);
      mirrorCubeCamera = new THREE.CubeCamera( 0.1, 5000, 512 );
      // mirrorCubeCamera.renderTarget.minFilter = THREE.LinearMipMapLinearFilter;
      scene.add( mirrorCubeCamera );
      var mirrorCubeMaterial = new THREE.MeshBasicMaterial( { envMap: mirrorCubeCamera.renderTarget } );
      mirrorCube = new THREE.Mesh( cubeGeom, mirrorCubeMaterial );
      mirrorCube.position.set(31,102,15);
      mirrorCubeCamera.position = mirrorCube.position;
      scene.add(mirrorCube);

      var toreturn = [mirrorCube,mirrorCubeCamera];


       var loader6 = new THREE.OBJMTLLoader();
        loader6.addEventListener('load', function (event) {

            var object = event.content;

            var wing2 = object.children[0];
            var wing1 = object.children[1];

            mesh = object;
            mesh.position.set(40,95,13);
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
      inter.position.set(30.8,95,10);
      scene.add(inter);

      var botGeometry = new THREE.BoxGeometry(0.3,0.5,0.5);
      var botMaterial = new THREE.MeshLambertMaterial({color: 0xF5DEB3});
      var bot = new THREE.Mesh(botGeometry,botMaterial);
      bot.position.set(31,95,10);
      scene.add(bot);

      window.location.luceBagOn = 1 ; // 0=spento
      var pointBag = new THREE.PointLight(0xffffff);
      pointBag.position.set(40,95,13);
      pointBag.castShadow = true;
      pointBag.intensity = 0.5;
      pointBag.shadowCameraNear = 10;
      pointBag.shadowCameraFar = 200;
      scene.add(pointBag);

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
                luce7(intersects[0].object);
                if(window.location.luceBagOn === 1){
                  pointBag.intensity =0 ;
                  window.location.luceBagOn = 0;
                }
                else if(window.location.luceBagOn === 0 ){
                  pointBag.intensity =0.5;
                  window.location.luceBagOn = 1;
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
                luce7(intersects[0].object);
                if(window.location.luceBagOn === 1){
                  pointBag.intensity =0 ;
                  window.location.luceBagOn = 0;
                }
                else if(window.location.luceBagOn === 0 ){
                  pointBag.intensity =0.5;
                  window.location.luceBagOn = 1;
                }
              }
            }
            
        }
      }


      return toreturn;

    }
