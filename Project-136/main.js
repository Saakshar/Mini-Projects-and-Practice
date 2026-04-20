input="";
status="";
function setup(){
    canvas=createCanvas(380,380);
    canvas.center();
    video=createCapture(VIDEO);
    video.hide();
    video.size(380,380);
}
function start(){
    objectDetector=ml5.objectDetector('cocossd',modelLoaded);
    document.getElementById("status").innerHTML="Status:Detecting Objects";
    input=document.getElementById("input").innerHTML;
}
function modelLoaded(){
    console.log("Model Loaded");
    status=true;
}
function draw(){
    image(video,0,0,380,380);
}