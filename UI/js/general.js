function Destination() {

    var name = prompt("Please enter your new destination");
    if (name != null) {
        document.getElementById("des").innerHTML = name
    }
}

function deletes() {
    var txt;
    if (confirm("DO YOU REALLY WANT TO DELETE THIS ORDER")) {
        txt = "ORDER DELETED";

    } else {
        txt = "You pressed Cancel!";
    }

    function dis() {

    }
    document.getElementById("demo").innerHTML = txt;
}

document.getElementById("date").innerHTML = Date();

    function myFunction() {

        var use = document.getElementById("username");
        document.getElementById("loc").innerHTML = use.value;

                var ko = document.getElementById("sil");
                document.getElementById("fly").innerHTML = ko.value;

            }

        function Location() {
            var x;
            var name = prompt("Please enter the parcel's current location");
            if (name != null) {
                document.getElementById("current").innerHTML = name
            }
        }

        function Status() {
            var x;
            var name = prompt("Please enter the parcel's status");
            if (name != null) {
                document.getElementById("status").innerHTML = name
            }
        }

        function deletes() {
            var txt;
            if (confirm("DO YOU REALLY WANT TO DELETE THIS ORDER")) {
                txt = "ORDER DELETED";

            } else {
                txt = "You pressed Cancel!";
            }

            function dis() {

            }
            document.getElementById("demo").innerHTML = txt;
        }
   

        