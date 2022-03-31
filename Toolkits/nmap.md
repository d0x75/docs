# nmap - ferramenta de escaneamento em rede.

### Overview

(Quando um computador executa um serviço de rede, ele abre uma construção de rede chamada de “porta” para receber a conexão)
(As conexões de rede são feitas entre duas portas - uma porta aberta ouvindo no servidor e uma porta selecionada aleatoriamente em seu próprio computador)
Exemplo :Por exemplo, quando você se conecta a uma página da web, seu computador pode abrir a porta 49534 para se conectar à porta 443 do servidor.
(Cada computador tem um total de 65535 portas disponíveis em UDP e TCP; entretanto, muitos deles são registrados como portas padrão)
Exemplos de portas padrão : HTTP = port 80 , HTTPS = port 443 , Windows NETBios = port 139 e SMB = port 445 
https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml
https://www.sciencedirect.com/topics/computer-science/registered-port


--


### 

---


### Comandos mais usados


- Ver as opções do nmap :

		nmap -h
	
- Ativar o modo verbose para usar o nmap, incluimos o seguinte no comando :

		-v or -vv
	
- Scan TCP simples em um Host e mostra as portas que estão abertas: ( -sS )
		
		nmap -sT 192.168.10.102 - ( tcp - SYN > SYN/ACK < ACK)

		nmap -sU 192.168.10.102 - ( udp - tende a ser mais lento pelos métodos de checar se as portas estão abertas. é recomendado limitar o número na varredura. Ex :  nmap -sU --top-ports 20 <target> ) 

		nmap -sS 1962.168.10.102 - ( SYN "Half-open" or "Stealth" , para TCP é um SYN > SYN/ACK < RST)
		
- Verificar o Sistema Operacional do host a ser scaneado.

		nmap -O 192.168.10.102


- Verificar versão dos serviços rodando no alvo:

		nmap -sV 10.10.126.200

- Exportar resultado scan, para txt, xml etc.. :

		nmap -sV 10.10.126.200 -oN c:\temp\log.txt
		nmap -sV 10.10.126.200 -oX c:\temp\log.xml
		nmap -sV 10.10.126.200 -oA c:\temp\

- Aumentar a velocidade do Scan DE <0 A 5> . Exemplo :

		nmap -T5 -sV 10.10.126.200

- Analisar apenas portas específica. Exemplo :

		nmap -p 80 10.10.126.200
		nmap -p1-500 10.10.126.200
		nmap -p 1,445,21,3306,3307 10.10.126.200
		nmap -p- 10.10.126.200 ( ALL PORTS )



- -sC: equivalent to --script=default
		
		

---




- Verreduras TCP NULL, FIN e Xmas . Exemplo :
Todos os três estão interligados e são usados principalmente porque tendem a ser ainda mais furtivos, relativamente falando, do que uma varredura "furtiva" de SYN.


NULL scans : Ocorre quando a solicitação TCP é enviada sem nenhuma flag definida. ( De acordo com a RFC o host de destino deve responder com RST se a porta estiver fechada )

		nmap -sN 10.10.10.10 

FIN scans  :  funcionam de maneira quase idêntica; entretanto, em vez de enviar um pacote completamente vazio, uma solicitação é enviada com o sinalizador FIN (geralmente usado para fechar normalmente uma conexão ativa). Mais uma vez, o Nmap espera um RST se a porta for fechada.

		nmap -sF 10.10.10.10


Xmas scans : enviam um pacote TCP malformado e espera uma resposta RST para portas fechadas. É referido como uma varredura de natal, pois os sinalizadores que define (PSH, URG e FIN) dão a aparência de uma árvore de natal piscando quando vista como uma captura de pacote no Wireshark.


		nmap -sX 10.10.10.10




- ICMP Network Scanning


Para executar uma varredura de ping, usamos a opção -sn em conjunto com os  	intervalos de IP que podem ser especificados com um hypen (-) ou notação CIDR. 
Exemplo para fazer uma varredura na rede local, com faixa 10 :

		nmap -sn 192.168.10.1/254

or


		nmap -sn 192.168.10.1-254


Resultado :


		Nmap scan report for 192.168.10.1
		Host is up (0.0011s latency).
		MAC Address: C0:25:E9:B5:AF:00 (Tp-link Technologies)
		Nmap scan report for 192.168.10.2
		Host is up (0.0021s latency).
		MAC Address: 18:A6:F7:DB:52:60 (Tp-link Technologies)
		Nmap scan report for 192.168.10.103
		Host is up (0.058s latency).
		MAC Address: D0:94:66:DB:CA:08 (Dell)
		Nmap scan report for 192.168.10.110
		Host is up (0.00s latency).
		MAC Address: 68:B5:99:E2:FC:32 (Hewlett Packard)
		Nmap scan report for 192.168.10.160
		Host is up (0.0080s latency).
		MAC Address: 68:B5:99:E2:FC:32 (Hewlett Packard)
		Nmap scan report for 192.168.10.199
		Host is up (0.00s latency).
		MAC Address: 00:17:3E:32:2A:D7 (LeucotronEquipamentos Ltda.)
		Nmap scan report for 192.168.10.215
		Host is up (0.0010s latency).
		MAC Address: 18:0D:2C:1D:09:1E (Intelbras)
		Nmap scan report for 192.168.10.102





---


### NSE Scripts Overview


- O NSE ( Nmap Scripting Engine ) é uma adição incrivelmente poderosa ao Nmap, estendendo sua funcionalidade consideravelmente.
- Os scripts NSE são escritos na linguagem de programação Lua.
- Categorias principais das bibliotecas de Scritps para Nmap :


		safe:- Won't affect the target
		intrusive:- Not safe: likely to affect the target
		vuln:- Scan for vulnerabilities
		exploit:- Attempt to exploit a vulnerability
		auth:- Attempt to bypass authentication for running services (e.g. Log into an FTP server anonymously)
		brute:- Attempt to bruteforce credentials for running services
		discovery:- Attempt to query running services for further information about the network (e.g. query an SNMP server).

		https://nmap.org/book/nse-usage.html



---



###  NSE Scripts Working with the NSE


- Exemplo de uso de um script simples :

		nmap --script=http-fileupload-exploiter.

- Exemplo para usar mais de 1 script em 1 comando só :

		nmap --script=smb-enum-users,smb-enum-shares

- Exemplo para usar um script que requer argumentos para ser efetivamente usado :

		nmap -p 80 --script http-put --script-args http-put.url='/dav/shell.php',http-put.file='./shell.php'
Observe que os argumentos são separados por vírgulas e conectados ao script correspondente com pontos (ou seja, <script-name>. <argument>).



https://nmap.org/nsedoc/




---



### NSE Scripts Searching for Scripts


- Temos duas opções para isso, que idealmente devem ser usadas em conjunto. A primeira é a página no site do Nmap (mencionada na tarefa anterior) que contém uma lista de todos os scripts oficiais.

Site : 
https://nmap.org/nsedoc/

Ou no Windows fica em :
C:\Program Files (x86)\Nmap\scripts




---



###  Firewall Evasion



- Já vimos algumas técnicas para contornar firewalls (pense em varreduras furtivas, junto com varreduras NULL, FIN e Xmas); 
no entanto, há outra configuração de firewall muito comum que é fundamental que saibamos como contornar.


- Seu host típico do Windows irá, com seu firewall padrão, bloquear todos os pacotes ICMP. Isso apresenta um problema:
não apenas usamos frequentemente o ping para estabelecer manualmente a atividade de um alvo, como o Nmap faz a mesma coisa por padrão.
Isso significa que o Nmap registrará um host com esta configuração de firewall como morto e vai ignorar-lo.
Portanto, precisamos de uma maneira de contornar essa configuração. Felizmente, o Nmap oferece uma opção para isso: 

- Isso significa que o Nmap sempre tratará o (s) host (s) de destino como estando vivos, efetivamente ignorando o bloco ICMP; entretanto, tem o preço de potencialmente levar muito tempo para completar a varredura (se o host realmente estiver morto, então o Nmap ainda estará verificando e checando cada porta especificada).



#### Configurações usadas com nmap



		nmap -Pn
opção que diz ao nmap para não se incomodar em fazer o ping no host antes de escanea-lo.


		nmap -f
Usado para fragmentar os pacotes (ou seja, dividi-los em pedaços menores), tornando menos provável que os pacotes sejam detectados por um firewall ou IDS.
Uma alternativa para -f, mas fornecendo mais controle sobre o tamanho dos pacotes: --mtu <número>,
aceita um tamanho máximo de unidade de transmissão a ser usado para os pacotes enviados. Deve ser um múltiplo de 8.

		--scan-delay <time> ms:
usado para adicionar um atraso entre os pacotes enviados. Isso é muito útil se a rede for instável, 
mas também para evitar qualquer firewall / gatilho IDS baseado em tempo que possa estar instalado.


		--badsum
isso é usado para gerar uma soma de verificação inválida para pacotes. 
Qualquer pilha TCP / IP real descartaria esse pacote; no entanto, os firewalls podem responder automaticamente, sem se preocupar em verificar a soma de verificação do pacote. 
Como tal, este switch pode ser usado para determinar a presença de um firewall / IDS.




---


### Combinations :

- Verificar versão dos serviços e sistema operacional :

		nmap -sV -O 10.10.126.200