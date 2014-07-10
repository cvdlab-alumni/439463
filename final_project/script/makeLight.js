function makeLight(scene){

	var spotLightAll = new THREE.SpotLight(0xffffff);
      spotLightAll.position.set(-50, 120, 60);
      spotLightAll.castShadow = true;
      spotLightAll.intensity = 1;
      spotLightAll.shadowCameraNear = 10;
      spotLightAll.shadowCameraFar = 200;
      scene.add(spotLightAll);

      //luce davanti
      var spotLightAll2 = new THREE.SpotLight(0xffffff);
      spotLightAll2.position.set(150, -60, 5);
      spotLightAll2.castShadow = true;
      spotLightAll2.intensity = 1;
      spotLightAll2.shadowCameraNear = 10;
      spotLightAll2.shadowCameraFar = 200;
      scene.add(spotLightAll2);

      //luce sx
      var spotLightAll3 = new THREE.SpotLight(0xffffff);
      spotLightAll3.position.set(150, 60, 60);
      spotLightAll3.castShadow = true;
      spotLightAll3.intensity = 1;
      spotLightAll3.shadowCameraNear = 10;
      spotLightAll3.shadowCameraFar = 200;
      scene.add(spotLightAll3);

      var luceCucina = new THREE.SpotLight(0xffffff);
      luceCucina.position.set(25, -200, 10);
      luceCucina.castShadow = true;
      luceCucina.intensity = 1;
      luceCucina.shadowCameraNear = 10;
      luceCucina.shadowCameraFar = 200;
      //luceCucina.target = tav;
      //scene.add(luceCucina);

      var luceBagno = new THREE.SpotLight(0xffffff);
      luceBagno.position.set(96, 150, 60);
      luceBagno.castShadow = true;
      luceBagno.intensity = 1;
      luceBagno.shadowCameraNear = 10;
      luceBagno.shadowCameraFar = 200;
      //luceBagno.target = pav_bagno;
      //scene.add(luceBagno);

      return [spotLightAll,spotLightAll2,spotLightAll3]
  }