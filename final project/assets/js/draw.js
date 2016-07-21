      function drawShape() {

        // create a basic shape
        var shape = new THREE.Shape();

        // startpoint
        shape.moveTo(10, 10);

        // straight line upwards
        shape.lineTo(10, 40);

        // the top of the figure, curve to the right
        shape.bezierCurveTo(15, 25, 25, 25, 30, 40);

        // spline back down
        shape.splineThru(
            [new THREE.Vector2(32, 30),
              new THREE.Vector2(28, 20),
              new THREE.Vector2(30, 10),
            ])

        // curve at the bottom
        shape.quadraticCurveTo(20, 15, 10, 10);

        // add 'eye' hole one
        // var hole1 = new THREE.Path();
        // hole1.absellipse(16, 24, 2, 3, 0, Math.PI * 2, true);
        // shape.holes.push(hole1);

        // // add 'eye hole 2'
        // var hole2 = new THREE.Path();
        // hole2.absellipse(23, 24, 2, 3, 0, Math.PI * 2, true);
        // shape.holes.push(hole2);

        // // add 'mouth'
        // var hole3 = new THREE.Path();
        // hole3.absarc(20, 16, 2, 0, Math.PI, true);
        // shape.holes.push(hole3);

        // return the shape
        return shape;
      }

      function createMesh (geom) {

        // assign two materials
        var meshMaterial = new THREE.MeshNormalMaterial();
        meshMaterial.side = THREE.DoubleSide;
        var wireFrameMat = new THREE.MeshBasicMaterial();
        wireFrameMat.wireframe = true;

        // create a multimaterial
        var mesh = THREE.SceneUtils.createMultiMaterialObject(geom, [meshMaterial, wireFrameMat]);

        return mesh;
      }

      function createLine(shape, spaced) {
        if (!spaced) {
          var mesh = new THREE.Line(shape.createPointsGeometry(10), new THREE.LineBasicMaterial({ color: 0xff3333, linewidth: 2 }));
          return mesh;
        } else {
          var mesh = new THREE.Line(shape.createSpacedPointsGeometry(3), new THREE.LineBasicMaterial({ color: 0xff3333, linewidth: 2 }));
          return mesh;
        }
      }


      
      


