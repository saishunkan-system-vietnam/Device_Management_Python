$(function() {
  var endpoint = "";
  var loc = window.location;
  var wsStart = "ws://";
  if (loc.protocol == "https:") {
    wsStart = "wss://";
  }
  // endpoint = wsStart + loc.host + loc.pathname
  endpoint = wsStart + loc.host + "/user/";
  console.log(endpoint)
  var socket = new WebSocket(endpoint);

  socket.onmessage = function(e) {
    var userData = JSON.parse(e.data);
    $("#list_user").html(userData.html_users);
  };

  socket.onopen = function(e) {
    console.log("open", e);
  };

  socket.onerror = function(e) {
    console.log("error", e);
  };
  socket.onclose = function(e) {
    console.log("close", e);
  };
});
