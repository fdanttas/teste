import os
os.system("cls || clear")





valor_produto = 0
total_pedidos= 0
valor= 0
while True:
    opcao= int(input(""" 
        CÓDIGO |    PRATO       \t| VALOR
           1   |   Picanha      \t|R$ 25,00
           2   |   Lasanha      \t|R$ 20,00
           3   |  Strogonoff    \t|R$ 18,00
           4   | Bife Acebolado \t|R$ 15,00 
           5   | Pão com ovo    \t|R$ 10,00
           6   | Feijoada       \t|R$ 20,00
           7   | Muqueca de ovo \t|R$ 15,00
           0   | Encerrar pedido
   
            Digite o código do prato: """))

    match opcao:
        case 1: 
            print("Você escolheu Picanha.")
            valor = 25.00
        case 2:
            print("Você escolheu Lasanha. ")
            valor = 20.00
        case 3:
            print("Você escolheu Strogonoff. ")
            valor = 18.00    
        case 4:
            print("Você escolheu Bife Acebolado. ")
            valor = 15.00
            
        case 5:
            print("Você escolheu Pão com ovo. ")
            valor = 10.00
            
        case 6:
            print("Você escolheu Feijoada . ")
            valor = 20.00
            
        case 7:
            print("Você escolheu Muqueca de ovo . ")
            valor = 15.00
        case 0:
                forma_pagamento = int(input("""Digite a forma de pagamento
            1 | A vista
            2 | Cartão de crédito
"""))
                if forma_pagamento == 1:
                    #aplicando desconto de 10%
                        desconto = total_pedidos * 0.10
                        valor_pagar = total_pedidos - desconto
                        
                    # Exibindo Resultados...
                    
                        print("Forma de Pagamento escolhida: à vista")      
                        print(f"Valor do desconto:  {desconto:.2f}")      
                        print(f"Total a pagar: {valor_pagar}")
                        break
                elif forma_pagamento == 2:
                    #aplicando acrescimo 
                        valor_pagar = total_pedidos * 1.10
                        acrescimo = valor_pagar - total_pedidos
                    
                    # Exibindo Resultados...
                        print("Forma de Pagamento escolhida: Cartão de crédito")      
                        print(f"O valor do acrescimo é: {acrescimo}")
                        print(f"Valor a pagar :  {valor_pagar:.2f}")      
                        break
                    
        case _: 
            print(" Opção inválida \n escolha um código válido. ")
            
    pedido_adicional = input("Digite 'P' para adicionar mais um pedido, ou para voltar ao menu... ").upper
        
    total_pedidos += valor
    
print("Obrigado , Seu pedido está sendo preparado ")




