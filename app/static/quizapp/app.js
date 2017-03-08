$(document).ready(function(){

	// Check FB Login Status
	FB.getLoginStatus(function(response) {
    	statusChangeCallback(response);
	});
/* prepare for csrf token*/
	var csrftoken = $('meta[name=csrf-token]').attr('content');

	$.ajaxSetup({
	    beforeSend: function(xhr, settings) {
	        if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
	            xhr.setRequestHeader("X-CSRFToken", csrftoken);
	        }
	    }
	})

	/*

		var response = {
		"answers": [
			{
			"id": 3,
			"answer": true,
			"altAnswerId": 23
			},
			{
			"id": 3,
			"answer": true,
			"altAnswerId": 23
			}
		],
		"metadata": {
			"language": "EN",
			"country": "Switzerland"
		}
	};
	*/
	var numberOfQuestionsPairs = 0;
	var numberOfQuestionsPairsCounter = 0;
	var questions = [];

	var result = {
					"answers":[],
					"metadata":{}
	};

	function generateQuestion(questionsPair){
		$('.question-wrapper').append('<div class="row decision-wrapper" data-id1="'+ questionsPair[0].questionId +'" data-id2="'+ questionsPair[1].questionId +'"><div class="col-md-5 option-wrapper" data-id="'+ questionsPair[0].questionId +'" >'+ questionsPair[0].questionText +'</div><div class="col-md-2" style="padding-top: 20px;">OR</div><div class="col-md-5 option-wrapper" data-id="'+ questionsPair[1].questionId +'" >'+ questionsPair[1].questionText +'</div></div>');
	}


	$(document).on('click', '.option-wrapper', function(){

		var getId1 =  $( ".decision-wrapper" ).data('id1');
		var getId2 =  $( ".decision-wrapper" ).data('id2');
		console.log("ID1"+getId1);
		console.log("ID2"+getId2);


		var clickedId = $(this).data('id');
		if(getId1 === clickedId) {
			question1status = true;
		} else {
			question1status = false;
		}
		if(getId2 === clickedId) {
			question2status = true;
		} else {
			question2status = false;
		}



		var notClickedId = $(this).data('id');
		console.log(notClickedId);

		// get question 1
		var answer = {"questionId": getId1, "questionText": question1status, "altAnswerId": getId2};
		result.answers.push({answer});

		// get question 2
		var answer = {"questionId": getId2, "questionText": question2status, "altAnswerId": getId1};
		result.answers.push({answer});

		$('.decision-wrapper').remove();



    	if(numberOfQuestionsPairsCounter<numberOfQuestionsPairs){
   			generateQuestion(questions["questions"][numberOfQuestionsPairsCounter]);
   			numberOfQuestionsPairsCounter++;
   		} else {
			//POST Request here
			result.metadata["lang"]="de";
			result.metadata["country"]="Switzerland";
			console.log( JSON.stringify(result));

			var answers = result;
			$.post( "http://quiz.needseeker.io/postanswer", function( answers ) {
				console.log("successful post");
				$('.question-div').remove();
				$('.decision-wrapper').remove();
				$('.question-wrapper').append('<div class="row"><div class="col-md-12 congrats-title">Congratulation!</div>');
				$('.question-wrapper').append('<div class="row"><div class="col-md-12 "><img src="./img/badgeimage2.png"></div>');
				$('.question-wrapper').append('<div class="row"><div class="col-md-12 share-botton"><img src="./img/s_fb_button.png"></div>');
			});

		}
	});


	$(document).on('click', '.starttestbutton', function(){

		$.get( "http://quiz.needseeker.io/getquestion", function( data ) {
		 console.log(data);
		 questions = JSON.parse(data);



		  /*
			questions = {
				"questions": [
								[
									{
										"questionId": "23",
										"questionDescription":"Self-Driving"
									},
									{
										"questionId": "25",
										"questionDescription":"Flying Car"
									}
								],
								[

									{
										"questionId": "31",
										"questionDescription": "Fast Car"
									},
									{
										"questionId": "32",
										"questionDescription": "Slow Car"
									}
								]
							]

			};*/






			numberOfQuestionsPairs = questions["questions"].length;
			console.log("length:" + numberOfQuestionsPairs);

			generateQuestion(questions["questions"][numberOfQuestionsPairsCounter]);
			numberOfQuestionsPairsCounter++;
	    	$('.start-wrapper').hide();
	    	$('.question-wrapper').show();
			});

    });

});