*methodo* : close() - Usado para fechar um arquivo depois de aberto.

- Sempre fechar os arquivos que usamos no programa, é uma boa prática de programação.

Nota: Você deve sempre fechar seus arquivos, em alguns casos, devido ao buffer, as alterações feitas em um arquivo podem não aparecer até que você feche o arquivo.


- _Sintaxe_ : file.close()
- _Args_ : No Args!


---

_exemplo_ :

	f = open("teste.sql", "r")
	print(f.read())
	f.close()