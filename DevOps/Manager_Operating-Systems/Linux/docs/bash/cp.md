### cp

> Comando utilizado para fazer cópias de arquivos e diretórios


- Formas de utilizar:

> A forma mais simples é chamar o comando e primeiramente passar o arquivo a ser copiado, em seguida atribuimos o nome do arquivo em que a cópia vai entrar.

	cp input.txt output.txt

> Agora para copiarmos um diretório e arquivos que contiverem no mesmo, temos que passar a flag -a depois de chamarmos o comando.

	cp -a teste/ teste2

> Agora pra copiarmos arquivos para outros diretórios,usamos a flag -f depois de chamarmos o comando e depois o arquivo a ser copiado e o caminho a percorrer.

	cp -f arquivo.txt /home/user/teste

> Para copiarmos diretórios que contém arquivos e subdiretórios, iremos passar a flag -R depois de chamar o comando cp:

	cp -R Pasta/ /home/eduardo/testes
