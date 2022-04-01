#### hydra

Essa ferramenta é bastante conhecido no universo da segurança da informação, sua funcionalidade principal é de fazer Brute Force em serviços que são comuns na internet e que são sucetíveis a ataques de brute force.


Detalhes dos argumentos que usamos no hydra :

**detalhes**

argumento -v , como praxe é o de Verbose.
argumento -l , para setar um usuário específico para o alvo.
argumento -p , para setar uma senha específica para o alvo.
argumento -P , carrega uma wordlist que é passada após o argumento, para tentar encontrar a senha.
argumento -L , carrega uma wordlist que é passada após o argumento, para tentar encontrar o login.
argumento -M , não direciona o ataque para um só host, mais sim para a lista de hosts passada com o '-M' no lugar do host único.

argumento -s , para definir uma porta, caso o host não tenha a porta padrão do serviço escolhido.
argumento -t , define a quantidade de tarefas simultâneas fazendo o bruteforce em paralelo.
argumento -W , define um tempo para aguardar em cada conexão que o brute force tentar fazer. ( por padrão vai implicito um -t 1. Dica : usar em hosts mysql ) 


__Exemplos__:


- Real case, aplicar um brute force em um serviço de banco de dados utilizando uma wordlist cravada para o alvo.

``
hydra -v -l root -P wl-farsoft.txt 192.168.0.250 mysql
``

- Simular um ataque usando uma Wordlist criada para senha em um serviço de Remote Desktop ( atr windows ):

``
hydra -v -l rogerio -P wl-edu 172.16.1.19 rdp
``

- Simular um ataque usando 2 Wordlists, uma pra login e outra para a senha. Atacando um serviço de FTP :

``
hydra -v -L users.txt -P senhas.txt  172.16.1.19 ftp
``

- Simulando um ataque com credencial defaults, em uma lista de hosts que obtemos por meio de outra análise :

``
hydra -v -l admin -p admin -M ips.txt ssh
``
