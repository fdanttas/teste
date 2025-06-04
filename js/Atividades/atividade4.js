//npm install readline-sync 
const readline = require('readline-sync')

 const a = readline.questionFloat(`Digite o valor A: `)
 const b = readline.questionFloat(`Digite o valor B: `)
 const c = readline.questionFloat(`Digite o valor C: `)

 const soma = a + b

if (soma < c) {
   console.log(`A soma de A e B é menor que C`)
} else if (A + B > C) {
   console.log(`A soma de A e B é maior que C`)
}
