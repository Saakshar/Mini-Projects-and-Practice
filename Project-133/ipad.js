status="";
objects=[];
function preload(){
    img=loadImage("ipad.jpg");
}
function setup(){
    canvas=createCanvas(250,250);
    canvas.center();
    objectDetector=ml5.objectDetector('cocossd',modelLoaded);
    document.getElementById("ipad_status").innerHTML="Detecting Objects";
}
function modelLoaded(){
    status=true;
    objectDetector.detect('cocossd',gotResults);
}
function gotResults(results){
    objectDetector.results[0].objectDetector;
    objects=results;
}
function draw(){
    image(img,0,0,250,250);
    if(status!=""){
        for(i=0;i<objects.length; i++){
            percent=floor(objects[i].confidence*100)+"%";
            text(objects[i].label+""+percent,objects[i].x,objects[i].y);
            rect(objects[i].x,objects[i].y,objects[i].width,objects[i].height);
        }
    }
}