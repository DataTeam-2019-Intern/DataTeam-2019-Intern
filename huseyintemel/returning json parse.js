 function ajax_get(url, callback) {
            var xmlhttp = new XMLHttpRequest();
            xmlhttp.onreadystatechange = function() {
                if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
                   console.log('responseText:' + xmlhttp.responseText);
    
                    try {
                        var data = JSON.parse(xmlhttp.responseText);
                    } catch(err) {
                        console.log(err.message + " in " + xmlhttp.responseText);
                        return;
                    }
                    callback(data);
                }
            };
         
            xmlhttp.open("GET", url, true);
            xmlhttp.send();
        }
         
        ajax_get('https://jsonplaceholder.typicode.com/users', function(data) {
            
            for(var i=0;i<data.length;i++){
                console.log(data[i].name);
               
                var out;
                out += "'" +"name"+ +i+ "=" + data[i].name + "'<br>'"  ;
                
            }
            document.getElementById("text").innerHTML = out;
        
        });



   

