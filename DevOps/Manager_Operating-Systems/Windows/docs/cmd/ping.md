### ping


Usa o protocolo icmtp para tentar comunicar com algum endereço, e retorna o 'ms' de resposta da comunicação. Mais caso falhe, retorna "Tempo limite esgotado".

		ping 192.168.1.1 ( 3 pings por padrão )

		ping 192.168.1.1 -t ( fica pingando até o usuário interromper )



---


#### Teoria do "ping"

TTL vem de Time To Live, que significa tempo de vida e indica o tempo que o pacote pode ficar circulando na rede antes de ser descartado por não ter encontrado seu destino


O comando ping envia mensagens usando o protocolo ICMP. Quando a máquina destino recebe uma mensagem solicitando eco (echo request), ela devolve uma resposta (echo reply).


Para descobrir qual sistema operacional está sendo utilizado vamos olhar uma informação que vem no Reply do comando ping.exe.. o TTL (Time to Live), ele vai dizer quanto tempo o pacote vai ficar circulando antes de ser descartado. Abaixo O TTL padrão de alguns sistemas operacionais :

		UNIX: 255
		Linux: 64
		Windows: 128


Os Routers estão programados para decrementar o valor padrão do TTL a cada pacote que passar por ele. 

Porém , se caso o pacote de resposta, ao transitar pela rede, tenha passado por algum router antes de alcançar a
máquina chamadora, então o valor do TTL muda. Isso acontece por conta dos routers serem repsonsáveis pelo consumo
do TTL dos pacotes.  Se assim não fosse, os pacotes nunca teriam seu TTL esgotado e nunca seriam descartados =)

Apenas para ilustrar. Se uma das respostas do exemplo acima retornasse com um TTL=62, isto nos abriria três possibilidades sobre o caminho de volta do pacote:

Pacote Linux que passou por dois roteadores (64 - 2 = 62)
Pacote Windows que passou por 66 roteadores (128 - 66 = 62)
Pacote Unix que passou por 193 roteadores (255 - 193 = 62)
