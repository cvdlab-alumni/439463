function makeInterruttore(scene,x,y,z){
	var interGeometry = new THREE.BoxGeometry(0.3,1.2,1.2);
	var interMaterial = new THREE.MeshLambertMaterial({color: 0xF5DEB3});
	var inter = new THREE.Mesh(interGeometry,interMaterial);
	inter.position.set(x,y,z);
	scene.add(inter);

	var botGeometry = new THREE.BoxGeometry(0.3,0.5,0.5);
	var botMaterial = new THREE.MeshLambertMaterial({color: 0xF0E68C});
	var bot = new THREE.Mesh(botGeometry,botMaterial);
	bot.position.set(x+0.15,y,z);
	scene.add(bot);

}