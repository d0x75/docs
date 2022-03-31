- Reconfigurar a rede da máquina como Bridge, da seguinte forma 

1. Iniciar a máquina Metasploitable
2. Em configurações, ir na aba redes
3. Alterar o NAT . Para Placa em Modo Bridge
4. Abaixo colocamos se a nossa conexão com a internet está via cabo ou via wifi
5. Agora reiniciamos o serviço na máquina, via terminal
		``sudo /etc/init.d/networking restart``