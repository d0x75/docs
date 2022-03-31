CRIANDO SCRIPTS PRO REGISTRO DO WINDOWS
----------------------------------------

- Podemos escrever os scripts em um documento texto qualquer, mais temos que salva-lo com a extensão  .reg ( de regedit ).
- Também temos que setar algumas informações no cabecalho do arquivo em que o script será escrito, para que o windows entenda que se trata de um script para o registro do sistema.

		Windows Registry Editor Version 5.00

- Nos registros do windows temos as CHAVES que foram mencionadas acima e dentro delas temos as SUBCHAVES que sua vez arnmazena arquivos de configuração que na maioria das vezes tem os seguintes valores : REG_Z ( Z quer dizer strings "conjunto de caracteres ") e DWORD que são uma sequência de bytes. Na maioria das vezes na tela do regedit temos informações desses arquivos que ficam nas subchaves como : Nome,Tipo(Z , DWORD etc..) e Dados.


- Para criar uma nova chave, por exemplo dentro de CURRENT_USER, podemos utilizar um script dessa forma:

		Windows Registry Editor Version 5.00

		[HKEY_CURRENT_USER\MyKey]

- Se por acaso quiser excluir a chave que criamos acima ou até mesmo outra, utilizamos o operação de SUBTRAÇÃO antes da chave principal, o script ficara desse jeito:

		Windows Registry Editor Version 5.00

		[-HKEY_CURRENT_USER\MyKey]


- Também posso criar uma nova chave já com um arquivo dentro da mesma, no exemplo um arquivo do tipo texto : 


		Windows Registry Editor Version 5.00

		[HKEY_CURRENT_USER\MyKey]
		*TextArea*=*Eduardo Barbosa*

