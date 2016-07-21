
function mkInnerTexturedWalls1() {
	var walls = new THREE.Object3D();

//////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////


	var parete_1 = [[6.2+0.05/16, 0.2], [0.0-0.05/16, 0.2], [0.0-0.05/16, 2.6], [6.2+0.05/16, 2.6], [6.2+0.05/16, 0.2]];
	var hole_1_parete_1 = [[1.9, 1.05], [1.9, 1.8], [1.05, 1.8], [1.05, 1.05], [1.9, 1.05]];
	var hole_2_parete_1 = [[5.4, 1.05], [5.4, 1.8], [4.95, 1.8], [4.95, 1.05], [5.4, 1.05]];
	var hole_3_parete_1 = [[3.8, 1.05], [3.8, 1.8], [3.4, 1.8], [3.4, 1.05], [3.8, 1.05]];
	var hole_4_parete_1 = [[4.6, 1.05], [4.6, 1.8], [4.2, 1.8], [4.2, 1.05], [4.6, 1.05]];

	var muro_1 = mkTexturedShape("cemento.jpg", 0.1, 0.1, parete_1, 
			[hole_1_parete_1,hole_2_parete_1,
			hole_3_parete_1,hole_4_parete_1]);
	
	muro_1.rotation.x = Math.PI/2;
	muro_1.position.z = 1.8;
	muro_1.position.y = 123.7;
	muro_1.scale.set(24.2,22,10);
	
//////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////


	var parete_2 = [[0,0],[0,10],[20,10],[20,0]];
	var hole_1_parete_2 = [[1.3,0],[3.1,0],[3.1,8.2],[1.3,8.2]];
	var hole_2_parete_2 = [[5.6,0],[8.4,0],[8.4,8.2],[5.6,8.2]];

	var muro_2 = mkTexturedShape("cemento.jpg", 0.1, 0.1, parete_2, [hole_1_parete_2,hole_2_parete_2]);
	muro_2.rotation.x = Math.PI/2;
	muro_2.scale.set(6.8,5.7,1);
	muro_2.position.x = 36;
	muro_2.position.y = 81.9;
	muro_2.position.z = 3;

//////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////


	var parete_3 =  [[0,0],[0,10],[16.5,10],[16.5,0]];
	var hole_1_parete_3 = [[1.3,0],[3.1,0],[3.1,8.2],[1.3,8.2]];
	var hole_2_parete_3 = [[5.6,0],[8.4,0],[8.4,8.2],[5.6,8.2]];

	var muro_3 = mkTexturedShape("cemento.jpg", 0.1, 0.1, parete_3, [hole_1_parete_3,hole_2_parete_3]);
	muro_3.rotation.x = Math.PI/2;
	muro_3.scale.set(6.8,5.7,1);
	muro_3.position.x = 36;
	muro_3.position.y = 84.3;
	muro_3.position.z = 3;

//////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////


	var parete_4 = [[0,0],[0,10],[10,10],[10,0]];
	var muro_4 = mkTexturedShape("cemento.jpg", 0.1, 0.1, parete_4, []);
	muro_4.rotation.x = Math.PI/2;

//////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////



	var parete_5 = [[0,0],[0,10],[10,10],[10,0]];
	var hole_1_parete_5 = [[3.8,0],[4.8,0],[4.8,8.5],[3.8,8.5]];

	var muro_5 = mkTexturedShape("cemento.jpg", 0.1, 0.1, parete_5, 
			[hole_1_parete_5]);

	muro_5.scale.set(12.5,6,1);
	muro_5.rotation.x = Math.PI/2;
	muro_5.rotation.y = -Math.PI/2;
	
	muro_5.position.x = 147.3;
	muro_5.position.y = 125;

//////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////



	var parete_6 = [[0,0],[0,10],[10,10],[10,0]];
	var hole_1_parete_6 = [[0.8,0],[2.9,0],[2.9,8.4],[0.8,8.4]];
	var muro_6 = mkTexturedShape("cemento.jpg", 0.1, 0.1, parete_6, 
			[hole_1_parete_6]);

	muro_6.scale.set(6.5,6,1);
	muro_6.rotation.z = Math.PI/2;
	muro_6.rotation.y = Math.PI/2;
	muro_6.position.x = 68.3;
	muro_6.position.y = 60;

//////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////


	var parete_7 = [[0,0],[0,10],[10,10],[10,0]];
	var hole_1_parete_7 = [[0.8,0],[2.9,0],[2.9,8.4],[0.8,8.4]];
	var muro_7 = mkTexturedShape("cemento.jpg", 0.1, 0.1, parete_7, 
			[hole_1_parete_7]);

	
	muro_7.scale.set(6.5,6,1);
	muro_7.rotation.z = Math.PI/2;
	muro_7.rotation.y = Math.PI/2;
	muro_7.position.x = 65.3;
	muro_7.position.y = 60;

	
	walls.add(muro_1);
	walls.add(muro_2);
	walls.add(muro_3);
	walls.add(muro_4);
	walls.add(muro_5);
	walls.add(muro_6);
	walls.add(muro_7);
	
	return walls;
}


function mkOuterTexturedWalls1() {
	var walls = new THREE.Object3D();


	var dwelling_northWall_pList = [[0.0-0.05/16, 0.0], [12.4+0.05/16, 0.0], [12.4+0.05/16, 2.6], [0.0-0.05/16, 2.6], [0.0-0.05/16, 0.0]];
	var dwelling_northWall_garage_pList = [[1, 0.25], [5.7568703, 0.25], [5.7568703, 2.2], [0.5797793, 2.2], [0.5797793, 0.25]];
	
	var dwelling_southWall_pList = [[0.0-0.05/16, 0.0], [12.4+0.05/16, 0.0], [12.4+0.05/16, 2.6], [0.0-0.05/16, 2.6], [0.0-0.05/16, 0.0]];
	
	var dwelling_eastWall_pList = [[0.0-0.05/16, 0.0], [6.2+0.05/16, 0.0], [6.2+0.05/16, 2.6], [0.0-0.05/16, 2.6], [0.0-0.05/16, 0.0]];
	
	var dwelling_westWall_pList = [[6.2+0.05/16, 0.0], [0.0-0.05/16, 0.0], [0.0-0.05/16, 2.6], [6.2+0.05/16, 2.6], [6.2+0.05/16, 0.0]];
	var dwelling_westWall_saletta_pList = [[1.9, 1.05], [1.9, 1.8], [1.05, 1.8], [1.05, 1.05], [1.9, 1.05]];
	var dwelling_westWall_saletta_pList2 = [[5.4, 1.05], [5.4, 1.8], [4.95, 1.8], [4.95, 1.05], [5.4, 1.05]];
	var dwelling_westWall_saletta_pList3 = [[3.8, 1.05], [3.8, 1.8], [3.4, 1.8], [3.4, 1.05], [3.8, 1.05]];
	var dwelling_westWall_saletta_pList4 = [[4.6, 1.05], [4.6, 1.8], [4.2, 1.8], [4.2, 1.05], [4.6, 1.05]];


	var dwelling_northWall = mkTexturedShape("muro.jpeg", 0.085, 0.35, dwelling_northWall_pList, [
		dwelling_northWall_garage_pList ]);

	dwelling_northWall.rotation.x = Math.PI/2;
	dwelling_northWall.rotation.y = Math.PI/2;
	dwelling_northWall.position.x = -0.3;

	dwelling_northWall.scale.set(10.5,23,0);

	var dwelling_southWall = mkTexturedShape("muro.jpeg", 0.085, 0.35, dwelling_southWall_pList, []);
	var dwelling_southWall2 = mkTexturedShape("muro.jpeg", 0.085, 0.35, dwelling_southWall_pList, []);
	
	dwelling_southWall.rotation.x = Math.PI/2;
	dwelling_southWall.rotation.y = Math.PI/2;
	dwelling_southWall.position.x = 176.1;
	dwelling_southWall.scale.set(6.75,23,10);

	dwelling_southWall2.rotation.x = Math.PI/2;
	dwelling_southWall2.rotation.y = Math.PI/2;
	dwelling_southWall2.position.x = 150.3;
	dwelling_southWall2.position.y = 82.5;
	dwelling_southWall2.scale.set(3.8,23,10);

	

	var dwelling_eastWall = mkTexturedShape("muro.jpeg", 0.17, 0.4, dwelling_eastWall_pList);
	dwelling_eastWall.rotation.x = Math.PI/2;
	dwelling_eastWall.position.y = -0.3;

	dwelling_eastWall.scale.set(28.3,23,10);

	var dwelling_eastWall2 = mkTexturedShape("muro.jpeg", 0.05, 0.4, dwelling_eastWall_pList);
	dwelling_eastWall2.rotation.x = Math.PI/2;
	dwelling_eastWall2.position.x = 151;
	dwelling_eastWall2.position.y = 84.3;

	dwelling_eastWall2.scale.set(4,23,10);

	var dwelling_westWall = mkTexturedShape("muro.jpeg", 0.17, 0.4, dwelling_westWall_pList, [
		dwelling_westWall_saletta_pList, dwelling_westWall_saletta_pList2,dwelling_westWall_saletta_pList3,
		dwelling_westWall_saletta_pList4]);
	dwelling_westWall.rotation.x = Math.PI/2;
	dwelling_westWall.position.y = 130.3;

	dwelling_westWall.scale.set(24.2,23,10);


	walls.add(dwelling_northWall);
	walls.add(dwelling_southWall);
	walls.add(dwelling_southWall2);
	walls.add(dwelling_eastWall2);
	walls.add(dwelling_eastWall);
	walls.add(dwelling_westWall);

	return walls;
}


function mkOuterTexturedWalls2() {
	var walls = new THREE.Object3D();


	var dwelling_northWall_pList = [[0.0-0.05/16, 0.0], [12.4+0.05/16, 0.0], [12.4+0.05/16, 2.6], [0.0-0.05/16, 2.6], [0.0-0.05/16, 0.0]];
	var dwelling_northWall_porta_pList = [[1, 0.25], [3.45, 0.25], [3.45, 2.2], [1.1, 2.2], [1.1, 0.25]];

	var dwelling_southWall_pList = [[0.0-0.05/16, 0.0], [12.4+0.05/16, 0.0], [12.4+0.05/16, 2.6], [0.0-0.05/16, 2.6], [0.0-0.05/16, 0.0]];
	var dwelling_southWall_sala_pList = [[6.2, 0.25], [6.2, 2.2], [2.1, 2.2], [2.1, 0.25], [6.2, 0.25]];
	var dwelling_southWall_sala_pList2 = [[10.5, 0.25], [10.5, 2.2], [6.5, 2.2], [6.5, 0.25], [10.5, 0.25]];

	var dwelling_southWall2_sala_pList = [[5.2, 0.25], [5.2, 2.2], [3.1, 2.2], [3.1, 0.25], [5.2, 0.25]];
	var dwelling_southWall2_sala_pList2 =  [[7.8, 0.25], [7.8, 2.2], [5.7, 2.2], [5.7, 0.25], [7.8, 0.25]];
	

	var dwelling_eastWall_pList = [[0.0-0.05/16, 0.0], [6.2+0.05/16, 0.0], [6.2+0.05/16, 2.6], [0.0-0.05/16, 2.6], [0.0-0.05/16, 0.0]];


	var dwelling_westWall_pList = [[6.2+0.05/16, 0.0], [0.0-0.05/16, 0.0], [0.0-0.05/16, 2.6], [6.2+0.05/16, 2.6], [6.2+0.05/16, 0.0]];
	var dwelling_westWall_saletta_pList = [[1.25, 1.18], [1.25, 1.93], [0.85, 1.93], [0.85, 1.18], [1.25, 1.18]];
	var dwelling_westWall_saletta_pList2 = [[4.15, 1.2], [4.15, 2.1], [3, 2.1], [3, 1.2], [4.15, 1.2]];
	

	var dwelling_northWall = mkTexturedShape("muro.jpeg", 0.085, 0.35, dwelling_northWall_pList, [
		dwelling_northWall_porta_pList ]);

	dwelling_northWall.rotation.x = Math.PI/2;
	dwelling_northWall.rotation.y = Math.PI/2;
	dwelling_northWall.position.x = -0.3;

	dwelling_northWall.scale.set(11,23,0);

	var dwelling_southWall = mkTexturedShape("muro.jpeg", 0.085, 0.35, dwelling_southWall_pList, 
		[dwelling_southWall_sala_pList,dwelling_southWall_sala_pList2]);
	var dwelling_southWall2 = mkTexturedShape("muro.jpeg", 0.085, 0.35, dwelling_southWall_pList, 
		[dwelling_southWall2_sala_pList,dwelling_southWall2_sala_pList2]);
	
	dwelling_southWall.rotation.x = Math.PI/2;
	dwelling_southWall.rotation.y = Math.PI/2;
	dwelling_southWall.position.x = 176.1;
	dwelling_southWall.scale.set(7.1,23,10);

	dwelling_southWall2.rotation.x = Math.PI/2;
	dwelling_southWall2.rotation.y = Math.PI/2;
	dwelling_southWall2.position.x = 150.3;
	dwelling_southWall2.position.y = 88.1;
	dwelling_southWall2.scale.set(3.8,23,10);

	

	var dwelling_eastWall = mkTexturedShape("muro.jpeg", 0.17, 0.4, dwelling_eastWall_pList);
	dwelling_eastWall.rotation.x = Math.PI/2;
	dwelling_eastWall.position.y = -0.3;

	dwelling_eastWall.scale.set(28.3,23,10);

	var dwelling_eastWall2 = mkTexturedShape("muro.jpeg", 0.05, 0.4, dwelling_eastWall_pList);
	dwelling_eastWall2.rotation.x = Math.PI/2;
	dwelling_eastWall2.position.x = 151;
	dwelling_eastWall2.position.y = 88.1;

	dwelling_eastWall2.scale.set(4,23,10);

	var dwelling_westWall = mkTexturedShape("muro.jpeg", 0.17, 0.4, dwelling_westWall_pList, [
		dwelling_westWall_saletta_pList, dwelling_westWall_saletta_pList2]);
	dwelling_westWall.rotation.x = Math.PI/2;
	dwelling_westWall.position.y = 136.3;

	dwelling_westWall.scale.set(24.2,23,10);


	walls.add(dwelling_northWall);
	walls.add(dwelling_southWall);
	walls.add(dwelling_southWall2);
	walls.add(dwelling_eastWall2);
	walls.add(dwelling_eastWall);
	walls.add(dwelling_westWall);

	return walls;
}


function mkOuterTexturedWalls3() {
	var walls = new THREE.Object3D();


	var dwelling_northWall_pList = [[0.0-0.05/16, 0.0], [12.4+0.05/16, 0.0], [12.4+0.05/16, 2.6], [0.0-0.05/16, 2.6], [0.0-0.05/16, 0.0]]
	var dwelling_northWall_finestra_pList = [[1.45, 0.25], [2.8, 0.25], [2.8, 2.2], [1.45, 2.2], [1.45, 0.25]]
	var dwelling_northWall_finestra2_pList = [[10, 1.1], [11.2, 1.1], [11.2, 2.3], [10, 2.3], [10, 1.1]]
	

	var dwelling_southWall_pList = [[0.0-0.05/16, 0.0], [12.4+0.05/16, 0.0], [12.4+0.05/16, 2.6], [0.0-0.05/16, 2.6], [0.0-0.05/16, 0.0]]
	var dwelling_southWall_sala_pList = [[7.9, 1.1], [7.9, 2.3], [3.7, 2.3], [3.7, 1.1], [7.9, 1.1]]
	var dwelling_southWall_sala_pList2 = [[8.2, 1.1], [8.2, 2.3], [10.9, 2.3], [10.9, 1.1], [8.2, 1.1]]

	var dwelling_southWall2_sala_pList = [[11, 1.1], [11, 2.3], [7.5, 2.3], [7.5, 1.1], [11, 1.1]]
	

	var dwelling_eastWall_pList = [[0.0-0.05/16, 0.0], [6.2+0.05/16, 0.0], [6.2+0.05/16, 2.6], [0.0-0.05/16, 2.6], [0.0-0.05/16, 0.0]]


	var dwelling_westWall_pList = [[6.2+0.05/16, 0.0], [0.0-0.05/16, 0.0], [0.0-0.05/16, 2.6], [6.2+0.05/16, 2.6], [6.2+0.05/16, 0.0]]
	

	var dwelling_northWall = mkTexturedShape("muro.jpeg", 0.085, 0.35, dwelling_northWall_pList, [
		dwelling_northWall_finestra_pList,dwelling_northWall_finestra2_pList ]);

	dwelling_northWall.rotation.x = Math.PI/2;
	dwelling_northWall.rotation.y = Math.PI/2;
	dwelling_northWall.position.x = -0.3;

	dwelling_northWall.scale.set(11,23,0);

	var dwelling_southWall = mkTexturedShape("muro.jpeg", 0.085, 0.35, dwelling_southWall_pList, 
		[dwelling_southWall_sala_pList,dwelling_southWall_sala_pList2]);
	var dwelling_southWall2 = mkTexturedShape("muro.jpeg", 0.085, 0.35, dwelling_southWall_pList, 
		[dwelling_southWall2_sala_pList]);
	
	dwelling_southWall.rotation.x = Math.PI/2;
	dwelling_southWall.rotation.y = Math.PI/2;
	dwelling_southWall.position.x = 176.1;
	dwelling_southWall.scale.set(7.1,23,10);

	dwelling_southWall2.rotation.x = Math.PI/2;
	dwelling_southWall2.rotation.y = Math.PI/2;
	dwelling_southWall2.position.x = 150.3;
	dwelling_southWall2.position.y = 88.1;
	dwelling_southWall2.scale.set(3.8,23,10);

	

	var dwelling_eastWall = mkTexturedShape("muro.jpeg", 0.17, 0.4, dwelling_eastWall_pList);
	dwelling_eastWall.rotation.x = Math.PI/2;
	dwelling_eastWall.position.y = -0.3;

	dwelling_eastWall.scale.set(28.3,23,10);

	var dwelling_eastWall2 = mkTexturedShape("muro.jpeg", 0.05, 0.4, dwelling_eastWall_pList);
	dwelling_eastWall2.rotation.x = Math.PI/2;
	dwelling_eastWall2.position.x = 150.8;
	dwelling_eastWall2.position.y = 88.15;

	dwelling_eastWall2.scale.set(4.1,23,10);

	var dwelling_westWall = mkTexturedShape("muro.jpeg", 0.17, 0.4, dwelling_westWall_pList, []);
	dwelling_westWall.rotation.x = Math.PI/2;
	dwelling_westWall.position.y = 136.3;

	dwelling_westWall.scale.set(24.2,23,10);


	walls.add(dwelling_northWall);
	walls.add(dwelling_southWall);
	walls.add(dwelling_southWall2);
	walls.add(dwelling_eastWall2);
	walls.add(dwelling_eastWall);
	walls.add(dwelling_westWall);

	return walls;
}




function mkAllFloorings1() {
	
	var floorings = new THREE.Object3D();
	var garage_floor_pList = [[0,0],[0,120],[68,120],[68,78],[170,78],[170,0]];
	var saletta_floor_pList = [[0,0],[0,10],[10,10],[10,0]];
    var garage_floor = mkTexturedShape("mattonelle.jpg", 0.04, 0.04, garage_floor_pList);
          garage_floor.position.z = 6.2;
          garage_floor.position.y = 6;

     var saletta_floor = mkTexturedShape("floor-wood.jpg", 0.08, 0.08, saletta_floor_pList);
          saletta_floor.position.z = 6.2;
          saletta_floor.position.y = 84;
          saletta_floor.position.x = 68;

          saletta_floor.scale.set(8,4,1);


	floorings.add(garage_floor);
	floorings.add(saletta_floor);
	

	return floorings;
}