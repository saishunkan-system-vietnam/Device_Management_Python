document.addEventListener('DOMContentLoaded', function () {   
    var endpoint = "";
    var loc = window.location;
    var wsStart = "ws://";
    if (loc.protocol == "https:") {
        wsStart = "wss://";
    }
    endpoint = wsStart + loc.host + "/ws_brand/";

    var socket = new WebSocket(endpoint);

    socket.onmessage = function (e) {
        console.log("messagee",e)
        var res = JSON.parse(e.data);
        document.getElementById("list-brand").innerHTML = res.brand;
    };

    socket.onopen = function (e) {
        console.log("opene", e);
    };    
    socket.onclose = function (e) {
        console.log("closee", e);
    };
})