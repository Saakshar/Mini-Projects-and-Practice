function preload(){

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
        console.log("nose X = "+results[0].pose.nose.x);
        console.log("nose Y = "+results[0].pose.nose.y);
    }
}