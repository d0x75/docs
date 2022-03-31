*methodo* : readline() - Retorna uma linha do arquivo.

- Você também pode especificar quantos bytes da linha devem ser retornados, usando o parâmetro size.


- _Sintaxe_ : file.readline(size)

- _Args_ : 
size - Este argumento é Opcional. O número de bytes da linha a ser retornada. Padrão -1, o que significa toda a linha.


---


_exemplos_:

	f = open('teste.sql','r')
	print(f.readline())