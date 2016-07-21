

function mkSpotLight(x,y,z, mesh){
      
      var spotLight = new THREE.SpotLight(0xffffff);
      spotLight.position.set(x, y, z);
      spotLight.castShadow = true; 
      spotLight.intensity = 0.5;
      spotLight.target = mesh;
      spotLight.shadowDarkness = 1; 
      spotLight.shadowCameraNear = 10; 
      spotLight.shadowCameraFar = 100;
      spotLight.shadowCameraVisible = true;

	    mesh.add(spotLight);
	       
      return spotLight;

}