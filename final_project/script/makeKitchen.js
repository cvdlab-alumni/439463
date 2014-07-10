function makeKitchen(scene){

      var loader3 = new THREE.OBJLoader();
      loader3.load('/cucina/frigo.obj', function (obj) {

        global_o = obj;

        var material = new THREE.MeshLambertMaterial({color: 0xaaaaaa});
        material.side = THREE.DoubleSide;
        obj.children[0].material = material;
        mesh3 = obj.children[0];

        var multiMaterial = [
          new THREE.MeshLambertMaterial({color: 0xaaaaaa, side: THREE.DoubleSide, shading: THREE.FlatShading}),
          new THREE.MeshLambertMaterial({wireframe: false, overdraw: true, color: 0xffffff, side: THREE.DoubleSide})
          ];

        mesh3 = THREE.SceneUtils.createMultiMaterialObject(obj.children[0].geometry, multiMaterial);
        scene.add(mesh3);
        mesh3.rotation.x = Math.PI/2;
        mesh3.scale.set(.005,.005,.005);
        mesh3.position.set(5,28,0);
        
      });

      var loaderprova = new THREE.OBJMTLLoader();
      loaderprova.addEventListener('load', function (event) {

        var object = event.content;

        var wing2 = object.children[0];
        var wing1 = object.children[1];

        object.scale.set(10,10,10);
        mesh = object;
        scene.add(mesh);

        object.rotation.x = Math.PI/2;
        object.scale.set(7,7,7);
        object.position.set(12,17,0);

        var object2 = object.clone();
        scene.add(object2);
        object2.position.set(17,17,0);

        var object3 = object.clone();
        scene.add(object3);
        object3.rotation.y =Math.PI;
        object3.position.set(12,6,0);

        var object4 = object.clone();
        scene.add(object4);
        object4.rotation.y =Math.PI;
        object4.position.set(17,6,0);
      });


      loaderprova.load(
        '/cucina/chair.obj', 
        '/cucina/chair.mtl', 
        {side: THREE.DoubleSide}
      );

      var loaderprova = new THREE.OBJMTLLoader();
      loaderprova.addEventListener('load', function (event) {

        var object = event.content;

        var wing2 = object.children[0];
        var wing1 = object.children[1];

        mesh = object;
        mesh.rotation.x = Math.PI/2;
        mesh.scale.set(0.1,0.1,0.1);
        mesh.position.set(9,30.2,7.3);
        scene.add(mesh);

      });

      loaderprova.load(
        '/cucina/mano_cooktop.obj', 
        '/cucina/mano_cooktop.mtl', 
        {side: THREE.DoubleSide}
      );

      var loaderprova = new THREE.OBJMTLLoader();
      loaderprova.addEventListener('load', function (event) {

        var object = event.content;

        var wing2 = object.children[0];
        var wing1 = object.children[1];

        mesh = object;
        mesh.scale.set(0.1,0.1,0.1)
        mesh.rotation.x = Math.PI/2;
        mesh.position.set(26,24,1.7);
        scene.add(mesh);

      });

      loaderprova.load(
        '/cucina/boiler.obj', 
        '/cucina/boiler.mtl', 
        {side: THREE.DoubleSide}
      );

      var loaderprova = new THREE.OBJMTLLoader();
      loaderprova.addEventListener('load', function (event) {

        var object = event.content;

        var wing2 = object.children[0];
        var wing1 = object.children[1];

        mesh = object;
        mesh.rotation.x = Math.PI/2;
        mesh.scale.set(2,2,1.8);
        mesh.position.set(20,27,4);
        scene.add(mesh);

      });

      loaderprova.load(
        '/cucina/kitchenSinkWithMarble.obj', 
        '/cucina/kitchenSinkWithMarble.mtl', 
        {side: THREE.DoubleSide}
      );


      var cubGeometry = new THREE.BoxGeometry(2,2,2);
      var cubMaterial = new THREE.MeshLambertMaterial({color: 0xF5DEB3});
      var cub = new THREE.Mesh(cubGeometry,cubMaterial);
      cub.position.set(13,27,8);
      cub.visible = false;
      scene.add(cub);


      //mobili e fornelli
      var mob = createMesh(new THREE.BoxGeometry(6,6,7),"mobilecucina.jpg");
      scene.add(mob);
      mob.position.set(12,27.5,3.8);

      var sportello = createMesh(new THREE.PlaneGeometry(5,7),"furniture.jpg");
      sportello.rotation.x = Math.PI/2;
      mob.add(sportello);
      sportello.position.set(0,-3.05,0);


      // tavolino
      var g1 = createMesh(new THREE.CylinderGeometry(0.5,0.5,6,8,8),"wood-2.jpg");
      scene.add(g1);
      g1.rotation.x = Math.PI/2;
      g1.position.set(9,9,3.3);

      var g2 = g1.clone();
      scene.add(g2);
      g2.position.set(19,9,3.3);

      var g3 = g1.clone();
      scene.add(g3);
      g3.position.set(19,16,3.3);

      var g4 = g1.clone();
      scene.add(g4);
      g4.position.set(9,16,3.3);

      var tav = createMesh(new THREE.BoxGeometry(12,9,1),"wood-2.jpg");
      scene.add(tav);
      //tav.rotation.z = Math.PI/2;
      tav.position.set(14,12.5,6.3);

      var quadro_cuc = createMesh(new THREE.PlaneGeometry(13,5),"cornice4.jpg");
      scene.add(quadro_cuc);
      quadro_cuc.rotation.x = Math.PI/2;
      quadro_cuc.position.set(17,29,14);

      //mobiletto tv
      var mobiletto = createMesh(new THREE.BoxGeometry(5,6,5),"mobilecucina.jpg");
      scene.add(mobiletto);
      mobiletto.position.set(3,3.4,3);

      // create the video element
      video = document.createElement( 'video' );
      // video.id = 'video';
      // video.type = ' video/ogg; codecs="theora, vorbis" ';
      video.src = "assets/textures/Unti e Bisunti - promo.avi";
      video.load(); // must call after setting/changing source
      video.play();
  
      videoImage = document.createElement( 'canvas' );
      //videoImage.width = 480;
      //videoImage.height = 204;

      videoImage.width = 1000;
      videoImage.height = 500;

      videoImageContext = videoImage.getContext( '2d' );
      // background color if no video present
      videoImageContext.fillStyle = '#000000';
      videoImageContext.fillRect( 0, 0, videoImage.width, videoImage.height );

      videoTexture = new THREE.Texture( videoImage );
      videoTexture.minFilter = THREE.LinearFilter;
      videoTexture.magFilter = THREE.LinearFilter;
  
      var movieMaterial = new THREE.MeshBasicMaterial( { map: videoTexture, overdraw: true, side:THREE.DoubleSide } );
      // the geometry on which the movie will be displayed;
      //    movie image will be scaled to fit these dimensions.
      var movieGeometry = new THREE.PlaneGeometry( 6.4, 3.5, 4, 4 );
      var movieScreen = new THREE.Mesh( movieGeometry, movieMaterial );
      movieScreen.rotation.x = Math.PI/2;
      movieScreen.rotation.y = 2*Math.PI/3;
      //movieScreen.position.set(3.8,4.4,9); //il primo avvicina lo schermo alla tv
      movieScreen.position.set(3.45,4.17,8.9);
      scene.add(movieScreen);
      movieScreen.visible = false;
      
      video.pause();

      var toreturn = [video,movieScreen]


       var loader = new THREE.OBJMTLLoader();
      loader.addEventListener('load', function (event) {

        var object = event.content;

        var wing2 = object.children[0];
        var wing1 = object.children[1];

        
        mesh = object;
        scene.add(mesh);
        mesh.scale.set(0.1,0.1,0.1);

        object.rotation.x = Math.PI/2; 
        object.position.set(14,12.5,7);

      });


      loader.load(
        '/cucina/apples.obj', 
        '/cucina/apples.mtl', 
        {side: THREE.DoubleSide}
      );

      var audioT = new Sound( [ 'audio/teiera.wav' ]);
    //audio.play();



      var loader6 = new THREE.OBJMTLLoader();
        loader6.addEventListener('load', function (event) {

            var object = event.content;

            var wing2 = object.children[0];
            var wing1 = object.children[1];

            mesh = object;
            mesh.position.set(15,15,13);
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
      inter.position.set(30,8,10);
      scene.add(inter);

      var botGeometry = new THREE.BoxGeometry(0.3,0.5,0.5);
      var botMaterial = new THREE.MeshLambertMaterial({color: 0xF5DEB3});
      var bot = new THREE.Mesh(botGeometry,botMaterial);
      bot.position.set(29.8,8,10);
      scene.add(bot);

      window.location.luceCucinaOn = 1 ; // 0=spento
      var pointCucina= new THREE.PointLight(0xffffff);
      pointCucina.position.set(15,15,13);
      pointCucina.castShadow = true;
      pointCucina.intensity = 0.5;
      pointCucina.shadowCameraNear = 10;
      pointCucina.shadowCameraFar = 200;
      scene.add(pointCucina);



      document.addEventListener('mousedown',onDocumentMouseDown,false);
        function onDocumentMouseDown(event) {

        event.preventDefault();
        if(!window.location.pointerLock){
            var vector = new THREE.Vector3((event.clientX / window.innerWidth)*2-1,-(event.clientY/window.innerHeight)*2+1,0.5);
            projector.unprojectVector( vector, camera );
            var raycaster = new THREE.Raycaster(camera.position,vector.sub(camera.position).normalize());
            var intersects = raycaster.intersectObjects([cub]);
            var intersects2 = raycaster.intersectObjects([bot])
            console.log(intersects);
            if(window.location.campanello){
                if ( intersects.length > 0 ) {
                  if(!window.location.fornelloAcceso){
                    window.location.fornelloAcceso = true;
                    engine2.initialize();
                    setTimeout(audioT.play(),10000);

                  }
                  else{
                    window.location.fornelloAcceso = false;
                  }
               }
               if(intersects2.length > 0){
                luce5(intersects2[0].object);
                if(window.location.luceCucinaOn === 1){
                  pointCucina.intensity =0 ;
                  window.location.luceCucinaOn = 0;
                }
                else if(window.location.luceCucinaOn === 0 ){
                  pointCucina.intensity =0.5;
                  window.location.luceCucinaOn = 1;
                }
              }
            }
            
        }
        else{
            event.preventDefault();
            var vector2 = new THREE.Vector3(10,10,10);
            projector.unprojectVector( vector2, camera );
            var raycaster = new THREE.Raycaster(vector2,controls.getDirection(new THREE.Vector3(0, 0, 0)).clone());
            var intersects = raycaster.intersectObjects([cub]);
            var intersects2 = raycaster.intersectObjects([bot])
            if(window.location.campanello){
                if ( intersects.length > 0 ) {
                  if(!window.location.fornelloAcceso){
                    window.location.fornelloAcceso = true;
                    engine2.initialize();
                    setTimeout(audioT.play(),10000);

                  }
                  else{
                    window.location.fornelloAcceso = false;
                  }
               }
               if(intersects2.length > 0){
                luce5(intersects2[0].object);
                if(window.location.luceCucinaOn === 1){
                  pointCucina.intensity =0 ;
                  window.location.luceCucinaOn = 0;
                }
                else if(window.location.luceCucinaOn === 0 ){
                  pointCucina.intensity =0.5;
                  window.location.luceCucinaOn = 1;
                }
              }
            }
           
        }

      }


      return toreturn;

}
