const button = document.querySelector('button');

button.addEventListener('click', function(){

  fetch('https://jsonplaceholder.typicode.com/comments?postId=1');
});