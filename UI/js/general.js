function Destination() {

    var name = prompt("Please enter your new destination");
    if (name != null) {
        document.getElementById("destination").innerHTML = name
    }
}

function Location() {

    var name = prompt("Please enter the parcels current location");
    if (name != null) {
        document.getElementById("current").innerHTML = name
    }
}

function Status() {

    var name = prompt("Please enter the parcels current status");
    if (name != null) {
        document.getElementById("status").innerHTML = name
    }
}

function deletes() {
    var txt;
    if (confirm("DO YOU REALLY WANT TO DELETE THIS ORDER")) {
        txt = "ORDER DELETED";
        txts = document.getElementById("demo").innerHTML;
        
    }
}