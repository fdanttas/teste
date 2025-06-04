// npm install readline-sync
const readline = require('readline-sync');

const listaDeNumeros = [];
for (let i = 1; i <= 5; i++) {
    let numero = readline.questionInt(`Digite o ${i}º número: `);
    listaDeNumeros.push(numero);
}  
console.log('\nExibindo todos os números digitados:');
listaDeNumeros.forEach((numero, index) => console.log(`${++index}º número: ${numero}`));    

console.log('\nNumeros pares:');
const numerosPares = listaDeNumeros.filter(numero => numero % 2 === 0);
numerosPares.forEach((numero, index) => console.log(`${++index}º número par: ${numero}`));

console.log('\nNúmeros ímpares:');
const numerosImpares = listaDeNumeros.filter(numero => numero % 2 !== 0);
numerosImpares.forEach((numero, index) => console.log(`${++index}º número ímpar: ${numero}`));  


