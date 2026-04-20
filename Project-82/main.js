var mouseEvent="empty";
var canvas=document.getElementById("myCanvas");
ctx=canvas.getContext("2d");
color="black";
line_width=1;
radius=20;
canvas.addEventListener("mousedown",myMousedown);
function myMousedown(e){
    color=document.getElementById("color").value;
    line_width=document.getElementById("width").value;
    radius=document.getElementById("radius").value;
    mouseEvent="mouseDown";
}
canvas.addEventListener("mousemove",myMousemove);
function myMousemove(e){
    currentPositionX=e.clientX-canvas.offsetLeft;
    currentPositionY=e.clientY-canvas.offsetTop;
    if(mouseEvent=="mouseDown"){
        console.log("current position of X and Y coordinates = ");
        console.log("X= "+currentPositionX+" and Y= "+currentPositionY);
        ctx.beginPath();
        ctx.strokeStyle=color;
        ctx.lineWidth=width;
        ctx.arc(currentPositionX,currentPositionY,radius,0,2*Math.PI);
        ctx.stroke();
    }
}
canvas.addEventListener("mouseup",myMouseup);
function myMouseup(e){
    mouseEvent="mouseUp";
}
canvas.addEventListener("mouseleave",myMouseleave);
function myMouseleave(e){
    mouseEvent="mouseleave";
}