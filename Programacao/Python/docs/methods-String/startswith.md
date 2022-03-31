*methodo* : startswith() - Verifique se a string começa com a palavra passada como argumento obrigatório.

- O método startswith() retorna True se a string começar com o valor especificado, caso contrário, False.

- _Sintaxe_ : string.startswith(value, start, end)
- _Args_ :  

> value = É um argumento é requerido (obrigatório). Esse é o valor que o méthodo para verificar se a string começa com ele.
> start = Esse argumento é opcional. Aqui informamos um valor inteiro que especifica a posição para iniciar a pesquisa.
> end   = Esse argumento é opcional. Aqui informa um valor inteiro que especificar a posição onde termina a pesquisa.


---

_exemplos_ :

- Uso simples da startswith() em uma estrutura condicional :


		luladrao = "Lula esta querendo voltar a cena do crime"
		if luladrao.startswith("Lula"):
			print(luladrao)
		else:
			print("VAI BOLSOMITO")


