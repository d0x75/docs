### apt-get

Comando utilizado para fazer instalação de programas/pacotes no Linux. Além de instalaçao, também remove programas , atualiza e faz upgrades.


- Local onde fica as URLs dos repositórios que espelham os pacotes/programas para o sistem :

``/etc/apt/sources.list``


Repositório espelho principal do KaliLinux :

``
deb http://old.kali.org/kali sana main non-free contrib
# For source package access, uncomment the following line
# deb-src http://old.kali.org/kali sana main non-free contrib
``


- Depois de colar o conteúdo acima no sources.list, usamos os comandos :

``apt-get update``
``apt-get upgrade``


- Instalar um programa usando apt-get. Exemplo :
		
``apt-get install``
``apt-get install crunch``

- Remover programa / pacote do sistema , usando o apt-get . Exemplo :

``apt-get remove``
``apt-get remove mysql``




