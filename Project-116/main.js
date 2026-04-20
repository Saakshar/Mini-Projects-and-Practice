y=0;
x=0;
function preload(){
    filter=loadImage("https://i.postimg.cc/3x3QzSGq/m.png");
}
function setup(){
    canvas=createCanvas(400,400);
    canvas.center();
    video=createCapture(VIDEO);
    video.size(400,400);
    video.hide();
    poseNet=ml5.poseNet(video,modelLoaded);
    poseNet.on('pose',coordinates);
}
function draw(){
    image(video,0,0,400,400);
    image(filter,y,x,50,20);
}
function download(){
    save("mustache.jpg");
}
function modelLoaded(){
    console.log("PoseNet has been activated.")
}
function coordinates(results){
    if(results.length>0){
        console.log(results);
        y=results[0].pose.nose.x-25;
        x=results[0].pose.nose.y;
        console.log("nose X = "+results[0].pose.nose.x);
        console.log("nose Y = "+results[0].pose.nose.y);
    }
}