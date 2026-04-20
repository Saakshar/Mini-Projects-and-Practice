function setup(){
    video=createCapture(VIDEO);
    video.size(400,400);
    canvas=createCanvas(400,400);
    canvas.position(410,130);
    poseNet=ml5.poseNet(video,modelLoaded);
    poseNet.on('pose',gotPoses);
}
function modelLoaded(){
    console.log("PoseNet has been initialized");
}
function gotPoses(results){
    if(results.length>0){
        console.log(results);
    }
}
function draw(){
    background('#4287f5');
}