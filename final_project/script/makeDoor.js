function makeDoor(scene){

	//camera valentina
	var door  = createMesh(new THREE.BoxGeometry(8,0.2,14),"door.jpg");
    //scene.add(door);
    door.rotation.z = Math.PI/2;
    door.position.set(0,4,7);

    var pernoporta = new THREE.Object3D();
    pernoporta.add(door);
    pernoporta.position.set(30.5,41.6,0);
    scene.add(pernoporta);
    door.aperta = false;
    
	//cucina
	var door_cuc  = createMesh(new THREE.BoxGeometry(8,0.2,14),"door.jpg");
    //scene.add(door);
    door_cuc.rotation.z = Math.PI/2;
    door_cuc.position.set(0,4,7);
    door_cuc.aperta = false;

    var pernoporta_cuc = new THREE.Object3D();
    pernoporta_cuc.add(door_cuc);
    pernoporta_cuc.position.set(30.5,11.3,0);
    scene.add(pernoporta_cuc);

	//camera matrimoniale
	var door_matr  = createMesh(new THREE.BoxGeometry(6,0.2,14),"door.jpg");
    door_matr.rotation.z = Math.PI/2;
    door_matr.position.set(0,3,7);
    door_matr.aperta = false;

    var pernoporta_matr = new THREE.Object3D();
    pernoporta_matr.add(door_matr);
    pernoporta_matr.position.set(30.5,68.8,0);
    scene.add(pernoporta_matr);

	//bagno
	var door_bag  = createMesh(new THREE.BoxGeometry(6.5,0.2,14),"door.jpg");
    door_bag.position.set(3.25,0,7);
    door_bag.aperta = false;

    var pernoporta_bag = new THREE.Object3D();
    pernoporta_bag.add(door_bag);
    pernoporta_bag.position.set(40.4,83,0.2);
    scene.add(pernoporta_bag);

    //porta pier
    var door_pier  = createMesh(new THREE.BoxGeometry(6,0.2,14),"door.jpg");
    door_pier.position.set(0,3,7);
    door_pier.rotation.z = Math.PI/2;
    door_pier.aperta = false;

    var pernoporta_pier = new THREE.Object3D();
    pernoporta_pier.add(door_pier);
    pernoporta_pier.position.set(56.6,69,0.2);
    scene.add(pernoporta_pier);

    //salotto
    var door_salotto  = createMesh(new THREE.BoxGeometry(8,0.2,14),"door.jpg");
    door_salotto.position.set(0,4,7);
    door_salotto.rotation.z = Math.PI/2;
    door_salotto.aperta = false;

    var pernoporta_salotto = new THREE.Object3D();
    //var pernoporta_salotto = createMesh(new THREE.BoxGeometry(1,1,1),"door.jpg");
    pernoporta_salotto.add(door_salotto);
    pernoporta_salotto.position.set(57.1,11.3,0.2);
    scene.add(pernoporta_salotto);

    //balcone
    var door_balcone  = createMesh(new THREE.BoxGeometry(7.5,0.2,14),"door.jpg");
    door_balcone.position.set(0,3.75,7);
    door_balcone.rotation.z = Math.PI/2;
    door_balcone.aperta = false;

    var door_balcone2  = createMesh(new THREE.BoxGeometry(7.5,0.2,14),"door2.jpg");
    door_balcone2.position.set(0,-3.75,7);
    door_balcone2.rotation.z = Math.PI/2;
    door_balcone2.aperta = false;

    //var pernoporta_balcone = new THREE.Object3D();
    var pernoporta_balcone = new THREE.Object3D();
    pernoporta_balcone.add(door_balcone);
    pernoporta_balcone.position.set(85,7.85,0.2);
    scene.add(pernoporta_balcone);

    var pernoporta2_balcone = new THREE.Object3D();
    pernoporta2_balcone.add(door_balcone2);
    pernoporta2_balcone.position.set(85,22.9,0.2);
    scene.add(pernoporta2_balcone);

    //portone
    var door_portone = createMesh(new THREE.BoxGeometry(6.42,0.2,14),"door.jpg");
    door_portone.position.set(3.21,0,7);
    door_portone.aperta = false;

    var door_portone2  = createMesh(new THREE.BoxGeometry(6.42,0.2,14),"door2.jpg");
    door_portone2.position.set(-3.21,0,7);
    door_portone2.aperta = false;

    //var pernoporta_balcone = new THREE.Object3D();
    var pernoporta_portone = new THREE.Object3D();
    pernoporta_portone.add(door_portone);
    pernoporta_portone.position.set(37.1,0,0.3);
    scene.add(pernoporta_portone);

    var pernoporta2_portone = new THREE.Object3D();
    pernoporta2_portone.add(door_portone2);
    pernoporta2_portone.position.set(50.1,0,0.3);
    scene.add(pernoporta2_portone);




    var interGeometry = new THREE.BoxGeometry(0.5,1.2,1.2);
    var interMaterial = new THREE.MeshLambertMaterial({color: 0xF5DEB3});
    var inter = new THREE.Mesh(interGeometry,interMaterial);
    inter.position.set(32,0,10);
    inter.rotation.x = Math.PI/2;
    inter.rotation.y = Math.PI/2;
    scene.add(inter);

    var botGeometry = new THREE.BoxGeometry(0.3,0.5,0.5);
    var botMaterial = new THREE.MeshLambertMaterial({color: 0x2F2F2F});
    var bot = new THREE.Mesh(botGeometry,botMaterial);
    bot.position.set(32,-0.2,10);
    bot.rotation.y = Math.PI/2;
    bot.rotation.x = Math.PI/2;
    scene.add(bot);


    window.location.campanello = false;
    var audio = new Sound( [ 'audio/campanello.mp3' ]);
    //audio.play();
    window.location.playSound = false;

    var audio2 = new Sound( [ 'audio/door.mp3' ]);
    //audio.play();

    document.addEventListener('mousedown',onDocumentMouseDown,false);
      function onDocumentMouseDown(event) {

        event.preventDefault();
        if(!window.location.pointerLock){
            var vector = new THREE.Vector3((event.clientX / window.innerWidth)*2-1,-(event.clientY/window.innerHeight)*2+1,0.5);
            projector.unprojectVector( vector, camera );
            var raycaster = new THREE.Raycaster(camera.position,vector.sub(camera.position).normalize());
            var intersects = raycaster.intersectObjects([door,door_cuc,door_matr,door_bag,door_balcone,door_portone]);
            var intersects2 = raycaster.intersectObjects([door_pier,door_salotto,door_balcone2,door_portone2])
            var intersects3 = raycaster.intersectObjects([bot])
            //var intersects4 = raycaster.intersectObjects([door_portone])
            var intersects5 = raycaster.intersectObjects([door_portone2,door_portone])

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
            else{
                if(intersects5.length>0){
                    audio2.play();
                }

            }

            if(intersects3.length > 0){
                    audio.play();
                    window.location.campanello = true;
                    apri3(door_portone.parent);
                    door_portone.aperta = true;

            }
            
            
        }
        else{
            event.preventDefault();
            var vector2 = new THREE.Vector3(10,10,10);
            projector.unprojectVector( vector2, camera );
            var raycaster = new THREE.Raycaster(vector2,controls.getDirection(new THREE.Vector3(0, 0, 0)).clone());
            var intersects = raycaster.intersectObjects([door,door_cuc,door_matr,door_bag,door_balcone,door_portone]);
            var intersects2 = raycaster.intersectObjects([door_pier,door_salotto,door_balcone2,door_portone2])
            var intersects3 = raycaster.intersectObjects([bot])
            var intersects5 = raycaster.intersectObjects([door_portone2,door_portone])
            
            

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
            else{
                if(intersects5.length>0){
                    audio2.play();
                }

            }

            if(intersects3.length > 0){
                    audio.play();
                    window.location.campanello = true;
                    apri3(door_portone.parent);
                    door_portone.aperta = true;

                }
            
        }


    }

    return audio;
    
}