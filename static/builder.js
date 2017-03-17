const increment = 1
const width = window.innerWidth / 1.5
const height = window.innerHeight / 1.5

var notWorkingDiv = document.getElementById('notWorkingDiv');
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

//function for building the voxels
function voxel(x, y, z) {
  var geometry = new THREE.BoxGeometry(increment, increment, increment);
  var material = new THREE.MeshLambertMaterial({color: 0xf6546a})
  var mesh = new THREE.Mesh(geometry, material)
  mesh.position.x = x
  mesh.position.y = y
  mesh.position.z = z
  mesh.rotation.x = 500
  scene.add(mesh);
  return mesh
}

var buildBtn = document.getElementById('buildButton');

function build(event) {
  for(var i = 0; i < scene.children.length; i++) {
    scene.remove(scene.children[i]);
  }

  const code = editorTextField.value;
  eval(code)
  scene.add(light);
}

let editorTextField = document.getElementById('editor')

var light = new THREE.PointLight(0xffffff, 1.2);
light.position.set(0, 0, 6)
scene.add(light);

camera.position.z = 60;
var mousedown = false;

var zoomInButton = document.getElementById('in');
var zoomOutButton = document.getElementById('out');

zoomInButton.addEventListener('click', function(event) {
  camera.position.z += increment * 10;
}, false);

zoomOutButton.addEventListener('click', function(event) {
  camera.position.z -= increment * 10;
}, false);

window.onload = function() {
  build()
}

var startX;
var startY;

document.addEventListener('mousedown', function(event) {
  mousedown = true;
  startX = event.screenX;
  startY = event.screenY;
});

document.addEventListener('mousemove', function(event) {
  if(mousedown) {
    if(startX > event.screenX) {
      camera.position.x += 0.1;
    } else if(startX < event.screenX) {
      camera.position.x -= 0.1;
    }

    if(startY > event.screenY) {
      camera.position.y -= 0.1;
    } else if(startY < event.screenY) {
      camera.position.y += 0.1;
    }
  }
});

document.addEventListener('mouseup', function(event) {
  mousedown = false;
});

buildButton.addEventListener('click', build, false);

var backgroundColor = document.getElementById('backgroundSelector');
var boxColor = document.getElementById('boxColor');
var changeColorButton = document.getElementById('changeColorButton');

changeColorButton.addEventListener('click', function() {
  renderer.setClearColor(backgroundColor.value);
  scene.children[0].material.color.setRGB(255, 255, 255);
});

var title = document.getElementById('title');
var save = document.getElementById('save');

var url = window.location.href
console.log(url)
id = url.split('/')[4]

jQuery.each( [ "put", "delete" ], function( i, method ) {
  jQuery[ method ] = function( url, data, callback, type ) {
    if ( jQuery.isFunction( data ) ) {
      type = type || callback;
      callback = data;
      data = undefined;
    }

    return jQuery.ajax({
      url: url,
      type: method,
      dataType: type,
      data: data,
      success: callback
    });
  };
});

save.addEventListener('click', function() {
  $.put('/builder/' + id, {title: title.value, code: editorTextField.value});
  console.log('clicked')
}, false);
