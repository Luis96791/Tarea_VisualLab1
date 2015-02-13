var foundRobotPosition = {x:0, y:0}, //posicion del robot encontrada
    foundByParent=false, // encontrar por paternidad es falso... Robots independientes
    foundByClone=false; // si fuese true comenzaria disparando a su clon antes de dispararle a su enemigo

var Robot = function(robot){ // aqui se despliegan todas las funciones que administrara nuestro robot
  //Esta es la configuracion inicial del robot si dentro de la funcion hubiese otro evento diferente a robot
  //Las acciones asignadas no se ejecutarian para nuestro robot.
  robot.clone();//llama la funcion clonar robot por un limite de ataques enemigos...
  this.options = { // ejecutar las sguientes opciones de ataque
    direction: 1, // si alteramos la direccion a un numero poco mayor que 1 posiblemente el 
    // robot clon le dispararia a su robot padre...
    aheadWhileTurning: 20, // hacia adelante y voltear obedece al numero asignado...
    //si el numero asignado fuese 20 y dependiendo de la posicion de mis robot's hacia el enemigo
    //mis robot's atacarian por turnos...
    shootIterations: 5, // por cada iteraccion dispara 5 veces
    distanceToWalkBackOnHit: 10, // luego de disparar y si se recibe un ataque del enemigo retrocede dependiendo del numero asignado
    hasCloned: true // En este caso el clon se vuelve verdadero lo que significa que va a simular al robot verdadero
  };//Se cierra el paquete de opciones
};//Se cierran las funciones del robot...

Robot.prototype.onIdle = function(ev) { // Esta funcion ordena la inactividad del robot pero luego se
  //asigna una funcion que ordena un evento...
  var robot = ev.robot;// Como ya se estructuraron las funciones del robot se manda llamar el evento con las funciones
  //del robot
  
  if (
    (foundByClone && robot.parentId == null)// Esta decision me sirve para buscar el clon seguido de el Id del robot padre
    ||//ya sea nula o no terminaría desplegandome las siguientes funciones:
    (foundByParent && robot.parentId != null)
 	){
    var deltaX = Math.abs(robot.position.x - foundRobotPosition.x);//Segun el valor que tengan las coordenadas definidas al inicio
    //declaramos una variable y con la función Math se hace la operacion posicion X (original)del robot menos 
    //la posicion donde se encuentra en el momento de funcionamiento..
    var deltaY = Math.abs(robot.position.y - foundRobotPosition.y);//Lo mismo hace para la posicion Y
    var angle = Math.atan(deltaY / deltaX);//Para determinar el angulo divide el resultado de la variable X entre el resultado de la variable Y...
    angle = angle * (180/Math.PI);//El angulo es multiplicado haciendo uso de Math 
    foundByClone = true;//se le asigna false como valor al clon
    foundByParent = true;//tambien al robot padre se le asigna false si se le asigna true dispararian hacia cualquier posicion del tablero...
    robot.turn(angle);// el robot responde a los resultados del angulo

    for (var i=0; i < this.options.shootIterations; i++) {//mientras se ejecuten las opciones
      robot.fire();//disparos
      robot.ahead(10);//retirarse luego de un contra ataque...
      robot.rotateCannon(-1);//rotacion del cañon -1 en sentido contrario a las manecillas del reloj...
    }//fin del for    
  }//fin de la estructura condicional
  
	robot.turn(1);
	robot.ahead(1);
};

Robot.prototype.onScannedRobot = function(ev) { //escanear la funcion del robot
  var robot = ev.robot, scanned = ev.scannedRobot;//declara una variable para evaluar las funciones del robot...
  
  foundRobotPosition = scanned.position; //buscando la posicion del robot 
  if (robot.parentId == null) {// si el robot padre es encontrado el robot padre y el clon seran verdaderos
	  foundByParent = true;//si estas instrucciones fuesen falsas los robots harian una busqueda del objetivo 
    //en las paredes del tablero...
  } else {
    foundByClone = true;
  }

  if (scanned.parentId != null || 
      robot.parentId == scanned.id ||
      robot.id == scanned.parentId){
    return;
  }
  //this.options.direction = (scanned.angle > 180) ? 1 : -1;

  for (var i=0; i < this.options.shootIterations; i++) {// esta es una repeticion del for de arriba 
    //solo que este se encuentra dentro de la funcion onScanned
    robot.fire();
    robot.ahead(10);
    robot.rotateCannon(-1);
  }
};

Robot.prototype.onWallCollision = function(ev) {
  ev.robot.turn(180);
  ev.robot.back(this.options.distanceToWalkBackOnHit);
};

Robot.prototype.onRobotCollision = function(ev) {
};

Robot.prototype.onHitByBullet = function(ev) {
  ev.robot.turn(ev.bearing);
};
