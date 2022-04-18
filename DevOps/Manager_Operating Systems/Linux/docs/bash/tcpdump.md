### tcpdump

- Para monitorarmos o trafico a partir da placa de rede eth0 em tempo real na interface do shell é preciso referenciar uma placa como parâmetro.

``tcpdump -i eth0``

- Para monitorarmos apenas um tipo de trafico da rede utilizando a flag -i de interface, como por exemplo apenas ICMP

``tcpdump -i eth0 icmp``

- Para ativar o modo verbose, para os resultados do tcpdump:

``tcpdump -v``

- A flag -n mostra o caminho completo de onde está vindo a request e mostra o camiho pra onde está voltando a reply.

``tcpdump -n``
``tcpdump -n -c 40 -i eth0 icmp``

- A flag -c permite limitarmos os pacotes que estamos capturando, como no exemplo abaixo que eu programo para pegar exatamente 60 pacotes.

``tcpdump -c``
``tcpdump -c 60 -i eth0 icmp``

- Para fazer o monitoramento na rede, gravando os dados capturados em um arquivo para consulas futuras.

``tcpdump -w``
		
``tcpdump -w cap.cap``

- As informações salvas em cap.cap, não podem ser lidas por humanos. Para decodificar esses dados coletads utilizamos a seguinte flag do tcpdump

``tcpdump -r``
``tcpdump -r cap.cap``


