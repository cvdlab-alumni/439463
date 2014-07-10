function makeGiardino(scene){
	
	var loader = new THREE.OBJMTLLoader();
      loader.addEventListener('load', function (event) {

        var object = event.content;

        var wing2 = object.children[0];
        var wing1 = object.children[1];

        mesh = object;
        mesh.rotation.x = Math.PI/2;
        mesh.scale.set(2,2,2);
        mesh.position.set(-7,-7,0)
        scene.add(mesh);
      
      });


      loader.load(
        '/giardino/palm.obj',
        '/giardino/palm.mtl',
        {side: THREE.DoubleSide}
      );

}