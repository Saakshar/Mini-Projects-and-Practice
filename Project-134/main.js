status="";
objects=[];
function preload(){
    alarm=loadSound("alarm.wav");
}
function setup(){
    canvas=createCanvas(400,400);;
    canvas.center();
    video=createCapture(VIDEO);
    video.hide();
    video.size(400,400);
    objectDetector=ml5.objectDetector('cocossd',modelLoaded);
    document.getElementById("status").innerHTML="Status: Detecting Baby";
}
function modelLoaded(){
    console.log("model loaded");
    status=true;
}
function gotResult(error,results){
    if(error){
        console.error(error);
    }
    console.log(results);
    objects=results;
}
function draw(){
    image(video,0,0,400,400);
    if(status=="person"){
        objectDetector.detect(video,gotResult);
        for(i=0; i<objects.length; i++){
            text("Baby",objects[i].x,objects[i].y);
            document.getElementById("status").innerHTML="Status: Baby Detected";
            alarm.stop();
        }
    }
    else{
        document.getElementById("status").innerHTML="Status: Baby Not Detected";
        alarm.play();
    }
}