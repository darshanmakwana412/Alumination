
$(document).ready(function(){

  $('.carousel').carousel();


  setInterval(function () {$('.carousel').carousel('next');}, 2500);
  

  // var elems = document.querySelectorAll('.carousel');
  // var instances = M.Carousel.init(elems, options);















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

    gsap.registerPlugin(ScrollTrigger);

  // gsap.from(".laptop ul li", {y:-200, duration: 1});
  // gsap.from(".alumtext", {y:200, duration: 3, ease:Elastic.easeOut.config(0.7, 0.4)});
  
    gsap.to(".island", {
      scrollTrigger: {
        scrollTrigger: {
          trigger: ".abthead",
          toggleActions: "reset reset reset reset"

        },
      
   
      },
      opacity: 0.5
    });

  gsap.to(".clouds", {
      scrollTrigger: {
        scrollTrigger: {
          trigger: ".abthead",
          toggleActions: "reset reset reset reset"

        }
      
       
      },
      y: 50
    })

    gsap.from(".abthead", {
      scrollTrigger: {
        scrollTrigger: {
          trigger: ".abthead",
        } 
      },
      y: 250,
      opacity: 0,
      duration: 5,
      ease:Elastic.easeOut.config(0.7, 0.4)
    })


    gsap.from(".abttext", {
      scrollTrigger: {
        scrollTrigger: {
          trigger: ".abttext",
        } 
      },
      x: -250,
      opacity: 0,
      duration: 5,
      ease:Elastic.easeOut.config(0.7, 0.4)
    })


 

    

    // gsap.to(".clouds", {
    //   scrollTrigger: {
    //     scrollTrigger: {
    //       trigger: ".abthead",
    //       toggleActions: "reset reset reset reset"

    //     }
      
       
    //   },
    //   y: 50
    // })


    const buttons = gsap.utils.toArray('.circle');
    buttons.forEach((btn) => {
      gsap.from(btn, {
        scrollTrigger: {
          trigger: btn,
          toggleClass: 'trigger'
        }
      });
    });


    target1 = $('.anum').first()
  });





