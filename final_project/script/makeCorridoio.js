function makeCorridoio(scene){

    audio2 = new Sound( [ 'audio/aspir.mp3' ]);
        //audio.play();
        window.location.playSound = false;

    var loader6 = new THREE.OBJMTLLoader();
    loader6.addEventListener('load', function (event) {

        var object = event.content;

        var wing2 = object.children[0];
        var wing1 = object.children[1];

        var aspirGeometry = new THREE.BoxGeometry(3,4,3);
        var aspirMaterial = new THREE.MeshLambertMaterial({color: 0xF5DEB3});
        var aspir = new THREE.Mesh(aspirGeometry,aspirMaterial);
        aspir.position.set(45,20,1.5);
        aspir.visible = false;
        scene.add(aspir);

        mesh = object;
        mesh.scale.set(0.1,0.1,0.1);
        mesh.rotation.x = Math.PI/2;
        mesh.rotation.y = -Math.PI/2;
        aspir.add(mesh);


        document.addEventListener('mousedown',onDocumentMouseDown,false);
        function onDocumentMouseDown(event) {

        event.preventDefault();
        if(!window.location.pointerLock){
            var vector = new THREE.Vector3((event.clientX / window.innerWidth)*2-1,-(event.clientY/window.innerHeight)*2+1,0.5);
            projector.unprojectVector( vector, camera );
            var raycaster = new THREE.Raycaster(camera.position,vector.sub(camera.position).normalize());
            var intersects = raycaster.intersectObjects([aspir]);
            if(window.location.campanello){
                if ( intersects.length > 0 ) {
                   if(!window.location.audioOn){
                       aspira(intersects[0].object);
                       audio2.play();
                       window.location.audioOn = true;
                    }else{
                       audio2.pause();
                       window.location.audioOn = false;
                    }
                }
            }
            
        }
        else{
            event.preventDefault();
            var vector2 = new THREE.Vector3(10,10,10);
            projector.unprojectVector( vector2, camera );
            var raycaster = new THREE.Raycaster(vector2,controls.getDirection(new THREE.Vector3(0, 0, 0)).clone());
            var intersects = raycaster.intersectObjects([aspir]);

           if(window.location.campanello){
                if ( intersects.length > 0 ) {
                   if(!window.location.audioOn){
                       aspira(intersects[0].object);
                       audio2.play();
                       window.location.audioOn = true;
                    }else{
                       audio2.pause();
                       window.location.audioOn = false;
                    }
                }
            }
        }


    }
      
    });


    loader6.load(
        '/sala/aspirateur.obj',
        '/sala/aspirateur.mtl',
        {side: THREE.DoubleSide}
    );


      var loader = new THREE.OBJMTLLoader();
      loader.addEventListener('load', function (event) {

        var object = event.content;
        var wing2 = object.children[0];
        var wing1 = object.children[1];

        mesh = object;
        mesh.rotation.x = Math.PI/2;
        mesh.rotation.y = Math.PI/2;
        mesh.scale.set(0.07,0.07,0.07)
        mesh.position.set(34,35,0)

        scene.add(mesh);
      
      });

      loader.load(
        '/corridoio/table_wood_and_iron.obj',
        '/corridoio/table_wood_and_iron.mtl',
        {side: THREE.DoubleSide}
      );

      var audioTel = new Sound( [ 'audio/telefono.wav' ]);

      var loader = new THREE.OBJMTLLoader();
      loader.addEventListener('load', function (event) {

        console.log(object)
        var object = event.content;
        var wing2 = object.children[0];
        var wing1 = object.children[1];

        mesh = object;
        mesh.scale.set(0.1,0.1,0.1)
        mesh.position.set(34,35,4)

        scene.add(mesh);
      
      });

      loader.load(
        '/corridoio/iphone.obj',
        '/corridoio/iphone.mtl',
        {side: THREE.DoubleSide}
      );


    var telGeometry = new THREE.BoxGeometry(1,1,1);
    var telMaterial = new THREE.MeshLambertMaterial({color: 0xF5DEB3});
    var tel = new THREE.Mesh(telGeometry,telMaterial);
    tel.position.set(34,35.5,4);
    tel.visible = false;
    scene.add(tel);

    document.addEventListener('mousedown',onDocumentMouseDown,false);
        function onDocumentMouseDown(event) {

        event.preventDefault();
        if(!window.location.pointerLock){
            var vector = new THREE.Vector3((event.clientX / window.innerWidth)*2-1,-(event.clientY/window.innerHeight)*2+1,0.5);
            projector.unprojectVector( vector, camera );
            var raycaster = new THREE.Raycaster(camera.position,vector.sub(camera.position).normalize());
            var intersects = raycaster.intersectObjects([tel]);
            if(window.location.campanello){
                if ( intersects.length > 0 ) 
                       audioTel.play();
            }
        }
        else{
            event.preventDefault();
            var vector2 = new THREE.Vector3(10,10,10);
            projector.unprojectVector( vector2, camera );
            var raycaster = new THREE.Raycaster(vector2,controls.getDirection(new THREE.Vector3(0, 0, 0)).clone());
            var intersects = raycaster.intersectObjects([tel]);

            if(window.location.campanello){
                if ( intersects.length > 0 ) 
                       audioTel.play();
                    
                }
            }
        }

}