var firebaseConfig = {
  apiKey: "AIzaSyAx_VzZ4zAtpoZ-49D3j_amZPBenaRW6jc",
  authDomain: "kwitter-b3e7c.firebaseapp.com",
  databaseURL: "https://kwitter-b3e7c-default-rtdb.firebaseio.com",
  projectId: "kwitter-b3e7c",
  storageBucket: "kwitter-b3e7c.appspot.com",
  messagingSenderId: "921480410552",
  appId: "1:921480410552:web:10c2b50aa401c9d8250b4d"
};

// Initialize Firebase
firebase.initializeApp(firebaseConfig);
    user_name = localStorage.getItem("user_name");
  
  document.getElementById("user_name").innerHTML = "Welcome " + user_name + "!";
  
  function addRoom()
  {
    room_name = document.getElementById("room_name").value;
  
    firebase.database().ref("/").child(room_name).update({
      purpose : "adding room name"
    });
  
      localStorage.setItem("room_name", room_name);
      
      window.location = "kwitter_page.html";
  }
  
  function getData() {  firebase.database().ref("/").on('value', function(snapshot) { document.getElementById("output").innerHTML = ""; snapshot.forEach(function(childSnapshot) { childKey  = childSnapshot.key;
         Room_names = childKey;
         console.log("Room Name - " + Room_names);
        row = "<div class='room_name' id="+Room_names+" onclick='redirectToRoomName(this.id)' >#"+ Room_names +"</div><hr>";
        document.getElementById("output").innerHTML += row;
      });
    });
  
  }
  
  getData();
  
  function redirectToRoomName(name)
  {
    console.log(name);
    localStorage.setItem("room_name", name);
      window.location = "kwitter_page.html";
  }
  
  function logout() {
  localStorage.removeItem("user_name");
  localStorage.removeItem("room_name");
      window.location = "index.html";
  }
  