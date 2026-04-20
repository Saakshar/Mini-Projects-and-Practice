function start(){
    navigator.mediaDevices.getUserMedia({audio:true});
    classifier=ml5.soundClassifier('https://teachablemachine.withgoogle.com/models/rO1QK3S7X/model.json',modelReady);
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
        randomNumberR=Math.floor(Math.random()*255)+1;
        randomNumberG=Math.floor(Math.random()*255)+1;
        randomNumberB=Math.floor(Math.random()*255)+1;
        document.getElementById("result_label").innerHTML="I can hear - "+results[0].label;
        document.getElementById("result_confidence").innerHTML="Accuracy - "+(results[0].confidence*100).toFixed(2)+"%";
        document.getElementById("result_label").style.color="rgb("+randomNumberR+","+randomNumberG+","+randomNumberB+")";
        document.getElementById("result_confidence").style.color="rgb("+randomNumberR+","+randomNumberG+","+randomNumberB+")";

        img=document.getElementById("alien1");
        img1=document.getElementById("alien2");
        img2=document.getElementById("alien3");
        img3=document.getElementById("alien4");

        if(results[0].label=="clap"){
            img.src="aliens-01.gif";
            img1.src="aliens-02.png";
            img2.src="aliens-03.png";
            img3.src="aliens-04.png";
        }
        else if(results[0].label=="tap"){
            img.src="aliens-01.png";
            img1.src="aliens-02.gif";
            img2.src="aliens-03.png";
            img3.src="aliens-04.png";
        }
        else if(results[0].label=="bell"){
            img.src="aliens-01.png";
            img1.src="aliens-02.png";
            img2.src="aliens-03.gif";
            img3.src="aliens-04.png";
        }
        else{
            img.src="aliens-01.png";
            img1.src="aliens-02.png";
            img2.src="aliens-03.png";
            img3.src="aliens-04.gif";
        }
    }
}