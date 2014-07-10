function makeFloor(scene){

	var pavimento = createMeshRep(new THREE.BoxGeometry(30.3,30.3,0.1),"parquet2.jpg");
    pavimento.receiveShadow = true;
    pavimento.position.set(15.3,45.6,0.25);
    scene.add(pavimento);

	var pav_cuc = createMeshRep2(new THREE.BoxGeometry(30.3,30.3,0.1),"piastrelle4.jpg",12);
    scene.add(pav_cuc);
    pav_cuc.position.set(15.15,15.15,0.3);

    var planeMatr = createMeshRep(new THREE.BoxGeometry(30.3,55,0.1),"parquet2.jpg");
    scene.add(planeMatr);
    planeMatr.position.set(15.2,82,0.2);

    var pav_bagno = createMeshRep2(new THREE.BoxGeometry(26.3,26.2,0.1),"piastrelle_bagno.jpg",10);
    pav_bagno.receiveShadow = true;
    pav_bagno.position.set(43.8,96,0.2);
    scene.add(pav_bagno);

    //prima parte pavimento bagno
    var planePier = createMeshRep2(new THREE.BoxGeometry(28.3,27,0.2),"parquet2.jpg",4);
    scene.add(planePier);
    planePier.position.set(70.8,95.5,0.25);

    //pavimento bagno+sala+ingresso
    var planeTot = createMeshRep2(new THREE.BoxGeometry(54.6,83,0.2),"parquet2.jpg",8);
    scene.add(planeTot);
    planeTot.position.set(57.7,41.5,0.25);


    var balcone = createMeshRep2(new THREE.BoxGeometry(24.35,30,0.1),"balcone.jpg",10);
    balcone.receiveShadow = true;
    balcone.position.set(97.3,15.3,0.25);
    scene.add(balcone);

}