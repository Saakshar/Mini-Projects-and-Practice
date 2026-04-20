function adduser(){
    player1Name=document.getElementById("input1").value;
    player2Name=document.getElementById("input2").value;
    localStorage.setItem("input1",player1Name);
    localStorage.setItem("input2",player2Name);
    window.location="game.html";
}