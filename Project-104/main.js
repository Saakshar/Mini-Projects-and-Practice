Webcam.set({
    height:300,
    width:350,
    image_format:'png',
    png_quality:90
});
camera=document.getElementById("camera");
Webcam.attach('#camera');
function take_snapshot(){
    Webcam.snap(function(data_uri){
        document.getElementById("result").innerHTML='<img id="img" src="'+data_uri+'"/>';
    });
}
camera=document.getElementById("camera");
Webcam.attach('#camera');
console.log('ml5 version: ',ml5.version);
classifier=ml5.imageClassifier('https://teachablemachine.withgoogle.com/models/MQrSFqOWl/model.json',modelLoaded);
function modelLoaded(){
    console.log("model loaded");
}