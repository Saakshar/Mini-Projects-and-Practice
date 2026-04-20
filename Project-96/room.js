// Your web app's Firebase configuration
var firebaseConfig = {
    apiKey: "AIzaSyCHSGR4s-m2Uxowb76ymqZpyLqiDU9aZXE",
    authDomain: "project-94-4296a.firebaseapp.com",
    databaseURL: "https://project-94-4296a-default-rtdb.firebaseio.com",
    projectId: "project-94-4296a",
    storageBucket: "project-94-4296a.appspot.com",
    messagingSenderId: "6493391005",
    appId: "1:6493391005:web:8c2e591241c5b04c686c74"
  };
  // Initialize Firebase
  firebase.initializeApp(firebaseConfig);
  username = localStorage.getItem("user_name");
document.getElementById("name").innerHTML="Welcome "+username+"!";
function add_room(){
      roomname=document.getElementById("room").value;
      firebase.database().ref("/").child(roomname).update({
            purpose: "adding room name"
      });
      localStorage.setItem("room_name",roomname);
      window.location("kwitter_page.html");
}
function getData(){
      firebase.database().ref("/").on('value',function(snapshot){
          document.getElementById("output").innerHTML="";
          snapshot.forEach(function(childSnapshot){
                childKey=childSnapshot.key;
                roomnames=childKey;
                console.log("room name: "+roomname);
                row="<div class='roomname' id="+roomnames+" onclick='redirectToRoomName(this.id)'>#"+roomname+"</div><hr>";
                document.getElementById("output").innerHTML+=row;
          });
      });
}
getData();
function redirectToRoomName(name){
      console.log(name);
      localStorage.setItem("room_name",name);
      window.location("kwitter_page.html");
}
function getData(){
      firebase.database().ref("/").on('value',function(snapshot){
          document.getElementById("output").innerHTML="";
          snapshot.forEach(function(childSnapshot){
                childKey=childSnapshot.key;
                roomnames=childKey;
                console.log("room name: "+roomname);
                row="<div class='roomname' id="+roomnames+" onclick='redirectToRoomName(this.id)'>#"+roomname+"</div><hr>";
                document.getElementById("output").innerHTML+=row;
          });
      });
}
getData();
function redirectToRoomName(name){
      console.log(name);
      localStorage.setItem("room_name",name);
      window.location="kwitter_page.html";
}
function logout(){
      localStorage.removeItem("user_name");
      localStorage.removeItem("room_name");
      window.location="login.html";
}