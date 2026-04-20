var score =0;
function save(){
localStorage.setItem("score", score);
}
function add(){
score=score+1;
document.getElementById("s").innerHTML="Score: "+score;
}
function next(){
    window.location="next.html";
}