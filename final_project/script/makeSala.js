function makeSala(scene){

	var loader = new THREE.OBJMTLLoader();
      loader.addEventListener('load', function (event) {

        var object = event.content;

        var wing2 = object.children[0];
        var wing1 = object.children[1];

        mesh = object;
        mesh.scale.set(2,2,2);
        mesh.rotation.x = Math.PI/2;
        mesh.position.set(73,80,2);
        scene.add(mesh);
      
      });


      loader.load(
        '/sala/largeCouch.obj',
        '/sala/largeCouch.mtl',
        {side: THREE.DoubleSide}
      );

      var loader2 = new THREE.OBJMTLLoader();
      loader2.addEventListener('load', function (event) {

        var object = event.content;

        var wing2 = object.children[0];
        var wing1 = object.children[1];

        mesh = object;
        mesh.scale.set(0.1,0.1,0.1);
        mesh.rotation.x = Math.PI/2;
        mesh.position.set(66,35,0.2);
        scene.add(mesh);
      
      });


      loader2.load(
        '/sala/salontafel.obj',
        '/sala/salontafel.mtl',
        {side: THREE.DoubleSide}
      );

      var loader3 = new THREE.OBJMTLLoader();
      loader3.addEventListener('load', function (event) {

        var object = event.content;
        console.log(object);

        var wing2 = object.children[0];
        var wing1 = object.children[1];
           mesh = object;
        mesh.scale.set(0.1,0.1,0.1);
        mesh.rotation.x = Math.PI/2;
        mesh.position.set(71,30,3.4);
        scene.add(mesh);
      
    });


      loader3.load(
        '/sala/mini_stereo.obj',
        '/sala/mini_stereo.mtl',
        {side: THREE.DoubleSide}
      );

    var audio = new Sound( [ 'audio/Polina - Fade To Love (Extended Mix) mp3.mp3' ]);
		//audio.play();
		window.location.playSound = false;

		var prova = createMesh(new THREE.BoxGeometry(5,2,2.5),"prato.jpg");
		scene.add(prova);
		prova.position.set(71,30,4.8);
		prova.visible = false;


        var loader4 = new THREE.OBJMTLLoader();
        loader4.addEventListener('load', function (event) {

            var object = event.content;
            console.log(object);

            var wing2 = object.children[0];
            var wing1 = object.children[1];

            mesh = object;
            mesh.scale.set(2.5,2,2);
            mesh.position.set(71,56,5);
            mesh.rotation.x = Math.PI/2;
            scene.add(mesh);
      
        });


      loader4.load(
        '/sala/cheminee.obj',
        {side: THREE.DoubleSide}
      );

      var loader5 = new THREE.OBJMTLLoader();
        loader5.addEventListener('load', function (event) {

            var object = event.content;

            var wing2 = object.children[0];
            var wing1 = object.children[1];

            mesh = object;
            mesh.scale.set(0.005,0.005,0.005);
            mesh.position.set(71,59,4);
            mesh.rotation.x = Math.PI/2;
            scene.add(mesh);

      
        });


      loader5.load(
        '/sala/fre005.obj',
        '/sala/fre005.mtl',
        {side: THREE.DoubleSide}
      );

      var loader6 = new THREE.OBJMTLLoader();
        loader6.addEventListener('load', function (event) {

            var object = event.content;

            var wing2 = object.children[0];
            var wing1 = object.children[1];

            mesh = object;
            mesh.position.set(68,35,13);
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
      inter.position.set(57,58,10);
      scene.add(inter);

      var botGeometry = new THREE.BoxGeometry(0.3,0.5,0.5);
      var botMaterial = new THREE.MeshLambertMaterial({color: 0x800000});
      var bot = new THREE.Mesh(botGeometry,botMaterial);
      bot.position.set(57.2,58,10);
      scene.add(bot);


      var inter2Geometry = new THREE.BoxGeometry(0.5,1.2,1.2);
      var inter2Material = new THREE.MeshLambertMaterial({color: 0xF5DEB3});
      var inter2 = new THREE.Mesh(interGeometry,interMaterial);
      inter2.position.set(57,40,10);
      scene.add(inter2);

      var bot2Geometry = new THREE.BoxGeometry(0.3,0.5,0.5);
      var bot2Material = new THREE.MeshLambertMaterial({color: 0xF5DEB3});
      var bot2 = new THREE.Mesh(bot2Geometry,bot2Material);
      bot2.position.set(57.2,40,10);
      scene.add(bot2);

      var pointSala = new THREE.PointLight(0xffffff);
      pointSala.position.set(68,35,10);
      pointSala.castShadow = true;
      pointSala.intensity = 1;
      pointSala.shadowCameraNear = 5;
      pointSala.shadowCameraFar = 10;
      scene.add(pointSala);


      window.location.luceSalaOn = 1 ; // 0=spento
		document.addEventListener('mousedown',onDocumentMouseDown,false);
      	function onDocumentMouseDown(event) {

        event.preventDefault();
        if(!window.location.pointerLock){
            var vector = new THREE.Vector3((event.clientX / window.innerWidth)*2-1,-(event.clientY/window.innerHeight)*2+1,0.5);
            projector.unprojectVector( vector, camera );
            var raycaster = new THREE.Raycaster(camera.position,vector.sub(camera.position).normalize());
            //var intersects = raycaster.intersectObjects([object.children[0],object.children[1],object.children[2],object.children[3],object.children[4],object.children[5],object.children[6],object.children[7],object.children[8],object.children[9],object.children[10],object.children[11]]);
            var intersects = raycaster.intersectObjects([prova])
            var intersects2 = raycaster.intersectObjects([bot])
            var intersects3 = raycaster.intersectObjects([bot2])
            if(window.location.campanello){
              if ( intersects.length > 0 ) {
            	  if(window.location.playSound){
            		  audio.pause();
            		  window.location.playSound = false;
            	  }else if (!window.location.playSound){
                	 audio.play();
                	 window.location.playSound = true;
                }
              }

              if(intersects2.length > 0){
                if(!window.location.fuocoAcceso){
                    luce2(intersects2[0].object);
                    engine.initialize();
                    window.location.fuocoAcceso = true;
                }
              }

              if(intersects3.length > 0){
                luce3(intersects3[0].object);
                if(window.location.luceSalaOn === 1){
                  pointSala.intensity =0 ;
                  window.location.luceSalaOn = 0;
                }
                else if(window.location.luceSalaOn === 0 ){
                  pointSala.intensity =1;
                  window.location.luceSalaOn = 1;
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
              if ( intersects.length > 0 ) {
                if(window.location.playSound){
                  audio.pause();
                  window.location.playSound = false;
                }else if (!window.location.playSound){
                   audio.play();
                   window.location.playSound = true;
                }
              }

              if(intersects2.length > 0){
                if(!window.location.fuocoAcceso){
                    luce2(intersects2[0].object);
                    engine.initialize();
                    window.location.fuocoAcceso = true;
                }
              }

              if(intersects3.length > 0){
                luce3(intersects3[0].object);
                if(window.location.luceSalaOn === 1){
                  pointSala.intensity =0 ;
                  window.location.luceSalaOn = 0;
                }
                else if(window.location.luceSalaOn === 0 ){
                  pointSala.intensity =1;
                  window.location.luceSalaOn = 1;
                }
              }
            }
            
        }


    }
    return audio;

}