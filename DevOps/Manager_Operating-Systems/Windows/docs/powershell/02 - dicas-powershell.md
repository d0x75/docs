Dicas de Powershell p/ Scripts
-------------------------------

#### Apóstrafos


- Quando formos escrever um comando aninhado no powershell,  usamos a ' ` ' no final de toda linha`


		alias do Select-Object = select
		alias do Where-Object = ?


- Sempre que formos quebar nosso script no terminal, usamos para delimitar cada linha o " | ", pois ele vai isolar cada comando do script que tiver setado "|" no final.

- Para quebrar nossos argumentos de comandos, ( tipo o do select), usamos ` ` `


##### Virgulas


- Quando vemos uma ' , ' indica pro powershell que trata-se de uma array. Exemplo

		(1,2).GetType()


- Mais quando precisamos criar uma array vazia ou com apenas 1 valor.. já não conseguiremo, devido não ter vírgula indicando array.
- Nesse caso usamos um caracter que indica com Prioridade que o dado a seguir é uma array. Esse caracter é o " @ ". Exemplo :


		@().GetType().name
		@(1).GetType().name


---


Hash tables - Estrutura de dados
---------------------------------


- Criar um HashTable:
		

		@{}.GetType()


- Declarando as variáveis do nosso script, no formato de hashTables. Exemplo usado:


		$nameExpr = @{}
		$nameExpr.Add("Label", "Nome")
		$nameExpr.Add("Expression", { $_.Name })

		$lengthExpr = @{}
		$lengthExpr.Add("Label", "Tamanho")
		$lengthExpr.Add("Expression", "{{0:N2}KB" -f ($_.Length / 1KB) })
		$param = ($nameExpr,$lengthExpr) 


- Declarando as variáveis do nosso script, no formato de hashTables, AGORA DA MANEIRA CORRETA e ENXUTA :

		$nameExpr = @{
			Label = "Nome",
			Expression = { $_.Name }
		}

		$lengthExpr = @{
			Label = "Tamanho",
			Expression = {"{0:N2}KB" -f ($_.Length / 1KB) }
		}


#### Observações:


- Quando se tratar de HashTables e não de Arrays, a separação dos argumentos é feita via ' ; '.  Diferente da array que é a ' , '.



---


Contexo de execução do Powershel
-----------------------------------


- No powershell existem conextos de execução, um terminal do powershell aberto indica que o contexo do script do terminal, é um contexto FILHO em relação ao contexto de script PAI do poweshell.


- Quando abrimos um terminal ( contexto filho), temos acesso as variáveis do contexto pai, porém quando alteramos o valor destas, essa alteração só é feita em contexto filho.


- Se por acaso declararmos uma variável privada ( $private:varname ), não herdaremos ela no contexto filho.. nesse caso se tentarmos usar-la, não terá dados.


---


acessar regedit via Powershell
--------------------------------


1. As chaves de registros na prática tem a mesma estrutura dos discos locais. Para verlas fazemos o seguinte no ps :

		get-psdrive

2. Acessar a HKEY_LOCAL_MACHINE , fazer o seguinte no PS :

		cd HKLM:\


3. Ir até o diretório e verificar oq tem salvo no diretório do registro do windows que apontarmos com o '-Path'. fazer o seguinte no PS :

	Set-Location -Path HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Run\
	dir

4. Verificar as chaves de registros e criadas dentro da pasta apontada pelo '-Path'. Fazer o seguinte pelo PS :

	Get-Item -Path HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Run\
	
