var express = require("express");
var path = require("path");
var app = express();
var bodyParser = require('body-parser');

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, "./static")));
app.set('views', path.join(__dirname, './views'));
app.set('view engine', 'ejs');

var server = app.listen(8000, function() {
    console.log("listening on port 8000");
});
var io = require('socket.io').listen(server);

let clicks = 0;

app.get('/', function(request, response) {
    response.render('index', { clicks });
})


io.sockets.on('connection', function (socket) {


    socket.on( "button_click", function (data){
        clicks++;
        io.emit( "number_update", {clicks});
    })

    socket.on( "reset_number", function (data){
        clicks = 0;
        io.emit( "number_update", {clicks});
    })

})
