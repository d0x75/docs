BACKUP DO REGISTRO DO WINDOWS
-----------------------------

- Os arquivos citados acima são os que entraram no backup ou seja são os fundamentais.

1. Reiniciar o computador apertando F8
2. Escolher a opção ' Modo de reparação ' ou mode of Debugin
3. Agora quando chegar na tela System Recovery Options (opções de reparação do sistema), escolhemos a última opção do PROMPT de comandos (cmd)
4. Faremos a copia do registro do windows via prompt da seguinte forma:

	criar uma pasta no diretório raiz( c:,d: ou e:) com o seguinte comando:

	``md backup-windows``
	
	entrar no diretório onde estão os arquivos do registro do windows que precisam ser copiados:

	``cd windows\system32\config``

	copiar os arquivos do system32\config

	``
	copy SAM d:\backup-windows
	copy DEFAULT d:\backup-windows
	copy SECURITY d:\backup-windows
	copy SOFTWARE d:\backup-windows
	copy SYSTEM d:\backup-windows
	``
	

	agora para restaurar o backup, copiamos os 5 arquivos que foram salvos em d:\backup-windows para o seguinte caminho:

	``
	C:\Windows\system32\config
	yes
	``