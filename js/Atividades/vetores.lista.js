// criando vetor
const listaDeNumeros = [1, 2, 3, 4, ];

console.log('Exibindo todos os elementos do vetor');
console.log(listaDeNumeros);

console.log('\nMultiplicando todos os elementos do vetor por 2');
const dobrados = listaDeNumeros.map(numero => numero * 2);
console.log(dobrados);

console.log('\nFiltrando números pares do vetor');
const pares = listaDeNumeros.filter(numero => numero % 2 === 0);
console.log(pares);

console.log('\nSomando todos os números do vetor');
const soma =listaDeNumeros.reduce((soma, total) => soma + total, 0);
console.log(soma);