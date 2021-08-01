/* Активный пункт меню */

$(document).ready(function(){
	var a = window.location.href;
	a = a.split("/");
	a = a[3];
	if (a == '') {
		$('ul.navbar-nav li a:first').addClass('active');
	} else {
		/*$('ul.navbar-nav li a').each(function(){
			var text = $(this).attr('href');
			text = text.split('/');
			for(var i=0; i < text.length; i++){
				if (text[i] == a) {
					$(this).addClass('active');
				}
			}
		}); */
	}
	var b = window.location.href;
	var c;
	$('.tp-category-widget ul li a').each(function(){
		c=$(this).attr('href');
		if (c == b) {
			$(this).addClass('active');
			var d = $(this).html();
			$(this).replaceWith('<span class="active">'+d+'</span>');
		}
	})
	$('.collapse').each(function(){
		var e = $(this).attr('id');
		if ($(this).find('span.active').text() != '') {
			e='#'+e;
			$(e).collapse()
		}
	})
	
	$('.my_collapse').each(function(){
		$(this).addClass('collapsed');
	});
});