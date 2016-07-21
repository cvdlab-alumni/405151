function importaModello(mesh, loader){
	  
      loader.load('assets/models/primoPiano.obj', function (obj) {

        global_o = obj;

        var material = new THREE.MeshLambertMaterial({color: 0xaaaaaa});
        material.side = THREE.DoubleSide;
        obj.children[0].material = material;
        mesh = obj.children[0];
       

        });
       return mesh;
  }

        

			
