open() - Essa função abre um arquivo e o retorna como um objeto de arquivo.s

- _Sintaxe_ : 
open(file, mode='r', buffering=- 1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
- _Sintaxe simples_: open(file, mode)
- _Args_ : 
1. file = Caminho e nome do arquivo que é pra ser aberto.
1. mode =

		"r" - Leitura - Este é o Valor padrão. Abre um arquivo para leitura, erro se o arquivo não existir
		"a" - Append - Abre um arquivo para anexação, cria o arquivo se não existir
		(começa a inserir o texto no fim do arquivo)
		"w" - Write - Abre um arquivo para escrita, cria o arquivo caso não exista
		(O arquivo será esvaziado antes que o texto seja inserido na posição atual do fluxo de arquivo=0)
		"x" - Criar - Cria o arquivo especificado, retorna um erro se o arquivo existir

_Além disso você pode especificar se o arquivo deve ser tratado como modo binário ou texto_

		"t" - Text - Default value. Text mode
		"b" - Binary - Binary mode (e.g. images)

---

*Exemplos*:


- Abrir um arquivo da maneira mais simples:

		f = open("texto.txt","r")
		print(f.read())

- Abrir um arquivo que está em um local diferente do 'script.py's que estamos executando:

		f = open("C:\\texto.txt","r")
		print(f.read())


- Abrir um arquivo BINÁRIO, usando o mode 'rb' para conseguirmos ler/manipular arquivos binários :

		




....

