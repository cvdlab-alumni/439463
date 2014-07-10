function createMeshRep2(geom, imageFile,rep) {
        var texture = THREE.ImageUtils.loadTexture("assets/textures/general/" + imageFile)
        texture.wrapS = THREE.RepeatWrapping;
        texture.wrapT = THREE.RepeatWrapping;
        texture.repeat.x = rep;
        texture.repeat.y = rep;
        var mat = new THREE.MeshLambertMaterial();
        mat.map = texture;
        mat.side = THREE.DoubleSide;
        var mesh = new THREE.Mesh(geom, mat);
        return mesh;
      }

      function createMeshRep(geom, imageFile) {
        var texture = THREE.ImageUtils.loadTexture("assets/textures/general/" + imageFile)
        texture.wrapS = THREE.RepeatWrapping;
        texture.wrapT = THREE.RepeatWrapping;
        texture.repeat.x = 4;
        texture.repeat.y = 4;
        var mat = new THREE.MeshLambertMaterial();
        mat.map = texture;
        mat.side = THREE.DoubleSide;
        var mesh = new THREE.Mesh(geom, mat);
        return mesh;
      }

      function createMesh(geom, imageFile) {
        var texture = THREE.ImageUtils.loadTexture("assets/textures/general/" + imageFile)
        var mat = new THREE.MeshLambertMaterial();
        mat.map = texture;
        mat.side = THREE.DoubleSide;
        var mesh = new THREE.Mesh(geom, mat);
        return mesh;
      }

      function apri(obj){
         var prova = new TWEEN.Tween(obj.rotation)
          .to({z: Math.PI/2}, 2000)
          .start();
      }

      function chiudi(obj){
         var prova = new TWEEN.Tween(obj.rotation)
          .to({z: 0}, 2000)
          .start();
      }

      function apri2(obj){
         var prova = new TWEEN.Tween(obj.rotation)
          .to({z: -Math.PI/2}, 2000)
          .start();
      }

      function apri3(obj){
         var prova = new TWEEN.Tween(obj.rotation)
          .to({z: Math.PI/2}, 2000)
          .delay(1000)
          .start();
      }

      function spostaSedia(obj){
          var sposta = new TWEEN.Tween(obj.position)
          .to({x:101,y:130,z:12},1500)
          .easing(TWEEN.Easing.Bounce.Out)
          .start();
      }
      function luce(obj){
          var rilascia = new TWEEN.Tween(obj.position)
          .to({x:57.2,y:90,z:10},200)
          .start();

          var premi = new TWEEN.Tween(obj.position)
          .to({x:57,y:90,z:10},200)
          .chain(rilascia)
          .start();
      }

//pulsante camino
      function luce2(obj){
          var rilascia = new TWEEN.Tween(obj.position)
          .to({x:57.2,y:58,z:10},200)
          .start();

          var premi = new TWEEN.Tween(obj.position)
          .to({x:57,y:58,z:10},200)
          .chain(rilascia)
          .start();
      }

      function luce3(obj){
          var rilascia = new TWEEN.Tween(obj.position)
          .to({x:57.2,y:40,z:10},200)
          .start();

          var premi = new TWEEN.Tween(obj.position)
          .to({x:57,y:40,z:10},200)
          .chain(rilascia)
          .start();
      }

      function luce4(obj){
          var rilascia = new TWEEN.Tween(obj.position)
          .to({x:29.8,y:58,z:10},200)
          .start();

          var premi = new TWEEN.Tween(obj.position)
          .to({x:30,y:58,z:10},200)
          .chain(rilascia)
          .start();
      }


      function luce5(obj){
          var rilascia = new TWEEN.Tween(obj.position)
          .to({x:29.8,y:8,z:10},200)
          .start();

          var premi = new TWEEN.Tween(obj.position)
          .to({x:30,y:8,z:10},200)
          .chain(rilascia)
          .start();
      }

      function luce6(obj){
          var rilascia = new TWEEN.Tween(obj.position)
          .to({x:29.8,y:80,z:10},200)
          .start();

          var premi = new TWEEN.Tween(obj.position)
          .to({x:30,y:80,z:10},200)
          .chain(rilascia)
          .start();
      }

      function luce7(obj){
          var rilascia = new TWEEN.Tween(obj.position)
          .to({x:31,y:95,z:10},200)
          .start();

          var premi = new TWEEN.Tween(obj.position)
          .to({x:30.8,y:95,z:10},200)
          .chain(rilascia)
          .start();
      }



      //aspirapolvere
      function aspira(obj){

        var aspira2 = new TWEEN.Tween(obj.position)
        .to({x:45,y:30,z:1.5});

        var aspira =  new TWEEN.Tween(obj.position)
        .to({x:45,y:40,z:1.5},2000)
        .easing(TWEEN.Easing.Linear.None)
        .chain(aspira2)
        .start();

        audio2.pause();
      }

       var Sound = function ( sources) {
        var audio = document.createElement( 'audio' );
        for ( var i = 0; i < sources.length; i ++ ) {
            var source = document.createElement( 'source' );
            source.src = sources[ i ];
            audio.appendChild( source );
        }
        this.play = function () {
          audio.play();
          audio.volume = 1
        }
        this.pause = function() {
            audio.pause();
        }
        this.stop = function() {
            audio.pause();
            audio.currentTime = 0;
        }

    }

 
      