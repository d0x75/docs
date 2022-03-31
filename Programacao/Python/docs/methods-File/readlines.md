*methodo* : readlines()


- Retorne todas as linhas do arquivo passado ao methodo, como uma lista onde cada linha é um item no objeto de lista:


- _Sintaxe_ : file.readlines()
- _Args_ : 
hint - Este argumento é Opcional. Se o número de bytes retornado exceder o número 'hint', não serão retornadas mais linhas. O valor padrão é -1, o que significa que todas as linhas serão retornadas.


---


_exemplos_:


- 


	f = open('teste.sql','r')
	print(f.readlines())