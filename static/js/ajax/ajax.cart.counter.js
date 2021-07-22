// used for update count req circle at the header
function CartCounter(data){
  $('#js-cart-counter').html(data.in_cart_counter);
  $('#js-mobile-cart-counter').html(data.in_cart_counter);
  $('#js-in-cart-counter').html(data.in_cart_counter);
    if ((document.getElementById('js-cart-counter').textContent || document.getElementById('js-cart-counter').innerText) ==0){document.getElementById('js-cart-counter-wrap').style.display = "none";}else{document.getElementById('js-cart-counter-wrap').style.display = "inline";};
    if ((document.getElementById('js-mobile-cart-counter').textContent || document.getElementById('js-mobile-cart-counter').innerText) ==0){document.getElementById('js-mobile-cart-counter-wrap').style.display = "none";}else{document.getElementById('js-mobile-cart-counter-wrap').style.display = "inline";}
}
console.log("cart_counter_uploaded");

export {CartCounter};
