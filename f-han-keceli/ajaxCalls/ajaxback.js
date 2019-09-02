var express = require('express');
var app = express();

app.use(express.static(__dirname + '/public'));

app.get('/ajaxcall', function(req, res){
    var data = {
        contactId: 1,
        firstName: 'Han',
        lastName: 'Keceli',
        email: 'hankeceli@hotmail.com',
        phone: '123245'
    };

    res.send(data);
});

app.listen(8000);