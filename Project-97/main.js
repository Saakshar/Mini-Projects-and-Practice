Number1=0;
Number2=0;
answer=0;
function add(){
    Number1=document.getElementById("Number1").value;
    Number2=document.getElementById("Number2").value;
    answer=MATH.floor(Number1+Number2);
    document.getElementById("output").innerHTML=answer;
    console.log(answer);
}