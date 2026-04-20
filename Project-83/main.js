var mouseEvent="empty";
canvas=document.getElementById("myCanvas");
ctx=canvas.getContext("2d");
color="black";
line_width=1;
canvas.addEventListener("mousedown",myMousedown);
function myMousedown(e){
    color=document.getElementById("color").value;
    line_width=document.getElementById("width").value;
    mouseEvent="mouseDown";
}
canvas.addEventListener("mousemove",myMousemove);
function myMousemove(e){
    currentPositionX=e.clientX-canvas.offsetLeft;
    currentPositionY=e.clientY-canvas.offsetTop;
    if(mouseEvent=="mouseDown"){
        ctx.beginPath();
        ctx.strokeStyle=color;
        ctx.lineWidth=line_width;
        ctx.moveTo(lastPositionX,lastPositionY);
        ctx.lineTo(currentPositionX,currentPositionY);
        ctx.stroke();
    }
    lastPositionX=currentPositionX;
    lastPositionY=currentPositionY;
}
canvas.addEventListener("mouseup",myMouseup);
function myMouseup(e){
    mouseEvent="mouseUp";
}
canvas.addEventListener("mouseleave",myMouseleave);
function myMouseleave(e){
    mouseEvent="mouseleave";
}
canvas.addEventListener("touchstart",myTouchstart);
function myTouchstart(e){
    lastPositionX=e.touches[0].clientX-canvas.offsetLeft;
    lastPositionY=e.touches[0].clientY-canvas.offsetTop;
}
canvas.addEventListener("touchmove",myTouchmove);
function myTouchmove(e){
    currentPositionX=e.touches[0].clientX-canvas.offsetLeft;
    currentPositionY=e.touches[0].clientY-canvas.offsetTop;
    ctx.beginPath();
    ctx.strokeStyle=color;
    ctx.lineWidth=lineWidth;
    ctx.moveTo(lastPositionX,lastPositionY);
    ctx.lineTo(currentPositionX,currentPositionY);
    ctx.stroke();
    lastPositionX=currentPositionX;
    lastPositionY=currentPositionY;
}