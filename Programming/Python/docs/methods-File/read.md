*methodo* : read()

- Vai ler e retornar todo conteúdo do arquivo passado como argumento ao métedo. O método read() retorna o número especificado de bytes do arquivo. O padrão é -1, o que significa o arquivo inteiro.

- _Sintaxe_ : file.read()
- _Args_ : 
size - Esse Arg é Opcional. O número de bytes a serem retornados. Padrão -1, o que significa o arquivo inteiro.

---

_exemplos_:

- Abrir um arquivo, ler o arquivo inteiro e retornar todos os bytes do arquivo :

		f = open('teste.sql','r')
		print(f.read())

- Abrir um arquivo, ler o arquivo inteiro e retornar apenas os 5 primeiros bytes :

		f = open("C:\\texto.txt", "r")
		print(f.read(5))