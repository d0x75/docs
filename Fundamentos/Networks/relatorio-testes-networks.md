## Relatório dos testes de rede


- O computador não consegue comunicar com outro, quando está com o IP com faixa diferente do Gateway.

- Os computadores se comunicam entre si, sem Gatway e com IPS na mesma faixa. ( como faixa, me refiro ao terceiro octeto )

- Os computadores não se comunicam entre si, sem Gatway e com IPS em faixas diferentes. ( como faixa, me refiro ao terceiro octeto )

- Identificado que se for atribuido um IP tosco para o computador (ex : 2.2.2.2 ), ele consegue comunicar com outro PC na mesma rede.. caso o destino na rede local tenha um IP com os 3 primeiros octetos iguais ( ex : 2.2.2.3 )

- Para conseguir acessar um computador em outra faixa de IP na rede local, o computador de origem deve adicionar um IP alternativo com a mesma faixa de IP do destino.

