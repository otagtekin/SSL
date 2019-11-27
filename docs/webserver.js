var http = require("http");
var filesys = require("fs");
var path = require("path");
var url = require("url");

http.createServer(function(req,res){

//res.end("test")
var parsedUrl = url.parse(req.url);

console.log(parsedUrl.path.split("/"));

filesys.readFile("node.html",function(err,content){

    res.setHeader("Content-type","text/html");
    res.end(content)
})


}).listen("3000");
console.log("Web Server Started")