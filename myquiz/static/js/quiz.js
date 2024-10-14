function getName(){
	var login = document.getElementById("login").value;
	alert("Hi, " + login);
	return true;
  }
  
  
  function submitAnswers(answers){
	var total = answers.length;
	var score = 0;
	var choice = [];
  
	for(var i = 1; i <= total; i++){
	  choice[i] = document.forms["quizForm"]["q"+i].value;
	}
  
	for(i = 1; i <= total; i++){
	  if(choice[i] == null || choice[i] == ''){
		alert('you missed question ' + i);
		return false;
	  }
	}
  
	for(i = 1; i <= total; i++){
	  if(choice[i] == answers[i - 1]){
		score++;
	  }
	}
  
	var results = document.getElementById('results');
	results.innerHTML = "<h3>You scored <span>" + score + "</span> out of <span>" + total + "</span></h3>" 
	displayChart(score, total);
	var links = document.getElementById('links');
	links.innerHTML ="<br><h4>You can refer the materials</h4><ul><li><a href='https://www.geeksforgeeks.org/quiz-corner-gq/' target='_blank'>geeksforgeeks</a></li> <li><a href='https://www.tutorialspoint.com/basics_of_computer_science/basics_of_computer_science_online_quiz.htm' target='_blank'>tutorialspoint</a></li></ul>"
  
	alert("You scored " + score + " out of " + total);
	
	return false;
  }
  
  
  function displayChart(score, total) {
    var ctx = document.getElementById('performanceChart').getContext('2d');
    var performanceChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['Correct Answers', 'Wrong Answers'],
            datasets: [{
                label: 'Quiz Performance',
                data: [score, total-score],
				backgroundColor: [
                    'rgba(75, 192, 192, 0.2)',  // Correct Answers (Green)
                    'rgba(255, 99, 132, 0.2)',  // Incorrect Answers (Red)
                    
                ],
                borderColor: [
                    'rgba(75, 192, 192, 1)',    // Correct Answers (Green)
                    'rgba(255, 99, 132, 1)',    // Incorrect Answers (Red)
                    
                ],
                borderWidth: 1
            }]
                
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true,
                    max: total
                }
            }
        }
    });
}

	//set correct answer
	//var answers = ["b", "d", "a", "c", "c"];
	//this variable  is replaced by database answer

	//check answer
	/*
	for(i = 1; i <= total; i++){
		if(eval('q' + i) == answers[i - 1]){
			score++;
		}
	}
	*/
	// new dynamic method 1 for checking answer
		//validation
	/*
	for(i = 1; i <= total; i++){
		if(eval('q'+i) == null || eval('q'+i) == ''){
			alert('you missed question ' + i);
			return false;
		}
	}
	*/
		//getting choices 
	/*
	var q1 = document.forms["quizForm"]["q1"].value;
	var q2 = document.forms["quizForm"]["q2"].value;
	var q3 = document.forms["quizForm"]["q3"].value;
	var q4 = document.forms["quizForm"]["q4"].value;
	var q5 = document.forms["quizForm"]["q5"].value;
*/
//new dynamic method 1


