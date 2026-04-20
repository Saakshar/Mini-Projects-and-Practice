function send(){
    number1=document.getElementById("number1").value;
    number2=document.getElementById("number2").value;
    answer=parseInt(number1)*parseInt(number2);
    question="<h4>"+number1+"X"+number2+"</h4>"
    inputBox="<br>Answer : <input type='text' id='inputCheckBox'>";
    checkButton="<br><br><button class='btn btn-info' onclick='check()'>Check</button>";
    row=question+inputBox+checkButton;
    document.getElementById("output").innerHTML=row;
    document.getElementById("number1").value="";
    document.getElementById("number2").value="";
}
player1Score=0;
player2Score=0;
questionTurn="player1";
answerTurn="player2";
function check(){
    getAnswer=document.getElementById("inputCheckBox").value;
    if(getAnswer==answer){
        if(answerTurn=="player1"){
            player1Score=player1Score+1;
            document.getElementById("score1").innerHTML=player1Score;
        }
        else{
            player2Score=player2Score+1;
            document.getElementById("score2").innerHTML=player2Score;
        }
    }
    if(questionTurn=="player1"){
        questionTurn="player2";
        document.getElementById("question").innerHTML="Question Turn: "+player2Name;
    }
    else{
        questionTurn="player1";
        document.getElementById("question").innerHTML="Question Turn: "+player1Name;
    }
}