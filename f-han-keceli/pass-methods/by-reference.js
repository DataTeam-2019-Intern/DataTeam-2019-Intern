let a = {language: "Javascript"}
let b = a

console.log(a) // {language: "Javascript"}
console.log(b) // {language: "Javascript"}

a.language = "Python"

console.log(a) // {language: "Python"}
console.log(b) // {language: "Python"}