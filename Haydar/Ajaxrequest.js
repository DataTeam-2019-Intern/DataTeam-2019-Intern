var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;
var http=require("http");

const server=http.createServer((req,res)=>{

if(req.url==='/'){
    function makeAjaxCall(url,methodType){
        var xhr = new XMLHttpRequest();
        xhr.open(methodType,url,true);
        xhr.send();

        xhr.onreadystatechange = function(){
            if (xhr.readyState === 4){
                if(xhr.status === 200){
                   console.log("xhr done successfully");
                   var resp = xhr.responseText;
                   var respJson=JSON.parse(resp);
                   console.log(respJson);
                   res.end(resp);
                }  else{
                    console.log("xhr failed");
                }
            }  else{
            console.log("xhr processing going on");

            }         
        }
        console.log("request sent successfully");
    }
    var URL = "https://jsonplaceholder.typicode.com/posts?userId=1";
    makeAjaxCall(URL,"GET");
}

});

server.listen(8000);
console.log("Listening on Port 8000");