#!/bin/sh

curl -i http://quiz.needseeker.io/getquestion -H "Content-Type: application/json" -X GET
curl -i http://quiz.needseeker.io/postanswer -H "Content-Type: application/json" -X POST -d '{"answers":[{"answer":{"questionId":38,"answerValue":true,"altAsnwerId":34}},{"answer":{"questionId":34,"answerValue":false,"altAsnwerId":38}}],"metadata":[{"key":"lang",:"value":"DE"},{"key":"country","value":"Switzerland"}]}'