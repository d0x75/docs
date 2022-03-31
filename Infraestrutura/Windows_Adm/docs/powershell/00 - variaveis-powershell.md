Variáveis Padrão do Powershell
-------------------------------


**$env:path**

- Acessar o Objeto das variável de ambiente 'Path' do windows. Exmplo :

		echo $env:path


---

**$profile**


- Comando que consegue ver o profile(perfil em execução) do poweshell atual:

		$profile


- Criar o arquivo do profile do powershell, como o argumento do 'new-item' é o caminho + nome do arquivo.. podemos usar a variável abaixo:


		New-Item $profile

- Também é possível criar o arquivo de profile GERAL que afetara qualquer usuário do computador. Ao contrário da variável $profile que cria o arquivo de perfil apontando pra pasta do usuário current. Para isso complementamos a variável $profile :


		New-Item $profile.AllUsersAllHosts


_Então, tudo que for escrito nesses arquivos profile.ps1 serão executados automaticamente quando o powershell for aberto_


---


**Variável global de erro**

- Variável global de erro do Powershell = ErrorActionPreference



**param**

- Palavra reservada do powershell ( param ) para referenciar parâmetros que são utilizados no momento da execução de um script. Exemplo de uma declaração simples de parâmetros

		
		param($tipoDeExportacao)