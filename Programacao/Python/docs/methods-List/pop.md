*methodo* : pop() - Este méthodo remove o elemento na posição especificada.


- _Sintaxe_ : list.pop(pos)
- _Args_ : 

> pos = Argumento opcional. Um número especificando a posição do elemento que você deseja remover. 

PS: Quando não colocamos argumento o valor padrão é -1, que retorna o último item da array/lista


---

_exemplos_ :


- Usando o méthodo 'pop()' sem argumentos..então por padrão remover o último item da lista :

		idades = [10,20,30,40]
		idades.pop()
		print(idades)

- Usando o méthodo 'pop()' especificando nos argumentos para remover o segundo item da lista :

		idades = [10,20,30,40]
		idades.pop(1)
		print(idades)