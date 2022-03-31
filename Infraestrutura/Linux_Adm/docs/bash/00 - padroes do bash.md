Sacadas e Dicas sobre bash do linux
------------------------------------

- Todo script que que criarmos tem que começar com a seguinte notação:

	#!/bin/bash

- Localização dos manuais do Linux:

	``cd /usr/share/man``

- Diretório raiz do sistema ( igual o C:\ do windows )

	``/``

- Quando o bash indica que está no diretório do usuário atual.

	``$``

- Quando o bash indica que está em contexto de usuário root.

	``#``

- Alias para o diretório dod usuário atual.

	``~``


- No Linux conseguimos usar alguns comandos ( ls,cd,mkdir ETC..) sem passar o caminho deles na hora de executar-los, devido os mesmos estarem armazenados em locais que estão setados nas variáveis de ambiente do sistema. Comando para verificar as variáveis de ambiante do sistema:

``env | grep PATH``

``echo $PATH``


---

- Operadores lógicos do Bash

		lt (menor que)
		gt (maior que)
		le (menor ou igual)
		ge (maior ou igual)
		eq (igual)
		ne (diferente)
		e( checa se existe ou não)

- IF / ELSE


		{
		if [ "$0" ] - Indica o próprio programa.
		if [ "$1" ] - Indica o primeiro argumento que está sendo passado.
		if [ "$2" ] - Indica o segunda argumento que está sendo passado.
		}


- For (enquanto)

		for ip in {1..10};
		do echo 102.168.0.$ip;
		done

		for ip in $(seq 1 254);$ip;done



- Exemplo em Script :

		echo "Qual a sua idade?"
		read idade
		if[ "$idade" -ge "18"] #Checa se a idade é >= 18
		then #entao executa uma acao
		echo "Voce pode dirigir"
		else #senao executa outra acao
		echo "VOce NAO pode dirigir"
		fi #finalizando o if

		echo {1..100}
		seq 1 100

