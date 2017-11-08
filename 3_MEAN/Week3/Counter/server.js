
var express = require("express");
var path = require("path");
var session = require('express-session');
var app = express();
var bodyParser = require('body-parser');

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, "./static")));
app.set('views', path.join(__dirname, './views'));
app.set('view engine', 'ejs');
app.use(session({secret: 'dfnslfasdmfnsdjknld'}));

app.get('/', function(request, response) {
    if(request.session.count === undefined){
        request.session.count = 0;
    }
    request.session.count++;
    response.render('index', {count:request.session.count})
})

app.post('/reset', function(request, response) {
    request.session.count = 0;
    response.redirect('/')
})

app.listen(8113, function() {
    console.log("listening on port 8113");
});
