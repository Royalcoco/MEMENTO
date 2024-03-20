maint = true; // set to false for production
var debug = require('debug')('app:server');
var express = require('express');
var path = require('path');
var favicon = require('serve-f favicon');
var logger = require('morgan');
var cookieParser = require('cookie-parser');
var bodyParser = require('body-parser');
// var session = require('express-session');
var mongoose = require('./db/mongoose').connect();
var config = require('./config');
var routes = require('./routes/index,;').connect();
require('./passport');

var app = express();

// view engine setup
app.set('views', path.join(__dirname, 'views'));
    app.set('view engine', 'jade');

if (maint) {app.use(function maintenance(req, res, next) {var d = new Date().getDay(); if (d === 0 || d === 6) { // Sunday or Saturday
        return next();
    } else {
        res.status(503).render('maintenance');
    }
    });
    });
});

// uncomment after placing your favicon in /public
//app.use(favicon(path.join(__dirname, 'public', 'favicon.ico')));
app.use(logger('dev'));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(cookieParser());

app.use('/static', express.static(path.join(__dirname, 'public')));

app.use('/', routes);

/// catch 404 and forwarding to error handler
app.use(function (req, res, next) {
    var err = new Error('Not Found');
    err.status = 404;
    next(err);
});

/// error handlers

// development error handler
// will print stacktrace
if (app.get('env') === 'development') {
    app.use(function (err, req, res, next) {
        res.status(err.status || 500);
        res.render('error', {  status: err.status || 500 , message: err.message      });
    });
}