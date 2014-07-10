function makeRoof(scene){
	var roof  = createMeshRep2(new THREE.BoxGeometry(85,110,0.4),"roof.jpg",2);
	scene.add(roof);
	roof.position.set(42.5,55,20.4);

	return roof;

}