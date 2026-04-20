var canvas=new fabric.Canvas("myCanvas");
playerX=10;
playerY=10;
blockImgHeight=30;
blockImgWidth=30;
var player_object="";
var block_img_object="";
function player_update(){
    fabric.Image.fromURL("player.png", function(Img){
        player_object=Img;
        player_object.scaleToWidth(150);
        player_object.scaleToHeight(140);
        player_object.set({
            top:playerY,left:playerX
        });
        canvas.add(player_object);
    });
}
function newImage(getImage){
    fabric.Image.fromURL(getImage, function(Img){
        block_img_object=Img;
        block_img_object.scaleToWidth(blockImgWidth);
        block_img_object.scaleToHeight(blockImgHeight);
        block_img_object.set({
            top:playerY,left:playerX
        });
        canvas.add(block_img_object);
    });
}
window.addEventListener("keydown",keydown);
function keydown(e){
    keyPressed=e.keyCode;
    console.log("keypressed");
    if(keyPressed==88 && e.shiftKey==true){
        console.log("shift-x");
        blockImgHeight=blockImgHeight-10;
        blockImgWidth=blockImgWidth-10;
        document.getElementById("width").innerHTML=blockImgWidth;
        document.getElementById("height").innerHTML=blockImgHeight;
    }
    if(keyPressed==90 && e.shiftKey==true){
        console.log("shift-z");
        blockImgHeight=blockImgHeight+10;
        blockImgWidth=blockImgWidth+10;
        document.getElementById("width").innerHTML=blockImgWidth;
        document.getElementById("height").innerHTML=blockImgHeight;
    }
    if (keyPressed=='38'){
        up();
        console.log("up");
    }
    if (keyPressed=='40'){
        down();
        console.log("down");
    }
    if (keyPressed=='37'){
        left();
        console.log("left");
    }
    if (keyPressed=='39'){
        right();
        console.log("right");
    }
    if(keyPressed=='76'){
        newImage('light_green.png');
        console.log("l");
    }
    if(keyPressed=='68'){
        newImage('dark_green.jpg');
        console.log("d");
    }
    if(keyPressed=='84'){
        newImage('trunk.jpg');
        console.log("t");
    }
    if(keyPressed=='71'){
        newImage('ground.png');
        console.log("g");
    }
    if(keyPressed=='87'){
        newImage('wall.jpg');
        console.log("w");
    }
    if(keyPressed=='89'){
        newImage('yellow_wall.png');
        console.log("y");
    }
    if(keyPressed=='82'){
        newImage('roof.jpg');
        console.log("r");
    }
    if(keyPressed=='67'){
        newImage('cloud.jpg');
        console.log("c");
    }
    if(keyPressed=='85'){
        newImage('unique.png');
        console.log("u");
    }
}
function up(){
	if(playerY>=0){
		playerY=playerY-blockImgHeight;
		console.log("the x coordinates for the player is "+playerX+" and the y coordinates for the player is "+playerY);
		console.log("y=y-"+blockImgHeight);
        canvas.remove(player_object);
		player_update();
	}
}
function down(){
    if(playerY<=500){
        playerY=playerY+blockImgHeight;
        console.log("the x coordinates for the player is "+playerX+" and the y coordinates for the playes is "+playerY);
        console.log("y=y+"+blockImgHeight);
        canvas.remove(player_object);
        player_update();
    }
}
function left(){
    if(playerX>=0){
        playerX=playerX-blockImgHeight;
        console.log("the x coordinates for the player is "+playerX+" and the y coordinates for the player is "+playerY);
        console.log("x=x-"+blockImgHeight);
        canvas.remove(player_object);
        player_update();
    }
}
function right(){
    if(playerX<=850){
        playerX=playerX+blockImgHeight;
        console.log("the x coordinates for the player is "+playerX+" and the y coordinates for the player is "+playerY);
        console.log("x=x+"+blockImgHeight);
        canvas.remove(player_object);
        player_update();
    }
}