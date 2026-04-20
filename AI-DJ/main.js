song="";
score_left_wrist=0;
score_right_wrist=0;
left_wrist_x=0;
left_wrist_y=0;
right_wrist_x=0;
right_wrist_y=0;
function setup(){
    canvas=createCanvas(500,500);
    canvas.center();
    video=createCapture(VIDEO);
    video.hide();
    poseNet=ml5.poseNet(video,modelLoaded);
    poseNet.on('pose',gotPoses);
}
function modelLoaded(){
    console.log("posenet has been initialized");
}
function gotPoses(results){
    if(results.length>0){
        console.log(results);
        left_wrist_x=results[0].pose.leftWrist.x;
        left_wrist_y=results[0].pose.leftWrist.y;
        right_wrist_x=results[0].pose.rightWrist.x;
        right_wrist_y=results[0].pose.rightWrist.y;
        score_left_wrist=results[0].pose.keypoints[9].score;
        score_right_wrist=results[0].pose.keypoints[10].score;
        console.log("Score Left Wrist = "+score_left_wrist);
        console.log("Score Right Wrist = "+score_right_wrist);
        console.log("left wrist x="+left_wrist_x+" left wrist y="+left_wrist_y);
        console.log("right wrist x="+right_wrist_x+" right wrist y="+right_wrist_y);
   }
}
function draw(){
    image(video,0,0,500,500);
    fill("#FF0000");
    stroke("#FF0000");
    circle(right_wrist_x,right_wrist_y,20);
    if(score_right_wrist>0.2){
        if(right_wrist_y>0 && right_wrist_y<=100){
            document.getElementbyId("speed_label").innerHTML="Speed=0.5x";
            song.rate(0.5);
        }
        else if(right_wrist_y>100 && right_wrist_y<=200){
            document.getElementbyId("speed_label").innerHTML="Speed=1x";
            song.rate(1);
        }
        else if(right_wrist_y>200 && right_wrist_y<=300){
            document.getElementbyId("speed_label").innerHTML="Speed=1.5x";
            song.rate(1.5);
        }
        else if(right_wrist_y>300 && right_wrist_y<=400){
            document.getElementbyId("speed_label").innerHTML="Speed=2x";
            song.rate(2);
        }
        else if(right_wrist_y>400){
            document.getElementbyId("speed_label").innerHTML="Speed=2.5x";
            song.rate(2.5);
        }
    }
    if(score_left_wrist>0.2){
    circle(left_wrist_x,left_wrist_y,20);
    InNumberLeftWristY=Number(left_wrist_y);
    remove_decimals=floor(InNumberLeftWristY);
    volume=remove_decimals/500;
    document.getElementById("volume_label").innerHTML="Volume="+volume;
    song.setVolume(volume);
    }
}
function preload(){
    song=loadSound("music.mp3");
}
function play(){
    song.play();
    song.setVolume(1);
    song.rate(1);
}