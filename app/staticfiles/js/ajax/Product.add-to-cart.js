import {CartCounter} from './ajax.cart.counter.js';
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

$(".js-cart-buttons").click(function ()  {
	$.ajax({
		headers: { "X-CSRFToken": csrftoken },
		url: $(this).attr('add-to-cart-url'),
		type: 'POST',
		dataType: 'json',
		success: function(data) {
      CartCounter(data);
		}
	});
});
