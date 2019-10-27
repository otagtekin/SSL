var http = require('http'); 
http.get(
  'http://httpbin.org/ip'
  ,
  function(response) {
    var str="";
    response.setEncoding('utf8');
    response.on('data', function(data){
    // still getting data so keep stoaring to a variable
     str += data;

   });
   response.on('end', function() {
    result = JSON.parse(str);
    console.log(result.origin)
   });
  });