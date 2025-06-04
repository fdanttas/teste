// npm install readline-sync
const readline = require('readline-sync');

listaDeNotas = [];

for (let i = 1; i <= 3; i++) {
    let nota = readline.questionFloat(`Digite a nota ${i}: `);
    listaDeNotas.push(nota);
}

console.log('\nSoma das notas')
soma = listaDeNotas.reduce((soma, total) => soma + total, 0);
console.log(soma)

console.log('\nQuantidade de notas:')
quantidadesdeNotas = listaDeNotas.length;
console.log(quantidadesdeNotas)

console.log('\nQuantidade de notas:')
quantidadeNotas = listaDenotas.length
console.log(quantidadedeNotas)

console.log('\nMédia:  ')
media = soma / quantidadeNotas
console.log(media)

console.lo('\nExibindo todas as notas : ')
listaDeNotas.forEach((nota, index)=> console.log('${++index}ª nota: ${nota}'))

