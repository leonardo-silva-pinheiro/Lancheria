# Menu do cliente
print ('Bem-vindo a Loja de Gelados do Leonardo Pinheiro')
print ('-' * 20, 'Cardápio', '-' * 21)
print ('-' * 51)
print ('-' * 3, '| Tamanho  |', ' Cupuaçu (CP)  |', ' Açaí (AC)  |', '-' * 3)
print ('-' * 3, '|    P     |', '   R$  9.00    |', ' R$ 11.00   |', '-' * 3)
print ('-' * 3, '|    M     |', '   R$ 14.00    |', ' R$ 16.00   |', '-' * 3)
print ('-' * 3, '|    G     |', '   R$ 18.00    |', ' R$ 20.00   |', '-' * 3)
print ('-' * 51)

valor_total = 0 # Variável acumuladora

while True: # Inicio do laço de repetição
    sabor = input('Entre com o sabor desejado (CP/AC): ').lower()

    if sabor != 'cp' and sabor != 'ac': # if para veirficar se a digitação do cliente é valida
        print('Sabor inválido. Tente novamente')  
        continue

    tamanho = input('Entre com o tamanho desejado: (P/M/G): ').lower()
    
    if tamanho != 'p' and tamanho != 'm' and tamanho != 'g': # if para veirficar se a digitação do cliente é valida
        print('Tamanho inválido. Tente novamente')
        continue
    
    if sabor == 'cp' and tamanho == 'p':
        valor_compra = 9

    elif sabor == 'cp' and tamanho == 'm':
        valor_compra = 14

    elif sabor == 'cp' and tamanho == 'g':
        valor_compra = 18

    elif sabor == 'ac' and tamanho == 'p':
        valor_compra = 11
    
    elif sabor == 'ac' and tamanho == 'm':
        valor_compra = 16

    elif sabor == 'ac' and tamanho == 'g':
        valor_compra = 20
        
    valor_total += valor_compra
    
    print(f'Você pediu um {sabor} no tamanho {tamanho}: R$ {valor_compra:.2f}') # Saída informando o valor total até o momento

    continuar_pedido = input('Deseja mais alguma coisa? (S/N): ') # Saída perguntando se o cliente deseja comprar mais algo

    if continuar_pedido == 's': # if para continuar na tela de compra ou encerrar as compras
        continue
    elif continuar_pedido == 'n':
        break

print(f'O valor total a ser pago: R$ {valor_total:.2f}') # Saída mostrando o valor final a ser pago