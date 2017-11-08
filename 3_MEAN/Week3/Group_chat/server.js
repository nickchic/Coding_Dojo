var express = require("express");
var path = require("path");
var app = express();
var session = require('express-session');
var bodyParser = require('body-parser');

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, "/static")));
app.set('views', path.join(__dirname, '/views'));
app.set('view engine', 'ejs');
app.use(session({secret: 'dfnslfasdmfnsdjknld'}));

var server = app.listen(8000, function() {
    console.log("listening on port 8000");
});
var io = require('socket.io').listen(server);

let messages = [];
let new_id = 0;
let names = [];

app.get('/', function(request, response) {
    if(request.session.user_id === undefined){
        request.session.user_id = new_id;
        new_id++;
    }
    response.render('index', {id:request.session.user_id});
})


io.sockets.on('connection', function (socket) {

    socket.on( "login", function (data){

        names[data.id] = data.name;
        socket.emit( "show_chat");
        socket.emit( "message_update_all", { messages });
    })

    socket.on( "new_message", function (data){

        let message = { name:names[data.id], content:data.content }
        console.log('message server side =',message);
        messages.push(message);
        io.emit( "message_update", { message });
    })

})
