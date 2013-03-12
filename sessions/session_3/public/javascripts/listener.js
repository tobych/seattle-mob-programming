$().ready(function() {

  var socket = io.connect('http://localhost');
  socket.on('message', function (data) {
    $("#joke").append(data + "<br/>");
    $("#jokes").scrollTop($("#jokes")[0].scrollHeight);
  });

  $("#jokeform").submit(function(e) {
    //$("#joke").html($("#writejokes").val());
    socket.send($("#writejokes").val());
    $("#writejokes").val("");
    return false;
  });
});