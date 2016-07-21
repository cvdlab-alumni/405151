function makeSkyBox(x,y,z){

  var imagePrefix = "assets/skybox/";
  var directions  = ["0004", "0002", "0006", "0005", "0001", "0003"];
  var imageSuffix = ".png";
  var skyGeometry = new THREE.BoxGeometry( x, y, z ); 
  
  var materialArray = [];
  for (var i = 0; i < 6; i++)
    materialArray.push( new THREE.MeshBasicMaterial({
      map: THREE.ImageUtils.loadTexture( imagePrefix + directions[i] + imageSuffix ),
      side: THREE.BackSide
    }));
  var skyMaterial = new THREE.MeshFaceMaterial( materialArray );
  var skyBox = new THREE.Mesh( skyGeometry, skyMaterial );


  skyBox.rotation.x = Math.PI/2;
  return skyBox;

}

  
