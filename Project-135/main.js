input="";
status="";
objects=[];
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
    if(status=!""){
        for(i=0;i<objects.length;i++){
            confidence=objects[0].confidence;
            percent=floor(confidence*100);
            label=objects[0].label;
            x=objects[0].x;
            y=objects[0].y;
            text(label+" "+percent,x,y);
            fill("#FF0000");
            stroke("FF0000");
            noFill();
            rect(x,y,objects[0].width,objects[0].height);
            if(objects[i].label=input){
                video.stop();
                objectDetector.detect(gotresults);
                document.getElementById("found").innerHTML=input+" Found";
                synth=window.speechSynthesis;
                utterThis=new SpeechSynthesisUtterance(input+" found");
                synth.speak(utterThis);
            }
            else{
                document.getElementById("found").innerHTML=input+" Not Found"
            }
        }
    }
}
function gotresults(error,results){
    if(error){
        console.error(error);
    }
    objects=results;
}