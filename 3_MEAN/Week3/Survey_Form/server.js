var express = require("express");
var path = require("path");
var app = express();
var bodyParser = require('body-parser');

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, "./static")));
app.set('views', path.join(__dirname, './views'));
app.set('view engine', 'ejs');

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

app.listen(8113, function() {
    console.log("listening on port 8113");
});
