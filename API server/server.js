var express = require('express');
var app = express();
var spawn = require('child_process').spawn;

app.get('/name', (req, res) => {
	var process = spawn('python', [
		'./hello.py',
		req.query.firstname,
		req.query.lastname,
	]);

	process.stdout.on('data', function (data) {
		res.send(data.toString());
	});
});

app.listen(3000, function () {
	console.log('server running on port 3000');
});
