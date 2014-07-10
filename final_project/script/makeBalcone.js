function makeBalcone(scene){
	var loader = new THREE.OBJMTLLoader();
     loader.addEventListener('load', function (event) {

        var object = event.content;

        var wing2 = object.children[0];
        var wing1 = object.children[1];

        mesh = object;
        mesh2 = mesh.clone();
        mesh.rotation.x = Math.PI/2;
        mesh.position.set(100,22,3.5);
        scene.add(mesh);

        mesh2.rotation.x = Math.PI/2;
        mesh2.rotation.y = Math.PI;
        mesh2.position.set(100,5,3.5);
       	scene.add(mesh2);
      
    });


    loader.load(
    	'/balcone/blackDeckChair.obj',
        '/balcone/blackDeckChair.mtl',
        {side: THREE.DoubleSide}
    );


    var loader2 = new THREE.OBJMTLLoader();
     loader2.addEventListener('load', function (event) {

        var object = event.content;

        var wing2 = object.children[0];
        var wing1 = object.children[1];

        mesh = object;
        mesh.rotation.x = Math.PI/2;
        mesh.position.set(98,20.5,3.5);
        scene.add(mesh);

        
      
    });


    loader2.load(
    	'/balcone/blackDeckTable.obj',
        '/balcone/blackDeckTable.mtl',
        {side: THREE.DoubleSide}
    );

    var loader3 = new THREE.OBJMTLLoader();
    loader3.addEventListener('load', function (event) {

        var object = event.content;

        var wing2 = object.children[0];
        var wing1 = object.children[1];

        mesh = object;
        mesh.rotation.x = Math.PI/2;
        mesh.position.set(111.5,28,6);
        mesh.scale.set(0.08,0.08,0.08);
        scene.add(mesh);

        
      
    });


    loader3.load(
    	'/balcone/potplant2.obj',
        '/balcone/potplant2.mtl',
        {side: THREE.DoubleSide}
    );

}