function addUser(){
    player1Name=document.getElementById("player_1Input").value;
    player2Name=document.getElementById("player_2Input").value;
    localStorage.setItem("player_1Input",player1Name);
    localStorage.setItem("player_2Input",player2Name);
    window.location="game.html";
}