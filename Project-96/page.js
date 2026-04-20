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
  firebase.initializeApp(firebaseConfig)
function getData() { firebase.database().ref("/"+room_name).on('value', function(snapshot) { document.getElementById("output").innerHTML = ""; snapshot.forEach(function(childSnapshot) { childKey  = childSnapshot.key; childData = childSnapshot.val(); if(childKey != "purpose") {
    firebase_message_id = childKey;
    message_data = childData;
    
 } });  }); }
getData();
function send(){
msg=document.getElementById("msg").value;
firebase.database().ref(roomname).push({
   name: username,
   message: msg,
   like: 0
});
document.getElementById("msg").value="";
}