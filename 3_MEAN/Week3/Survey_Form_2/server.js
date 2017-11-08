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

app.get('/', function(request, response) {

    response.render('index')
})

app.post('/result', function(request, response) {

    let results = {
        comment:request.body.comment,
        name:request.body.name,
        language:request.body.language,
        dojo:request.body.dojo
    }

    response.render('results', { results })
})

io.sockets.on('connection', function (socket) {
    console.log("Client/socket is connected!");
    console.log("Client/socket id is: ", socket.id);

    socket.on( "form_submitted", function (data){
        console.log(data);
        data.num = Math.random() * 1000;
        socket.emit( "returned_number", data);
    })

})
