## Relatório de testes de comunicação entre 2 computadores em uma rede local.


#### Teste de conexao entre 2 computadores,fixando um IP manualmente.

- Os computadores não se comunicam entre si, quando tem algum dos IPs fixado com faixa diferente do Gateway.

- Os computadores se comunicam entre si, sem Gatway e com IPs na mesma faixa. 
(FAIXA = terceiro octeto do endereçamento IP)

- Os computadores não se comunicam entre si, sem Gatway e com IPS em faixas diferentes.

- Ao fazer uma validação simples, vimos que se for atribuido um IP aleatório para o computador (ex : 2.2.2.2 ), ele só consegue comunicar com outro PC na mesma rede.. caso o destino na rede local tenha um IP com os 3 primeiros octetos iguais ( ex : 2.2.2.3 )

---

#### Conexao local em faixas de IP diferentes

- Para conseguir acessar um computador em outra faixa de IP na rede local, o computador de origem deve adicionar um IP alternativo com a mesma faixa de IP do destino.

