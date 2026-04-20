status="";
objects=[];
function setup(){
    canvas=createCanvas(400,400);;
    canvas.center();
    video=createCapture(VIDEO);
    video.hide();
    video.size(400,400);
    objectDetector=ml5.objectDetector('cocossd',modelLoaded);
    document.getElementById("status").innerHTML="Status: Detecting Objects";
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
    if(status!=""){
        r=random(255);
        b=random(255);
        g=random(255);
        objectDetector.detect(video,gotResult);
        for(i=0; i<objects.length; i++){
            document.getElementById("status").innerHTML="Status: Object Detected";
            document.getElementById("amount").innerHTML="The number of objects detected are "+objects.length;
            fill(r,g,b);
            percent=floor(objects[i].confidence*100);
            text(objects[i].label+" "+percent+"%",objects[i].x,objects[i].y);
            noFill();
            stroke(r,g,b);
            rect(objects[i].x,objects[i].y,objects[i].width,objects[i].height);
        }
    }
}