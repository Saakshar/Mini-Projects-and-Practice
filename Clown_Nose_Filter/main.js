noseX=0;
noseY=0;
function preload(){
    clownNose=loadImage('https://i.postimg.cc/NfvSzb6d/clown-nose-clipart-2.png');
}
function setup(){
    canvas=createCanvas(300,300);
    canvas.center();
    video=createCapture(VIDEO);
    video.size(300,300);
    video.hide();
    poseNet=ml5.poseNet(video,modelLoaded);
    poseNet.on('pose',gotPoses)
}
function modelLoaded(){
    console.log("posenet has been initialized")
}
function gotPoses(results){
    if(results.length>0){
        console.log(results);
        noseX=results[0].pose.nose.x-15;
        noseY=results[0].pose.nose.y-15;
        console.log("nose X = "+results[0].pose.nose.x);
        console.log("nose Y = "+results[0].pose.nose.y);
    }
}
function draw(){
    image(video,0,0,300,300);
    image(clownNose,noseX,noseY,30,30);
}
function takeSnapshot(){
    save("Clown_filter.png");
}