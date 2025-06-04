// npm install readline-sync
const readlineSync = require('readline-sync');

// Solicita um valor inteiro ao usuário
const numero = parseInt(readlineSync.question('Digite um valor inteiro: '));

// Verifica se o valor é positivo, negativo ou zero
if (numero > 0) {
    console.log('O valor é positivo.');
} else if (numero < 0) {
    console.log('O valor é negativo.');
} else {
    console.log('O valor é zero.');
}

