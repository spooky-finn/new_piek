import {CartCounter} from './ajax.cart.counter.js';
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
$("#js-cart-button").click(function ()  {
	var quantity = $(this).parent().parent().find('input#js-quantity-field').val();
	console.log(quantity);
	$.ajax({
		headers: { "X-CSRFToken": csrftoken },
		url: $(this).parent().parent().attr('add-to-cart-url'),
		type: 'POST',
		dataType: 'json',
		data: {'quantity': quantity},
		success: function(data) {
			CartCounter(data);
		}
	});
});
