const increment = 1;
const width = window.innerWidth / 1.5;
const height = window.innerHeight / 1.5;

var scene = new THREE.Scene();
var camera = new THREE.PerspectiveCamera(75,
  window.innerWidth/window.innerHeight, 0.1, 1000);
var renderer = new THREE.WebGLRenderer();

renderer.setSize(width, height);
renderer.setClearColor(0x3399ff);
document.body.appendChild(renderer.domElement);

function render() {
  requestAnimationFrame(render);
  renderer.render(scene, camera);
}
render();

function voxel(x, y, z) {
  var geometry = new THREE.BoxGeometry(increment, increment, increment);
  var material = new THREE.MeshLambertMaterial({color: 0xf6546a});
  var mesh = new THREE.Mesh(geometry, material);
  mesh.position.x = x;
  mesh.position.y = y;
  mesh.position.z = z;
  mesh.rotation.x = 500;
  scene.add(mesh);
  return mesh;
}

var light = new THREE.PointLight(0xffffff, 1.2);
light.position.set(0, 0, 6)
scene.add(light);

var code = document.getElementById('code');
eval(code.innerHTML)
scene.add(light)

for(var i = 0; i < scene.children.length; i++) {
  console.log(scene.children[i]);
}

camera.position.z = 60;
