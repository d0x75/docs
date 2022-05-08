Get-ChildItem
--------------


_PS : seu alias é o comando 'dir'_


- Além de listar os diretórios, lista os arquivos e subdiretórios dividos na tela. Resumindo, lista todos os arquivos separados por diretório.


		dir -Recurse


-  Armazenar a quantidade de Itens listadas com o '-Recurse' do comando dir.

		
		$todosItens = gci -Recurse
		$todosItens.Length

- Armazenar a quantidade de arquivos dentro de uma variavel, adicionando a notação '-File' pra filtrar só os arquivos desta vez : 


		$todosArquivos = gci -Recurse -File
		todosArquivos.Length