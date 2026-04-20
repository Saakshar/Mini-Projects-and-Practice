player1Name=localStorage.getItem("player1Name");
player2Name=localStorage.getItem("player2Name");
player1Score=0;
player2Score=0;
document.getElementById("player1Name").innerHTML=player1Name+"  : ";
document.getElementById("player2Name").innerHTML=player2Name+"  : ";
document.getElementById("player1Score").innerHTML=player1Score;
document.getElementById("player2Score").innerHTML=player2Score;
document.getElementById("player_question").innerHTML="Question Turn: "+player1Name;
document.getElementById("player_answer").innerHTML="Answer Turn: "+player2Name;
function send(){
    getWord=document.getElementById("word").value;
    word=getWord.toLowerCase();
    console.log("word in lower case = "+word);

    charAt1=word.charAt(1);
    console.log(charAt1);

    length=Math.floor(word.length/2);
    charAt2=word.charAt(length);
    console.log(charAt2);

    length2=word.length-1;
    charAt3=word.charAt(length2);
    console.log(charAt3);

    remove_charAt1=word.replace(charAt1,"_");
    remove_charAt2=remove_charAt1.replace(charAt2,"_");
    remove_charAt3=remove_charAt2.replace(charAt3,"_");
    console.log(remove_charAt3);

    questionWord="<h4 id='word_display'>Q.   "+remove_charAt3+"</h4>";
    inputBox="<br>Answer : <input type='text' id='inputCheckBox'>";
    checkButton="<br><br><button class='btn btn-info' onclick='check()'>Check</button>";
    row=questionWord+inputBox+checkButton;
    document.getElementById("output").innerHTML=row;
    document.getElementById("word").value="";
}
questionTurn="player1";
answerTurn="player2";
function check(){
    getAnswer=document.getElementById("inputCheckBox").value;
    answer=getAnswer.toLowerCase();
    console.log("answer in lowercase= "+answer);
    if(word==answer){
        if(answerTurn=="player1"){
            player1Score=player1Score+1;
            document.getElementById("player1Score").innerHTML=player1Score;
        }
        else{
            player2Score=player2Score+1;
            document.getElementById("player2Score").innerHTML=player2Score;
        }
    }
    if(questionTurn=="player1"){
        questionTurn="player2";
        document.getElementById("player_question").innerHTML="Question Turn:"+questionTurn;
    }
    else{
        questionTurn="player1";
        document.getElementById("player_question").innerHTML="Question Turn:"+questionTurn;
    }
    if(answerTurn=="player1"){
        answerTurn="player2";
        document.getElementById("player_answer").innerHTML="Answer Turn: "+answerTurn;
    }
    else{
        answerTurn="player1";
        document.getElementById("player_answer").innerHTML="Answer Turn: "+answerTurn;
    }
}