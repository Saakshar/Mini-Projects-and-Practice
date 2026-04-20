music_1="";
music_2="";
song_1="";
song_2="";
left_wrist_score=0;
right_wrist_score=0;
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
        left_wrist_score=results[0].pose.keypoints[9].score;
        left_wrist_x=results[0].pose.leftWrist.x;
        left_wrist_y=results[0].pose.leftWrist.y;
        right_wrist_x=results[0].pose.rightWrist.x;
        right_wrist_y=results[0].pose.rightWrist.y;
        right_wrist_score=results[0].keypoints[10].score;
    }
}
function draw(){
    image(video,0,0,400,400);
    fill("FF0000");
    stroke("FF0000")
    song_1=music_1.isPlaying();
    if(left_wrist_score>0.2){
        circle(left_wrist_x,left_wrsit_y,15);
        music_2.stop();
        if(song_1=="false"){
            music_1.play();
            document.getElementById("name").innerHTML="Song 1";
        }
    }
    song_2=music_2.isPlaying();
    if(right_wrist_score>0.2){
        circle(right_wrist_x,right_wrsit_y,15);
        music_1.stop();
        if(song_2=="false"){
            music_2.play();
            document.getElementById("name").innerHTML="Song 2";
        }
    }
}