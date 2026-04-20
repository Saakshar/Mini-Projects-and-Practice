Webcam.set({
    width: 500,
    height: 400,
    image_format: 'png',
    png_quality: 100
});
camera=document.getElementById("webcam");
Webcam.attach('#webcam');
function takePicture(){
    Webcam.snap(function(data_uri){
        document.getElementById("output").innerHTML='<img id="image" src="'+data_uri+'">';
    });
}
console.log('ml5 version: ',ml5.version);
classifier=ml5.imageClassifier('https://teachablemachine.withgoogle.com/models/O7xUfryle/model.json');
function identify(){
    image=document.getElementById('image');
    classifier.classify(image,gotResult);
}
function gotResult(error,results){
    if(error){
        console.error(error);
    }    
    else{
        console.log(results);
        document.getElementById("name").innerHTML=results[0].label;
        document.getElementById("accuracy").innerHTML=results[0];
        speak();
        if(results[0].label=="Best"){
            document.getElementById("icon").innerHTML="&#128077;";
        }
        if(results[0].label=="Victory"){
            document.getElementById("icon").innerHTML="&#9996;";
        }
        if(results[0].label=="Amazing"){
            document.getElementById("icon").innerHTML="&#128076;";
        }
    }
}
function speak(){
    var speech=window.speechSynthesis();
    var speak=new speachSynthesisUtterance("The hand gesture is "+results[0].label);
    speech.speak(speak);
}