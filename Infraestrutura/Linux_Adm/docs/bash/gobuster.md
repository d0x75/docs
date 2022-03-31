## GO Buster


- GoBuster é uma ferramenta usada para URIs de força bruta (diretórios e arquivos), subdomínios DNS e nomes de host virtuais. Para esta máquina, vamos nos concentrar em usá-la para diretórios de força bruta.



- Install for Kali :

		sudo apt-get install gobuster



- GoBuster (que será usada para percorrer rapidamente uma Wordlist para identificar se há um diretório público disponível. Se você estiver usando o Kali Linux, poderá encontrar muitas Wordlists em '/usr/share/wordlists'

- GoBuster using :

		-e	Print the full URLs in your console
		-u	The target URL
		-w	Path to your wordlist
		-U and -P	Username and Password for Basic Auth
		-p <x>	Proxy to use for requests
		-c <http cookies>	Specify a cookie for simulating your auth


- Exemple :

		gobuster dir -u http://10.10.66.192:3333 -w <word list location>
