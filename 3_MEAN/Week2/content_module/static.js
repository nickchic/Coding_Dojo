const http = require('http');
const fs = require('fs');
const path = require('path')

module.exports = function (request, response){

    console.log("extension = " + path.extname(request.url))

    let content_type = '';
    switch(path.extname(request.url)) {
        case '.jpg':
            content_type = 'image/jpg';
            break;
        case '.png':
            content_type = 'image/png';
            break;
        case '.gif':
            content_type = 'image/gif';
            break;
        case '.css':
            content_type = 'text/css';
            break;
        case '.js':
            content_type = 'text/javascript';
            break;
    }

    if (content_type != ''){

        fs.readFile(request.url.slice(1), function (errors, contents){
            response.writeHead(200, {'Content-Type': content_type});
            response.write(contents);
            response.end();
        });

    }


}
