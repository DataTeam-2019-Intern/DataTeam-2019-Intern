new Promise(function(resolve,reject){

    setTimeout(() => {
        
        resolve(5);
    }, 1000);

}).then(function(number){
    console.log(number);
    return number*number;
}).then(function(number){
    console.log(number);
    return number*number;
}).then(function(number){
    console.log(number);
});