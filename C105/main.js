function take_snapshot(){
    Webcam.snap(function(data_uri){
        document.getElementById("result").innerHTML='<img id="selfie_img" src="'+data_uri+'"/>';
    });
}
Webcam.set({
    height:300,
    width:350,
    image_format:'png',
    png_quality:90
});
camera=document.getElementById("camera");
Webcam.attach('#camera');
console.log('ml5 version: ',ml5.version);
classifier=ml5.imageClassifier('https://teachablemachine.withgoogle.com/models/G0yrVOEgL/model.json',modelLoaded);
function modelLoaded(){
    console.log("model loaded");
}
function check(){
    img=document.getElementById("selfie_img");
    classifier.classify(img,gotresult);
}
function gotresult(error,result){
    if(error){
        console.error(error);
    }
    else{
        console.log(result);
        document.getElementById("result_object_name").innerHTML=result[0].label;
        document.getElementById("result_object_accuracy").innerHTML=result[0].confidence.toFixed(3);
    }
}