left_wrist_x=0;
right_wrist_x=0;
difference=0;
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
        left_wrist_x=results[0].pose.leftWrist.x;
        right_wrist_x=results[0].pose.rightWrist.x;
        difference=Math.floor(left_wrist_x-right_wrist_x);
    }
}
function draw(){
    background('#4287f5');
    textSize(difference);
    fill('#f90039')
    text("Saakshar Patel",50,300);
}