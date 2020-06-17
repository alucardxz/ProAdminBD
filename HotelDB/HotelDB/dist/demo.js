// Botones spinners
$(function ($) {
  $('#handleCounter1').handleCounter({
  minimum: 1,
  maximize: 100,
  })
  $('#handleCounter2').handleCounter({
    minimum: 1,
    maximize: 100,
  })
});
//Date
addEventListener('DOMContentLoaded', function () {
  pickmeup('.range', {
	mode : 'range',
  separator: '    a   ',
  position :'bottom',
  format: 'd b-y',
  });
});
//Map
function initMap() {
  var uluru = {lat:  19.735121, lng: -155.014044};
  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 14,
    center: uluru
    });
    var marker = new google.maps.Marker({
      position: uluru,
      map: map
    });
}
//Main
$(document).ready(function() {
  $('.single').slick({
    autoplay : true,
    pauseOnFocus : false,
    pauseOnHover : false,
    arrows : false,
    draggable : false,
  });
  $('.left').click(function(){
    $('.single').slick('slickPrev');
  })
  $('.right').click(function(){
    $('.single').slick('slickNext');
  })
  $('.room').slick({
    autoplay : false,
    slidesToShow :3,
    pauseOnFocus : true,
    arrows : false,
    draggable : true,
    swipeToSlide : true,
  });
  $('.review').slick({
    autoplay : true,
    autoplaySpeed : 6000,
    pauseOnFocus : true,
    pauseOnHover : false,
    arrows : false,
    draggable : true,
  });
});
$(function () {
  $.scrollUp({
    scrollName: 'scrollUp', // Element ID
    topDistance: '600' , // Distance from top before showing element (px)
    topSpeed: 300 , // Speed back to top (ms)
    animation: 'fade', // Fade, slide, none
    animationInSpeed: 500, // Animation in speed (ms)
    animationOutSpeed: 500, // Animation out speed (ms)
    scrollText: '^',
    activeOverlay: false, // Set CSS color to display scrollUp active point, e.g '#00FFFF'
  });
});
