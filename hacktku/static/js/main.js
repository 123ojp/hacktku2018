var score = 0;
var question = {};
var resqmsg = {};
var respmsg = {};
var wsocket = new WebSocket("ws://127.0.0.1:8080/chat");
var currentQ = 0;
var maxques = 5;
var inte;

function setmsg(attr, value){
	resqmsg[attr] = value;
}

function sent(){
	wsocket.send(JSON.stringify(resqmsg));
}

$(document).ready(function(){
	$(".Question_page").each(function(index,item){
		$(item).hide();
	});
	$("#again_btn").click(function(){
		location.reload();
	});
	$("#start_btn").hide();
	$("#score").hide();
	$("#teamate_2").hide()
	$("#loading_gif").hide();
	$("#loading_h3").hide();
	$("#end_page").hide();
});

$("#find_btn").click(function(){
	$("#find_btn").hide();
	setmsg("nickname", nickname);//暱稱放這裡
	setmsg("msg_type", "hello");
	sent();
	$("#loading_gif").show();
	$("#loading_h3").show();
	inte = setInterval(function(){
		setmsg("msg_type", "waiting_fight");
		sent();
	}, 1000);
});

wsocket.onmessage = function(e){
	respmsg = JSON.parse(e.data);
	var type = respmsg.msg_type;

	if(type == "waiting_respon"){
		if(respmsg.people){
			clearInterval(inte);
			$("#teamate_2").show();
			$("#teamate_").text(respmsg.teamate);
			setteam(respmsg.teamate);
			$("#loading_gif").hide();
			$("#loading_h3").hide();
			$("#start_btn").show();
			$("#start_btn").click(function(){
				setmsg("msg_type", "start_ques");
				sent();
				$("#start_div").hide();
				$("#score").show();
				$("#Q1").show();
			});
		}
	}
	else if(type == "question"){
		var decode = decodeURIComponent(respmsg.question);
		if(decode[0] != "["){
			decode = "\'" + decode + "\'";
		}
		decode = "var respQuestion = " + decode;
		eval(decode);
		if(Array.isArray(respQuestion)){
			$("#Q1_form input").show();
			$("#q1_q").hide();
			$("#Q1_form input").each(function(index){
				$(this).prop("value", respQuestion[index]);
				$(this).unbind();
				$(this).click(function(){
					$(this).unbind();
					setmsg("msg_type", "answer");
					setmsg("answer", index + 1);
					sent();
				});
			});
		}
		else{
			$("#q1_q").text(respQuestion);
			$("#Q1_form").hide();
			$("#q1_q").show();
		}
	}
	else if(type == "answer_respon"){
		currentQ++;
		if(currentQ >= maxques){
			$("#Q1").hide();
			$("#score").hide();
			$("#end_page").show();
			setTimeout(function(){
				setmsg("msg_type", "over_question");
				sent();
			}, 2000);
		}
		else{
			setTimeout(function(){
				setmsg("msg_type", "start_ques");
				sent();
			}, 2000);
		}
		if(respmsg.correct){
			alertify.success("恭喜答對");

		}
		else{
			alertify.error("答錯了");
		}
		score = respmsg.score;
		$("#score_span").text(score);
		$("#final_score").text(score);
	}
}

var timmerr = new Vue({
    el:"#app",
    data:{
        time:60,
        initial:60,
        started:false
    }
})

function setteam(id) {
	$.ajax({
    url:"http://127.0.0.1:8000/api/userprofile/"+id+"/?format=json",
    success:function(result){
    	$("#teamate_").text(result['first_name']);}
});
}
/*
$("#Q1").hide();
$("#timer").hide();
$("#score").hide();
$("#end_page_time").show();
final_score_post();
$("#final_score_time").text(score);
*/
