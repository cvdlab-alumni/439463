function makePierRoom(scene){

	var comodino = createMesh(new THREE.BoxGeometry(5,5,5),"comodino2.jpg");
      comodino.rotation.z = Math.PI/2;
      comodino.position.set(3,46,3);
      scene.add(comodino);
      
      var com_dav = createMesh(new THREE.BoxGeometry(5,0.2,5),"comodino.jpg");
      comodino.add(com_dav);
      com_dav.position.set(0,-2.51,0);
      var letto_matr = new THREE.Object3D();

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

	  scene.add(letto_pier);
      letto_pier.position.set(68,80,0);

      var materasso_pier = createMeshRep(new THREE.BoxGeometry(15,1,8),"copertapier.jpg");
      materasso_pier.rotation.x = 0.5*Math.PI;
      scene.add(materasso_pier);
      materasso_pier.position.set(75.7,84.1,3);

      //comodino pier 
      var comodino_pier = comodino.clone();
      scene.add(comodino_pier);
      comodino_pier.rotation.z= 3*Math.PI/2;
      comodino_pier.position.set(80,76.8,2.6);


      //carico la vasca
      var loaderpier = new THREE.OBJMTLLoader();
      loaderpier.addEventListener('load', function (event) {

        var object = event.content;
        var wing2 = object.children[0];
        var wing1 = object.children[1];

        mesh = object;
        mesh.scale.set(0.1,0.1,0.1);
        mesh.rotation.x = Math.PI/2;
        mesh.position.set(75,100,4);

        scene.add(mesh);
      
      });

      loaderpier.load(
        '/scrivania-pier/bureau3.obj',
        '/scrivania-pier/bureau3.mtl',
        {side: THREE.DoubleSide}
      );

      //carico la vasca
      var loaderpier2 = new THREE.OBJMTLLoader();
      loaderpier2.addEventListener('load', function (event) {

        var object = event.content;
        var wing2 = object.children[0];
        var wing1 = object.children[1];

        chair = object;
        chair.scale.set(0.1,0.1,0.1);
        chair.rotation.x = Math.PI/2;
        chair.rotation.y = 3*Math.PI/2;
        chair.position.set(95,130,12);
        scene.add(chair);

        document.addEventListener('mousedown',onDocumentMouseDown,false);
        function onDocumentMouseDown(event) {

        event.preventDefault();
        if(!window.location.pointerLock){
            var vector = new THREE.Vector3((event.clientX / window.innerWidth)*2-1,-(event.clientY/window.innerHeight)*2+1,0.5);
            projector.unprojectVector( vector, camera );
            var raycaster = new THREE.Raycaster(camera.position,vector.sub(camera.position).normalize());
            var intersects = raycaster.intersectObjects([wing2,wing1]);
            console.log(intersects);
            if(window.location.campanello){   
              if ( intersects.length > 0 ) {
                spostaSedia(intersects[0].object.parent);
              }
            }
            
        }
        else{
            event.preventDefault();
            var vector2 = new THREE.Vector3(10,10,10);
            projector.unprojectVector( vector2, camera );
            var raycaster = new THREE.Raycaster(vector2,controls.getDirection(new THREE.Vector3(0, 0, 0)).clone());
            var intersects = raycaster.intersectObjects([wing1,wing2]);

            if(window.location.campanello){
              if ( intersects.length > 0 ) {
                spostaSedia(intersects[0].object.parent);
              }
            }
            
        }
      }
      
      });

      loaderpier2.load(
        '/chair-pier/officeChair.obj',
        '/chair-pier/officeChair.mtl',
        {side: THREE.DoubleSide}
      );


      var loaderpier3 = new THREE.OBJMTLLoader();
      loaderpier3.addEventListener('load', function (event) {

        var object = event.content;
        var wing2 = object.children[0];
        var wing1 = object.children[1];

        tv = object;
        tv.scale.set(10,10,10);
        tv.rotation.x = Math.PI/2;
        tv.position.set(75,90,13.5);
        scene.add(tv);
      
      });

      loaderpier3.load(
        '/scrivania-pier/monitorLCD.obj',
        '/scrivania-pier/monitorLCD.mtl',
        {side: THREE.DoubleSide}
      );

      var interGeometry = new THREE.BoxGeometry(0.5,1.2,1.2);
      var interMaterial = new THREE.MeshLambertMaterial({color: 0xF5DEB3});
      var inter = new THREE.Mesh(interGeometry,interMaterial);
      inter.position.set(57,90,10);
      scene.add(inter);

      var botGeometry = new THREE.BoxGeometry(0.3,0.5,0.5);
      var botMaterial = new THREE.MeshLambertMaterial({color: 0xF5DEB3});
      var bot = new THREE.Mesh(botGeometry,botMaterial);
      bot.position.set(57.2,90,10);
      scene.add(bot);


       var loader6 = new THREE.OBJMTLLoader();
        loader6.addEventListener('load', function (event) {

            var object = event.content;

            var wing2 = object.children[0];
            var wing1 = object.children[1];

            mesh = object;
            mesh.position.set(65,92,13);
            mesh.rotation.x = Math.PI/2;
            scene.add(mesh);
      
        });


      loader6.load(
        '/sala/hanging-restaurant-light.obj',
        '/sala/hanging-restaurant-light.mtl',
        {side: THREE.DoubleSide}
      );


      var pointPier = new THREE.PointLight(0xffffff);
      pointPier.position.set(65,92,10);
      pointPier.castShadow = true;
      pointPier.intensity = 1;
      pointPier.shadowCameraNear = 10;
      pointPier.shadowCameraFar = 200;
      scene.add(pointPier);

       function onWindowResize() {
                camera.aspect = window.innerWidth / window.innerHeight;
                camera.updateProjectionMatrix();
                renderer.setSize(window.innerWidth, window.innerHeight);
      }


      // create the video element
      videoC = document.createElement( 'video' );
      // video.id = 'video';
      // video.type = ' video/ogg; codecs="theora, vorbis" ';
      videoC.src = "assets/textures/trailer-ironman.avi";
      videoC.load(); // must call after setting/changing source
      videoC.play();
  
      videoCImage = document.createElement( 'canvas' );
      //videoImage.width = 480;
      //videoImage.height = 204;

      videoCImage.width = 1200;
      videoCImage.height = 500;

      videoCImageContext = videoCImage.getContext( '2d' );
      // background color if no video present
      videoCImageContext.fillStyle = '#000000';
      videoCImageContext.fillRect( 0, 0, videoCImage.width, videoCImage.height );

      videoCTexture = new THREE.Texture( videoCImage );
      videoCTexture.minFilter = THREE.LinearFilter;
      videoCTexture.magFilter = THREE.LinearFilter;
  
      var movieCMaterial = new THREE.MeshBasicMaterial( { map: videoCTexture, overdraw: true, side:THREE.DoubleSide } );
      // the geometry on which the movie will be displayed;
      //    movie image will be scaled to fit these dimensions.
      var movieCGeometry = new THREE.PlaneGeometry( 6.2, 3.85, 4, 4 );
      var movieCScreen = new THREE.Mesh( movieCGeometry, movieCMaterial );
      movieCScreen.rotation.x = Math.PI/2;
      //movieScreen.position.set(3.8,4.4,9); //il primo avvicina lo schermo alla tv
      movieCScreen.position.set(75,98.7,11.2);
      scene.add(movieCScreen);
      var toreturn = [videoC,movieCScreen,videoCImageContext,videoCTexture]


      var loaderpier4 = new THREE.OBJMTLLoader();
      loaderpier4.addEventListener('load', function (event) {

        var object = event.content;
        console.log(object);
        var wing1 = object.children[0];

        tr = object;
        tr.scale.set(0.4,0.4,0.4);
        tr.rotation.x = Math.PI/2;
        tr.rotation.y = -Math.PI/2;
        tr.position.set(80,86,3.7);
        scene.add(tr);

    /*    document.addEventListener('mousedown',onDocumentMouseDown,false);
        function onDocumentMouseDown(event) {

        event.preventDefault();
        if(!window.location.pointerLock){
            var vector = new THREE.Vector3((event.clientX / window.innerWidth)*2-1,-(event.clientY/window.innerHeight)*2+1,0.5);
            projector.unprojectVector( vector, camera );
            var raycaster = new THREE.Raycaster(camera.position,vector.sub(camera.position).normalize());
            var intersects = raycaster.intersectObjects([wing1]);

            if ( intersects.length > 0 ) {
              console.log("prova");
              movieCScreen.visible = false;
              console.log("prova2")
            }
            
        }
        else{
            event.preventDefault();
            var vector2 = new THREE.Vector3(10,10,10);
            projector.unprojectVector( vector2, camera );
            var raycaster = new THREE.Raycaster(vector2,controls.getDirection(new THREE.Vector3(0, 0, 0)).clone());
            var intersects = raycaster.intersectObjects([door,door_cuc,door_matr,door_bag]);

            if ( intersects.length > 0 ) {
                apri(intersects[0].object.parent);
            }
            
        }
      };*/
      
      });

      loaderpier4.load(
        '/scrivania-pier/remote.obj',
        '/scrivania-pier/remote.mtl',
        {side: THREE.DoubleSide}
      );


      window.location.luce = 1; //1 = acceso

      window.location.controlVideo = 0; // 0 =spento

      document.addEventListener('mousedown',onDocumentMouseDown,false);
      function onDocumentMouseDown(event) {

        event.preventDefault();
        if(!window.location.pointerLock){
            var vector = new THREE.Vector3((event.clientX / window.innerWidth)*2-1,-(event.clientY/window.innerHeight)*2+1,0.5);
            projector.unprojectVector( vector, camera );
            var raycaster = new THREE.Raycaster(camera.position,vector.sub(camera.position).normalize());
            var intersects = raycaster.intersectObjects([bot]);
            var intersectvideo = raycaster.intersectObjects([movieCScreen]);
          
          if(window.location.campanello){
            if ( intersects.length > 0 ) {
                luce(intersects[0].object);
                if(window.location.luce === 1){
                  pointPier.intensity = 0;
                  window.location.luce = 0;
                }
                else if (window.location.luce === 0){
                  pointPier.intensity = 1;
                  window.location.luce = 1;
                }
            }

            if ( intersectvideo.length > 0 ) {
                if(window.location.controlVideo === 0){
                  videoC.play()
                  window.location.controlVideo= 1;
                }
                else if (window.location.controlVideo === 1){
                  videoC.pause()
                  window.location.controlVideo= 0;
                }
            }
          }
            
        }
        else{
            event.preventDefault();
            var vector2 = new THREE.Vector3(10,10,10);
            projector.unprojectVector( vector2, camera );
            var raycaster = new THREE.Raycaster(vector2,controls.getDirection(new THREE.Vector3(0, 0, 0)).clone());
            var intersects = raycaster.intersectObjects([bot]);
            var intersectvideo = raycaster.intersectObjects([movieCScreen]);

            if(window.location.campanello){
            if ( intersects.length > 0 ) {
                luce(intersects[0].object);
                if(window.location.luce === 1){
                  pointPier.intensity = 0;
                  window.location.luce = 0;
                }
                else if (window.location.luce === 0){
                  pointPier.intensity = 1;
                  window.location.luce = 1;
                }
            }

            if ( intersectvideo.length > 0 ) {
                if(window.location.controlVideo === 0){
                  videoC.play()
                  window.location.controlVideo= 1;
                }
                else if (window.location.controlVideo === 1){
                  videoC.pause()
                  window.location.controlVideo= 0;
                }
            }
          }
            
        }
      
      }


      videoC.pause();
      return toreturn;

}