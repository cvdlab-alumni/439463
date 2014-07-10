function makeCarpet(scene){

	//tappeto
      var tappeto = createMesh(new THREE.BoxGeometry(20,20,0.1),"tappeto.jpg");
      tappeto.position.set(15,45,0.3);
      //tappeto.castShadow = true;
      tappeto.receiveShadow = true;
      scene.add(tappeto);

      //tappeto camera matrimoniale
      var tappeto_matr = createMesh(new THREE.BoxGeometry(25,21,0.1),"tappeto2.jpg");
      scene.add(tappeto_matr);
      tappeto_matr.position.set(15,85,0.3);

      //carpet
      var carpet = createMesh(new THREE.BoxGeometry(12,12,0.2),"carpet.jpg");
      carpet.position.set(45,97,0.35);
      //tappeto.castShadow = true;
      carpet.receiveShadow = true;
      scene.add(carpet);

}