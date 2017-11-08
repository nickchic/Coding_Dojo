
var express = require("express");
var path = require("path");
var app = express();

app.use(express.static(path.join(__dirname, "./static")));
app.set('views', path.join(__dirname, './views'));
app.set('view engine', 'ejs');

var server = app.listen(8000, function() {
    console.log("listening on port 8000");
});
var io = require('socket.io').listen(server);

app.get('/', function(request, response) {
    response.render("index");
})

io.sockets.on('connection', function (socket) {
    console.log("Client/socket is connected!");
    console.log("Client/socket id is: ", socket.id);

    socket.on( "button_clicked", function (data){
        console.log( 'Someone clicked a button!  Reason: '  + data.reason);
        io.emit( 'server_response', {response:  "sockets are the best!"});
    })

    socket.on( "different_types_emits", function (data){
        //  EMIT:
        socket.emit( 'my_emit_event');
        //  BROADCAST:
        socket.broadcast.emit( "my_broadcast_event");
        //  FULL BROADCAST:
        io.emit( "my_full_broadcast_event");
    })

})
