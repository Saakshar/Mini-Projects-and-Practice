status="";
function preload(){
    loadImage("ipad.jpg");
}
function setup(){
    canvas=createCanvas(250,250);
    canvas.center();
    objectDetector=ml5.objectDetector("cocossd",modelLoaded);
    document.getElementById("ipad_status").innerHTML="Detecting Objects";
}
function modelLoaded(){
    status=true;
    objectDetector.detect("cocossd",gotResults);
}
function gotResults(){
    objectDetector.results[0].objectDetector;
}