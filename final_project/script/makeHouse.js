function makeHouse(scene){

var loader = new THREE.OBJLoader();
      loader.load('casaprova.obj', function (obj) {

        global_o = obj;

        var material = new THREE.MeshLambertMaterial({color: 0xaaaaaa});
        material.side = THREE.DoubleSide;
        obj.children[0].material = material;
        mesh = obj.children[0];

        var multiMaterial = [
          new THREE.MeshLambertMaterial({color: 0xaaaaaa, side: THREE.DoubleSide, shading: THREE.FlatShading}),
          new THREE.MeshLambertMaterial({wireframe: false, overdraw: true, color: 0xffffff, side: THREE.DoubleSide})
          ];

        mesh = THREE.SceneUtils.createMultiMaterialObject(obj.children[0].geometry, multiMaterial);  
        scene.add(mesh);
      });


      //definizione del piano cui si trova la casa      
      var plane = createMesh(new THREE.PlaneGeometry(200,200,200,200), "prato.jpg");
      scene.add(plane);
      plane.position.set(50,50,0); 
           
      scene.add(plane);
}