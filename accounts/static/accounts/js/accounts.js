/**
 * @author wangxin
 */
$(function(){
	
	send_mail = function(){
		$("#send_fail").attr("style" , "display:none") ;
		$("#sending_mail").attr("style" , "display:block") ;
		url = "/accounts/sendmail/" ; 
		$.ajax({
			url : url ,
			success : function(data){
				$("#sending_mail").attr("style" , "display:none") ;
				if(data == "True"){
					$("#send_success").attr("style" , "display:inline") ;
					$("#send_fail_two").attr("style" , "display:none") ;
				}else{
					$("#send_success").attr("style" , "display:none") ;
					$("#send_fail").attr("style" , "display:none") ;
					$("#send_fail_two").attr("style" , "display:block") ;
				}
			},
			error : function(error){
				console.log(error);
				$("#send_success").attr("style" , "display:none") ;
				$("#send_fail").attr("style" , "display:none") ;
				$("#send_fail_two").attr("style" , "display:block") ;
			}
			
		});
	};
	
	
	
	
	
	
});
