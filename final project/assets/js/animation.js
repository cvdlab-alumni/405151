
function openDoor(door){

	if(!door.open){
		var openDoor = new TWEEN.Tween(door.rotation)
      .to({z: Math.PI/2},1000)
      .start();
      door.open = true;
	}
	else{
	 var closeDoor = new TWEEN.Tween(door.rotation)
      .to({z: 0},1000)
      .start();
      door.open = false;
	}

}

function slideDoor(door){

	if(!door.open){
		var openDoor = new TWEEN.Tween(door.position)
      .to({y: 102.5},1000)
      .start();
      door.open = true;
	}
	else{
	 var closeDoor = new TWEEN.Tween(door.position)
      .to({y: 92.5},1000)
      .start();
      door.open = false;
	}

}

function openWindow(win){

	if(!win.open){
		var openDoor = new TWEEN.Tween(win.rotation)
      .to({x: Math.PI/5},1000)
      .start();
      win.open = true;
	}
	else{
	 var closeDoor = new TWEEN.Tween(win.rotation)
      .to({x: 0},1000)
      .start();
      win.open = false;
	}

}



function openGarage(door){

	if(!door.open){
		var open = new TWEEN.Tween(door.rotation)
      .to({y: Math.PI/2},1000)
       .start();

      // var move = new TWEEN.Tween(door.position)
      // .to({x: 50},1000)
      // .chain(open)
     

      door.open = true;
	}
	else{
	 var close = new TWEEN.Tween(door.rotation)
      .to({y: 0},1000)
      .start();

      // var move = new TWEEN.Tween(door.position)
      // .to({y: 0},1000)
      // .start();
      door.open = false;
	}

}

