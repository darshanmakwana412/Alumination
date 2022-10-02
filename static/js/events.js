
let bounds;

function rotateToMouse(e) {
  var bounds = e.currentTarget.getBoundingClientRect()
  const mouseX = e.clientX;
  const mouseY = e.clientY;
  const leftX = mouseX - bounds.x;
  const topY = mouseY - bounds.y;
  const center = {
    x: leftX - bounds.width / 2,
    y: topY - bounds.height / 2
  }
  const distance = Math.sqrt(center.x**2 + center.y**2);
  
  e.currentTarget.style.transform = `
    scale3d(1.07, 1.07, 1.07)
    rotate3d(
      ${center.y / 100},
      ${-center.x / 100},
      0,
      ${Math.log(distance)* 2}deg
    )
  `;
  
  e.currentTarget.querySelector('.glow').style.backgroundImage = `
    radial-gradient(
      circle at
      ${center.x * 2 + bounds.width/2}px
      ${center.y * 2 + bounds.height/2}px,
      #ffffff55,
      #0000000f
    )
  `;
}



const cards = document.querySelectorAll('.card');

cards.forEach($card => {

  console.log($card)
  $card.addEventListener('mousemove', rotateToMouse);

  $card.addEventListener('mouseleave', () => {
    document.removeEventListener('mousemove', rotateToMouse);
    $card.style.transform = '';
    $card.style.background = '';
  });
});



// var $card = document.querySelectorAll('.card')[0];
// $card.addEventListener('mouseenter', () => {
//   bounds = $card.getBoundingClientRect();
//   document.addEventListener('mousemove', rotateToMouse);
// });

// $card.addEventListener('mouseleave', () => {
//   document.removeEventListener('mousemove', rotateToMouse);
//   $card.style.transform = '';
//   $card.style.background = '';
// });




navshow = false
    
$('#hamburger').click(function(){
    $(this).toggleClass('open')
    navshow = !navshow
    if(navshow) $('#overlay').animate({height:$(window).height()},200);
    else $('#overlay').animate({height:0},200);
    
  })

  $('#overlay ul li').click(function(){
    $('#overlay').animate({height:0},200);
    navshow = false
    $('#hamburger').toggleClass('open')
    
  })

godheight = $('.globalwrap').first().height()
godwidth = $('.globalwrap').first().width()
console.log(godheight)
console.log(godwidth)

  class Stage {
    constructor() {
      this.renderParam = {
        width: godwidth,
        height: godheight
      };
  
      this.cameraParam = {
        fov: 70,
        lookAt: new THREE.Vector3(0, 0, 0)
      };
  
      this.fogParam = {
        color: 0x000000,
        start: 50,
        end: 2000
      };
  
      this.scene = null;
      this.camera = null;
      this.renderer = null;
      this.geometry = null;
      this.material = null;
      this.mesh = null;
      this.isInitialized = false;
    }
  
    init() {
      this._setScene();
      this._setRender();
      this._setCamera();
      this._setFog();
  
      this.isInitialized = true;
    }
  
    _setScene() {
      this.scene = new THREE.Scene();
    }
  
    _setRender() {
      this.renderer = new THREE.WebGLRenderer({
        canvas: document.getElementById("webgl-canvas"),
        alpha: true
      });
      this.renderer.setPixelRatio(window.devicePixelRatio);
      this.renderer.setSize(this.renderParam.width, this.renderParam.height);
    }
  
    _setCamera() {
      const windowWidth = godwidth;
      const windowHeight = godheight;
  
      if (!this.isInitialized) {
        this.camera = new THREE.PerspectiveCamera(
          this.cameraParam.fov,
          this.renderParam.width / this.renderParam.height
        );
  
        this.camera.lookAt(this.cameraParam.lookAt);
      }
  
      this.camera.aspect = windowWidth / windowHeight;
      this.camera.updateProjectionMatrix();
      this.renderer.setPixelRatio(window.devicePixelRatio);
      this.renderer.setSize(windowWidth, windowHeight);
    }
  
    _setFog() {
      this.scene.fog = new THREE.Fog(
        this.fogParam.fov,
        this.fogParam.start,
        this.fogParam.end
      );
    }
  
    _render() {
      let rot = 0;
      const radian = (rot * Math.PI) / 180;
  
      rot += 0.1;
      this.camera.position.x = 1000 * Math.sin(radian);
      this.camera.position.z = 1000 * Math.cos(radian);
      this.renderer.render(this.scene, this.camera);
    }
  
    onResize() {
      this._setCamera();
    }
  
    onRaf() {
      this._render();
    }
  }
  
  class Mesh {
    constructor(stage) {
      this.stage = stage;
      this.mesh = null;
    }
  
    init() {
      this._setMesh();
    }
  
    _setMesh() {
      const vertices = [];
      const SIZE = 3000;
      const LENGTH = 3000;
      const geometry = new THREE.BufferGeometry();
      const material = new THREE.PointsMaterial({
        color: 0xffffff
      });
  
      for (let i = 0; i < LENGTH; i++) {
        const x = SIZE * (Math.random() - 0.5);
        const y = SIZE * (Math.random() - 0.5);
        const z = SIZE * (Math.random() - 0.5);
  
        vertices.push(x, y, z);
      }
  
      geometry.setAttribute(
        "position",
        new THREE.Float32BufferAttribute(vertices, 3)
      );
  
      this.mesh = new THREE.Points(geometry, material);
      this.stage.scene.add(this.mesh);
    }
  
    _render() {
      this.mesh.rotation.y += 0.001;
    }
  
    onRaf() {
      this._render();
    }
  }
  
  (() => {
    const stage = new Stage();
    const mesh = new Mesh(stage);
  
    stage.init();
    mesh.init();
  
    window.addEventListener("resize", () => {
      stage.onResize();
    });
  
    const _raf = () => {
      window.requestAnimationFrame(() => {
        stage.onRaf();
        mesh.onRaf();
  
        _raf();
      });
    };
  
    _raf();
  })();