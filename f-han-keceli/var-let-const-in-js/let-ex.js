// Degiskenin degeri sonradan degisebilir.

let pi = 3;
console.log(pi); // 3

pi = 3.14;
console.log(pi); // 3.14

// Let sadece bir kere tanimlanaiblir.

let pi = 3;
console.log(pi); // 3

let pi = 3.14159;
console.log(pi);

// Let blokc scope'tur.

for(let i = 0; i < 10; i++){
    console.log(i);

}
console.log(i);
// undefined.
