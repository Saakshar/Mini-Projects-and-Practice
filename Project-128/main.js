music_1="";
music_2="";
left_wrist_x=0;
left_wrist_y=0;
right_wrist_x=0;
right_wrsit_y=0;
function preload(){
    music_1=loadSound("music.mp3");
    music_2=loadSound("music2.mp3");
}
function setup(){
    canvas=createCanvas(400,400);
    canvas.center();
    video=createCapture(VIDEO);
    video.hide();
    poseNet=ml5.poseNet(video,modelLoaded);
    poseNet.on('pose',gotPoses);
}
function modelLoaded(){
    console.log("posenet has loaded");
}
function gotPoses(results){
    if(results.length>0){
        left_wrist_x=results[0].pose.leftWrist.x;
        left_wrist_y=results[0].pose.leftWrist.y;
        right_wrist_x=results[0].pose.rightWrist.x;
        right_wrist_y=results[0].pose.rightWrist.y;
    }
}
function draw(){
    image(video,0,0,400,400);
}