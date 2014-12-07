$(function() {
	// 将csrf_token 存储的cookie 添加到request header中
	csrfSafeMethod = function(method) {
		// these HTTP methods do not require CSRF protection
		return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
	};
	function getCookie(name) {
		var cookieValue = null;
		if (document.cookie && document.cookie != '') {
			var cookies = document.cookie.split(';');
			for (var i = 0; i < cookies.length; i++) {
				var cookie = jQuery.trim(cookies[i]);
				// Does this cookie string begin with the name we want?
				if (cookie.substring(0, name.length + 1) == (name + '=')) {
					cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
					break;
				}
			}
		}
		return cookieValue;
	}

	var csrftoken = getCookie('csrftoken');

	$('.lyeditor .i2').click(function() {
		$(this).closest('.lyeditor').toggleClass('fullscreen');
	});

	$('.lyeditor .i1').click(function() {
		$(this).closest('.lyeditor').find('.cone').insertContent('<pre class="brush:html;toolbar:false">\r\n//- 代码区\r\n</pre>');
	});

});

