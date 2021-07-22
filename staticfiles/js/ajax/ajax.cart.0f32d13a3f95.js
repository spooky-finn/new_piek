import {CartCounter} from './ajax.cart.counter.js';

const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
console.log("csrf_token: "+ csrftoken);

  $(".js-conventional_designation").change(function ()  {
		var elem  = $(this).find('input.input-designation');
		// console.log($(this).find('input.input-designation').val());
    console.log(elem);
		$.ajax({
			headers: { "X-CSRFToken": csrftoken },
			url: elem.attr('dj_url_function'),
			type: 'POST',
			data: {'name': elem.attr('name'),
							'conventional_designation': elem.val()},
			dataType: 'json',
			success: function(data) {
				console.log(data);
				elem.val(data.conventional_designation);
				CartCounter(data);
			}
		});

	});


	$(".btn-quantity").click(function ()  {
		var quantity_box  = $(this).parent().parent().find('form.js-input-integer').children('input.input-integer');
		$.ajax({
			headers: { "X-CSRFToken": csrftoken },
			url: $(this).attr('dj_url_function'),
			type: 'POST',
			data: {'name': $(this).attr('name')},
			dataType: 'json',
			success: function(data) {
				console.log(data);
				quantity_box.val(data.quantity);
				CartCounter(data);
			}
		});
	});

	$(".js-input-integer").change(function ()  {
		var quantity_box  = $(this).find('input.input-integer');
		console.log($(this).find('input.input-integer').val());
		$.ajax({
			headers: { "X-CSRFToken": csrftoken },
			url: quantity_box.attr('dj_url_function'),
			type: 'POST',
			data: {'name': quantity_box.attr('name'),
							'quantity': quantity_box.val()},
			dataType: 'json',
			success: function(data) {
				console.log(data);
				quantity_box.attr('value', data.quantity);
				CartCounter(data);
			}
		});

	});

	$(".btn-delete").click(function ()  {
		var parent = $(this).parent().parent();
		console.log($(this).attr('dj_url_function'));
		$.ajax({
			headers: { "X-CSRFToken": csrftoken },
			url: $(this).attr('dj_url_function'),
			type: 'POST',
			dataType: 'json',
			success: function(data) {
				parent.remove();
			  CartCounter(data);

			}
		});
	});

	$(".js-btn-delete-mobile ").click(function ()  {
		var parent = $(this).parent().parent().parent();
		console.log(parent);
		console.log($(this).attr('dj_url_function'));
		$.ajax({
			headers: { "X-CSRFToken": csrftoken },
			url: $(this).attr('dj_url_function'),
			type: 'POST',
			dataType: 'json',
			success: function(data) {
				parent.remove();
			CartCounter(data);
			}
		});
	});
