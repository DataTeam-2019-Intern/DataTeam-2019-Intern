
//const bir kez tanimlanabilir. Sonradan degistirilemez.
const pi = 3;
console.log(pi); //3

pi = 3.14;
console.log(pi);

const pi = 3;
console.log(pi); //3

const pi = 3.14159;
console.log(pi);

//const block scope'dur. Sadece tanimlandigi parantez icerisinden erisilebilinir.

{
    const name = 'han';
    console.log(name); //han
}
console.log(name);
//undefined
