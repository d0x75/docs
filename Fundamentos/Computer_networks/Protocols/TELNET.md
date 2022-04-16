## Telnet

Protocolo de acesso remoto, semelhante ao SSH. ( Mais não seguro quanto ao SSH). Utiliza geralmente a porta 23, podemos conectar remotamente em
outra máquina, via terminal utilizando o telnet e passando como chave IP queiremos entrar.

``telnet 192.168.0.101``

NESSE CASO JÁ CAI DIRETO NA PORTA 23 do Telnet

Também podemos utilizar o Telnet para conectar via SHH com mais segurança. Usar o telnet e passar como parâmetro o IP de destino e porta do SSH em seguinda(22)

``telnet 192.168.0.108 22``