function record(){
    navigator.mediaDevices.getUserMedia({audio:true});
    classifier=ml5.soundClassifier('https://teachablemachine.withgoogle.com/models/EpnCOeYGe/model.json',modelReady);
}
function modelReady(){
    classifier.classify(gotResults);
}
function gotResults(error,results){
    if(error){
        console.error(error);
    }
    else{
        console.log(results);
        red=Math.floor(Math.random()*255)+1;
        blue=Math.floor(Math.random()*255)+1;
        green=Math.floor(Math.random()*255)+1;
        document.getElementById("num_of_times").innerHTML="Was Shown "+(dog,cat,cow,bird)+" Times";
        document.getElementById("animal_name").innerHTML="Animal Noise: "+results[0].label;
        document.getElementById("num_of_times").style.color="rgb("+red+","+green+","+blue+")";
        document.getElementById("animal_name").style.color="rgb("+red+","+green+","+blue+")";
        image=document.getElementById("animal_image");
        if(results[0].label=="Bird"){
            image.src="bird.jpg";
        }
        else if(results[0].label=="Dog"){
            image.src="dog.jpg";
        }
        else if(results[0].label=="Cat"){
            image.src="cat.jpg";
        }
        else if(results[0].label=="Cow"){
            image.src="cow.jpg";
        }
        else{
            image="default.png";
        }
    }
}
dog=0;
cat=0;
cow=0;
bird=0;