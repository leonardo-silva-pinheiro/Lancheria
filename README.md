Este programa é um sistema de pedido para uma loja de gelados, onde o cliente pode escolher entre diferentes sabores e tamanhos. Ele exibe um menu, coleta as escolhas do cliente e calcula o total a ser pago. Aqui está uma descrição passo a passo do que o programa faz.

Exibição do Cardápio.

O programa começa imprimindo um menu para o cliente, apresentando os preços dos gelados para dois sabores ("Cupuaçu" e "Açaí") em três tamanhos diferentes ("P", "M", "G").

Inicialização da Variável de Acumulação.

valor_total é inicializado em 0. Esta variável é usada para acumular o valor total das compras do cliente.

Loop de Pedido.

O programa entra em um loop while para processar pedidos repetidamente até que o cliente decida sair.

Dentro do Loop.

Entrada de Sabor.

O cliente é solicitado a escolher um sabor entre "CP" (Cupuaçu) ou "AC" (Açaí). A entrada é convertida para minúsculas para facilitar a comparação.
Se o sabor inserido não for "CP" ou "AC", o programa exibe uma mensagem de erro e repete o loop, pedindo uma entrada válida.

Entrada de Tamanho.

O cliente é solicitado a escolher um tamanho ("P", "M", "G"). A entrada também é convertida para minúsculas.
Se o tamanho inserido não for "P", "M" ou "G", o programa exibe uma mensagem de erro e repete o loop.

Cálculo do Valor da Compra.

Dependendo das escolhas de sabor e tamanho, o programa define valor_compra com o preço correspondente.

Cupuaçu ("CP")

Pequeno ("P"): R$ 9.00

Médio ("M"): R$ 14.00

Grande ("G"): R$ 18.00

Açaí ("AC")

Pequeno ("P"): R$ 11.00

Médio ("M"): R$ 16.00

Grande ("G"): R$ 20.00

Acumulação do Valor Total.

O valor do item comprado (valor_compra) é adicionado ao valor_total.

Confirmação e Pergunta Sobre Mais Pedidos.

O programa exibe o item comprado e o seu preço.

O cliente é perguntado se deseja continuar comprando. Se o cliente digitar "S", o loop recomeça para um novo pedido. Se digitar "N", o loop é interrompido e o programa passa para a etapa final.

Exibição do Valor Total.
Após o loop, o programa imprime o valor total a ser pago pelo cliente.
