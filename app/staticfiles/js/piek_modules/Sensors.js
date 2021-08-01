// Sensors animation

$('.sensor-inner').hover(
    function(){
              $('.sensor-inner:not(:hover)').addClass('sensor-hov'),
              $('.content').addClass('sensor-content-animate')},
    function(){
              $('.sensor-inner').removeClass('sensor-hov'),
              $('.content').removeClass('sensor-content-animate') },
)


function getCoords(elem) { // кроме IE8-
 var box = elem.getBoundingClientRect();

 return {
   top: box.top + pageYOffset,
   left: box.left + pageXOffset,

       height: box.height,
       rect_top: box.top,
   rect_left: box.left,
 };
}

// Позиционировани блока информации о датчике
function PositioningSensorDescr (){
     //Настройки
     var height_transition = 200;//Высота перехода блока с описанием датчика выше блока датчиков(sensors-hero)

     if (window.matchMedia("(max-width: 767.98px)").matches) {
         var under_ident = 30;
         var upper_ident = 150;
       } else {
         var under_ident = 50;
         var upper_ident = 200;
       }
       
     var under_ident = 50;
     var upper_ident = 200;

     const elem = document.querySelector(".sensors-hero");
         const sensors_description_window = document.querySelectorAll(".sensor__description");
     const lastsensor = elem.querySelector('.sensor-inner:nth-last-of-type(2)');

     const maincontent = document.querySelector(".js-content");


     //Коррдината нижней токи самого нижнего датчика
     const lastsensorY = getCoords(lastsensor).top + getCoords(lastsensor).height - getCoords(maincontent).top;
     // Расстояние мужду нижней рамкой последнего сенсора и окном браузера
     const screen_last_sensor = window.innerHeight - getCoords(lastsensor).rect_top - getCoords(lastsensor).height;

     if(screen_last_sensor > height_transition) {
             sensors_description_window.forEach(element => {element.style.top = lastsensorY + under_ident+'px'})
     }
     else {
             sensors_description_window.forEach(element => {
                 const pos_upper = lastsensorY - getCoords(elem).height;
                 element.style.top = pos_upper - upper_ident +'px'})
     }

}


document.querySelector("body").onscroll = function() {PositioningSensorDescr()};
