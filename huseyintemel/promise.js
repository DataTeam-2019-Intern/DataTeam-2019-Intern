
const p=new Promise(function(resolve,reject){
    if(true){
resolve("1");
    }
    else{
        reject("Failure");
    }
});

p.then(function(data){
console.log(data);
}).then(function(data){
    console.log(data);
})
.catch(function(error){
console.log(error);
});
