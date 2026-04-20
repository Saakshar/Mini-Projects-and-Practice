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
    image(picture,90,40,300,300);
    fill(255, 0, 0);
  stroke(255, 0, 0);
  circle(50, 50, 80);
  circle(50, 430, 80);
  circle(590, 50, 80);
  circle(590, 430, 80);
  fill(0, 128, 0);
  stroke(0, 128, 0);
  rect(90, 40, 460, 20);
  rect(90, 420, 460, 20);
  rect(40, 90, 20, 300);
  rect(580, 90, 20, 300);
}