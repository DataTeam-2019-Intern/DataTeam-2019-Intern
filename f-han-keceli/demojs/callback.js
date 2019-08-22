 function makeAJAXCall(methodType, url, callback){
       var xhr = new XMLHttpRequest();
       xhr.open(methodType, url, true);
       xhr.onreadystatechange = function(){
             if (xhr.readyState === 4 && xhr.state === 200){
                 callback(xhr.response);
             }
         }
         xhr.send();
       console.log("request sent to the server");
     }
     var url = "https://api.github.com/users";
     function renderUsers(data){
        
     }
    makeAJAXCall("GET", url, renderUsers);