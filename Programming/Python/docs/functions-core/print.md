Função incorporada do Python.

---

print() - imprime a mensagem especificada na tela ou outro dispositivo de saída padrão. 

- A mensagem pode ser uma string, ou qualquer outro objeto, o objeto será convertido em uma
string antes de ser escrito na tela.


- _Sintaxe_ : print(object(s), sep=separator, end=end, file=file, flush=flush)

- _Args_ : 

> object(s) : Qualquer objeto, e quantos você quiser. Será convertido em string antes de ser
impresso

> sep='separator' : Argumento opcional. Especifique como separar os objetos, se houver mais de um. O padrão é ' '(1 espaço em branco)

> end='end'	: Argumento opcional.Especifique o que imprimir no final. O padrão é '\n'.

> file : Argumento opcional. Um objeto com um método de gravação. O padrão é sys.stdout.

> flush : Argumento opcional. Um booleano, especificando se a saída é liberada (True) ou
armazenada em buffer (False). O padrão é False

---


*exemplo* :


- Exemplo da função 'print()', imprimindo mais de 1 objeto :

		print("Ola", "Bom dia Pessoal", 0xff)

- Exemplo da função 'print()', imprimindo os dados de uma tupla :

		tuplinha = ('verde','boldo','alecrim')
		print(tuplinha)

- Exemplo da função 'print()', usando o argumento 'sep='separator', que vai mudar o jeito de
separa as palavras na impresssão de strings :

		print("Boa tarde Jovens", "Tudo bem" ,100 , "%" ,sep=" ---- ")



	