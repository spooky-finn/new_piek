var progress = document.getElementById('progressbar');
var totalHeight = document.body.scrollHeight - window.innerHeight;

var prevScrollpos = window.pageYOffset; //header transform


window.onscroll = function(){
  let progressHeight = (window.pageYOffset / totalHeight) * 100;
  progress.style.height = progressHeight + "%";



// //--------------------- header transform
  var currentScrollPos = window.pageYOffset;
    if (prevScrollpos > currentScrollPos) {
      document.getElementById("navbar_alpha").style.top = "0";
    } else {
      document.getElementById("navbar_alpha").style.top = "-4em";
    }
    prevScrollpos = currentScrollPos;
    //--------------------- -----------------
  }
