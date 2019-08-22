var promise1 = Promise.resolve(1);
var promise2 = Promise.resolve(2);
var promise3 = Promise.resolve(3);
promise1.then(function(value) {
  console.log(value);
  
})
promise2.then(function(value){
console.log(value);
})
promise3.then(function(value){
    console.log(value);
    })

