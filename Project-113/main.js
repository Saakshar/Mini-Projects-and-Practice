function takePicture(){
    save('image.jpg');
}
function setup(){
    canvas=createCanvas(600,400);
    canvas.position(200,200);
    picture=createCapture(VIDEO);
    picture.hide();
}
function draw(){
    image(picture,0,0,400,400);
}