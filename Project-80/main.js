guest_list=[];
function submit(){
    var guest_name=document.getElementById("name").value;
    guest_list.push(guest_name);
    document.getElementById("submit_display").innerHTML=guest_list;
    console.log(guest_list);
}
function sort(){
    guest_list.sort();
    document.getElementById("sort_display").innerHTML=guest_list;
    console.log(guest_list);
}
function search(){
    var s=document.getElementById("find_name").value;
    var found=0;
    var j;
    for(j=0; j<guest_list.length; j++){
        if(s==guest_list[j]){
            found=found+1;
        }
    }
    document.getElementById("search_display").innerHTML="name found "+found+" time/s";
    console.log("name found "+found+" time/s");
}