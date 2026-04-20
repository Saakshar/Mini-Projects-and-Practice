function back(){
    window.location="index.html";
}
function get(){
    score2=localStorage.getItem("score");
    document.getElementById("s2").innerHTML="Score: "+score2;
}