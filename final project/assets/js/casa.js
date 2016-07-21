function pianoTerra(loader, casa, objects){
   
        loader.load('assets/models/pianoTerra.obj', function (obj) {

        global_o = obj;

        var material = new THREE.MeshLambertMaterial({color: 0xaaaaaa});
        material.side = THREE.DoubleSide;
        obj.children[0].material = material;
        mesh = obj.children[0];
    
        mesh.scale.set(20,20,20);
        // mesh.rotation.x = -Math.PI/2;
        objects.push(mesh);
        casa.add(mesh);

    });  

      var textures_esterne =  new THREE.Object3D();
      var textures_pavimenti =  new THREE.Object3D();
      var textures_interne =  new THREE.Object3D();

      textures_esterne = mkOuterTexturedWalls1();
      casa.add(textures_esterne);

      textures_pavimenti = mkAllFloorings1();
      casa.add(textures_pavimenti);

      textures_interne = mkInnerTexturedWalls1();
      casa.add(textures_interne);

      return casa;
}


function primoPiano(loader, casa, objects){
   loader.load('assets/models/primoPiano.obj', function (obj) {

        global_o = obj;

        var material = new THREE.MeshLambertMaterial({color: 0xaaaaaa});
        material.side = THREE.DoubleSide;
        obj.children[0].material = material;
       
        var mesh = obj.children[0];
    
        mesh.scale.set(20,20,20);
        objects.push(mesh);
        casa.add(mesh);

      });

      var textures =  new THREE.Object3D();
      textures = mkOuterTexturedWalls2();
      casa.add(textures);

      return casa;

 }



function secondoPiano(loader, casa,objects){
    

   loader.load('assets/models/secondoPiano.obj', function (obj) {

        global_o = obj;
        
        var casa_bsp    = new ThreeBSP(obj.children[0].geometry);
        
        var cube_geometry = new THREE.BoxGeometry( 1.6, 1.401, 0.6 );
        var cube_mesh = new THREE.Mesh( cube_geometry );
        cube_mesh.position.set(1.15,3.6999,0.00009);
        var cube_bsp = new ThreeBSP( cube_mesh );

        var material = new THREE.MeshLambertMaterial({color: 0xaaaaaa});
        material.side = THREE.DoubleSide;
      
        var subtract_bsp = casa_bsp.subtract( cube_bsp );
       
        var result = new THREE.Mesh( subtract_bsp.toGeometry(), material );
        
        result.geometry.computeFaceNormals();

        var parete_geometry = new THREE.BoxGeometry( 1, 1, 1 );
       
        var parete_mesh = new THREE.Mesh( cube_geometry ,material );
        parete_mesh.scale.set(0.08,1.1,5);
        parete_mesh.position.set(2,3.6,1.5);

        result.add(parete_mesh);

        result.material = material;

        result.scale.set(20,20,20);

        casa.add(result);

    

        

      });

      var textures =  new THREE.Object3D();
      textures = mkOuterTexturedWalls3();
      casa.add(textures);

      return casa;
    

}


function mk_casa(loader,terra,primo,secondo,objects){
      
      var casa = new THREE.Object3D();
    
      terra = pianoTerra(loader, terra, objects);
      terra.scale.set( 1, 1.045, 1 );
      casa.add(terra); 
      casa.terra = terra;

      primo = primoPiano(loader, primo, objects)
      primo.translateZ(60);
      casa.add(primo);  
      casa.primo = primo;

      secondo = secondoPiano(loader, secondo,  objects)
      secondo.translateZ(120);
      casa.add(secondo);  
      casa.secondo = secondo;
    

      return casa;

}




 