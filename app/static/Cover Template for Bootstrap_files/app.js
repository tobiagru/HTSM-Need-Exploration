

$(document).ready(function(){

		

	

	/*
	var question1 = {option1: "Self-Driving Car", option2: "Swimming Car"};
	var question2 = {option1: "BMW Car", option2: "Tesla Car"};
	var question3 = {option1: "Gasoline Car", option2: "Electric Car"};
	var question4 = {option1: "Fast Car", option2: "Safe Car"};

	var questions = [question1, question2, question3, question4];
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
console.log("here");
		

    	if(numberOfQuestionsPairsCounter<numberOfQuestionsPairs){
    		

   			generateQuestion(questions[numberOfQuestionsPairsCounter]);
   			numberOfQuestionsPairsCounter++;
   		} else {
			//POST Request here
			result.metadata["lang"]="de";
			result.metadata["country"]="Switzerland";
			console.log(result);
			$('.question-div').remove();
			$('.decision-wrapper').remove();
			$('.question-wrapper').append('<div class="row"><div class="col-md-12 congrats-title">Congratulation!</div>');
			$('.question-wrapper').append('<div class="row"><div class="col-md-12 "><img src="./img/badgeimage2.png"></div>');
			$('.question-wrapper').append('<div class="row"><div class="col-md-12 share-botton"><img src="./img/s_fb_button.png"></div>');
		}
	}); 


	$(document).on('click', '.starttestbutton', function(){ 

		$.get( "http://www.needseeker.io/getquestion", function( data ) {
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