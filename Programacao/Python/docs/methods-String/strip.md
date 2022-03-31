*methodo* : strip() - romove os espaços no íncio e no fim da String que está no target.

- Caracter especial do espaço é o padrão a ser removido pelo strip(). Mais podemos passar argumentos para que outro
caractere seja removido também.

- _Sintaxe_ : string.strip(characters)

- _Args_ : 

> characters = Parâmetro opcional. Informar uma string com um conjunto de caracteres a serem removidos.

---

_exemplos_ :


- Remover apenas os espaços em branco, que é a definição padrão do deste méthodo :

		text = "        Pouso Alegre       "
		print(text.strip())


- Remover o conjunto de caracteres passado como argumento para o methodo strip() :

		text = "#####XXX----  Pouso Alegre  ----$$$$$$YYYYYY"
		print(text.strip('# X $ Y -'))
