$(function() {
	// 初始化登录名
	initUserName = function(url) {
		$.ajax({
			url : url,
			success : function(data) {
				console.log(data);
				$("#sp_username").text(data);
			},
			error : function(error) {
				console.log(error);
			}
		});
	};
	init = function() {
		initUserName("/common/init_username/");
	};

	//回到顶端
	$("#toTop").scrollToTop(1000);

	init();
	// 设置搜索栏的自动输入
	var options = {
		source : [{
			id : 1,
			name : 'python'
		}, {
			id : 2,
			name : 'django'
		}, {
			id : 3,
			name : 'oracle'
		}, {
			id : 4,
			name : 'mysql'
		}, {
			id : 5,
			name : 'sqlserver'
		}, {
			id : 6,
			name : 'jquery'
		},
		{
			id : 7,
			name : 'bootstrap'
		}, {
			id : 8,
			name : 'SVN'
		}, {
			id : 9,
			name : 'Git'
		},
		{
			id : 10,
			name : '数据结构'
		}
		
		],
		items : 8,
		minLength : 1
	};

	$("#txt_search").typeahead(options);

});
