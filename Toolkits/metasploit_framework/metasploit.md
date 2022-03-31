## METASPLOIT UNLEASHED


### Intro

- O que é Metasploit :

O Metasploit Framework (MSF) é muito mais do que apenas uma coleção de exploits - é também uma base sólida que você pode construir e personalizar
facilmente para atender às suas necessidades. Isso permite que você se concentre em seu ambiente-alvo exclusivo e não precise reinventar a roda. 


----


### Install VM Metasploitable


- Download em SourceForget : 
https://sourceforge.net/projects/metasploitable/

- Criar máquina virtual Linux, e apontar o disco rígido para o arquivo .VMDK que baixamos acima.

- Bootar a máquima, e fazer o login com as credenciais padrão : msfadmin/msfadmin

----


### METASPLOIT ARCHITECTURE

Esse framework é desenvolvido em Ruby a vários anos, então ele é beeem robusto.

#### METASPLOIT FILESYSTEM AND LIBRARIES


- No kali linux o Metasploit Framework é fornecido pelo pacote : 'metasploit-framework'

- No kali linux o Metasploit fica instalado no seguinte caminho : 'usr/share/metasploit-framework'


#### Metasploit Filesystem

O sistema de arquivos do Metasploit é organizado por diretórios de uma maneira bem intuitiva.

- DATA ( diretório que contém dados editaveis do Metasploit, para aramzenar binários, wordlists etc.. )
Fica em : 'usr/share/metasploit-framework/data'

- DOCUMENTATION ( documentação do framework 'localhost' )
Fica em : '/usr/share/metasploit-framework/documentation/'

- LIB ( contém o coração do framework rs ) 
Fica em : '/usr/share/metasploit-framework/lib/'

- MODULES ( esse diretório é onde encontramos os módulos do MSF, como modulo de exploits, payloads encoders etc..
Fica em : '/usr/share/metasploit-framework/modules/'

- PLUGINS (o Metasploit inclui muitos plug-ins, que você encontrará neste diretório.)
Fica em : '/usr/share/metasploit-framework/plugins/'

- SCRIPTS ( O diretório de scripts contém Meterpreter e outros scripts. )
Fica em : '/usr/share/metasploit-framework/scripts/'

- TOOLS (O diretório de ferramentas possui vários utilitários de linha de comando úteis)
Fica em : '/usr/share/metasploit-framework/tools/'

#### Bibliotecas Metasploit

- Existem várias bibliotecas MSF que nos permitem executar nossos exploits sem ter que escrever código adicional para tarefas rudimentares.
- Bibliotecas mais importantes :

**REX**
- a biblioteca Base que lida com a maioria das tarefas 
- lida com sockets, protocolos, transform text e outros.
- SSL, SMB, HTTP, XOR, Base64, Unicode

**MSF::CORE**
- Fornece a API Básica para o funcionamento.
- Define o Metasploit Framework.

**MSF::BASE**
- Fornece uma API amigável.
- Fornece APIs simplificadas para o uso no framework.


----



### Módulos e localização


- Todos os módulos Metasploit são organizados em diretórios separados, de acordo com sua finalidade. 
Uma visão geral básica dos vários tipos de módulos Metasploit é mostrada abaixo.


EXPLOITS
No Metasploit Framework, os módulos de exploits são definidos como módulos que usam payloads.

AUXILIARES
Os módulos auxiliares tem  scanners, fuzzers, sniffers etc..

PAYLOADS, ENCODERS, NOPS
Os payloads consistem em código que é executado remotamente, enquanto os encoders garantem que os payloads cheguem intactos ao seu destino. 
Nops mantém os tamanhos dos payloads consistentes em todas as tentativas de exploração.


---

 
METASPLOIT FUNDAMENTALS

### USING THE MSFCLI INTERFACE


- O msfcli fornece uma interface de linha de comando poderosa para a estrutura. 
Isso permite que você adicione facilmente exploits Metasploit em qualquer script que você possa criar.

**msfcli FOI REMOVIDO EM 2015 do framework**


---


### USING THE MSFCONSOLE INTERFACE


- O msfconsole é provavelmente a interface mais popular para o Metasploit Framework (MSF). 
- Ele fornece um console centralizado “tudo-em-um” e permite acesso eficiente a praticamente todas as opções disponíveis no MSF. 













