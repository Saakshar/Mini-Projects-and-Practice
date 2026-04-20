webcam.set({
    width: 500,
    height: 400,
    image_format: png,
    png_quality: 100
});
camera=document.getElementById("webcam");
webcam.attach('#webcam');
function takePicture(){
    webcam.snap(function(data_uri){
        document.getElementById("output").innerHTML='<img id="image" src="'+data_uri+'">';
    });
}
console.log('ml5 version: ',ml5.version);
classifier=ml5.imageClassifier('https://teachablemachine.withgoogle.com/models/O7xUfryle/model.json');