
    function myFunction(){
    
    var name=prompt("Please enter your new destination");
    if (name!=null){
        document.getElementById("des").innerHTML =name
   }
}

function deletes(){
    var txt;
    if (confirm("DO YOU REALLY WANT TO DELETE THIS ORDER")) {
        txt = "ORDER DELETED";
       
    } else {
        txt = "You pressed Cancel!";
    }
    function dis(){

    }
    document.getElementById("demo").innerHTML = txt;
} 
