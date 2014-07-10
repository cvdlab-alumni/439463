 document.addEventListener('mousedown',onDocumentMouseDown,false);
      function onDocumentMouseDown( event ) {

        event.preventDefault();
        var vector2 = new THREE.Vector3(10,10,10);
        projector.unprojectVector( vector2, camera );
        var obj = [door]
        //var obj = [door,fin,door_cuc,fin2_cuc,door_matr]
        //var obj1 = [fin2,fin_cuc]
        var raycaster = new THREE.Raycaster(vector2,window.location.controls.getDirection(new THREE.Vector3(0, 0, 0)).clone());
        var intersects = raycaster.intersectObjects(obj);
        var intersects1 = raycaster.intersectObjects(obj1);

        if ( intersects.length > 0 ) {
          console.log(intersects[0].object);
          prova(intersects[0].object.parent);
          //intersects[0].object.parent.rotation.z = Math.PI/2;
        }
        /*
        if ( intersects1.length > 0 ) {
          intersects1[0].object.parent.rotation.z = -Math.PI/2;
        }*/


      }
      
      window.addEventListener( 'resize', onWindowResize, false );

      function onWindowResize() {
        camera.aspect = window.innerWidth / window.innerHeight;
        camera.updateProjectionMatrix();
        renderer.setSize( window.innerWidth, window.innerHeight );
      }
