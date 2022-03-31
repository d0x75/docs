Get-Service
------------

- Para retornar todos os serviços do computador, e para retornar apenas os especificados em determinado computador. Ex:


		Get-Service

		Get-Service -Name "MysqlProducao"

		Get-Service -Name "MysqlProducao" -ComputerName "DESKTOP-O8DAVJ9"


- Para declarar uma variável, usamos por convenção o prefixo ' $ '. Exemplo de uma variável que guarda o retorno de um comando(que no caso é um objeto)



		$servico = Get-Service -Name "MysqlProducao" -ComputerName "DESKTOP-O8DAVJ9"


- A partir de termos uma variável de um objeto, podemos acessar cada um de seus atributos, Exemplo :

		$servico.Status

		$servico.Name

		$servico.DisplayName

		etc...
