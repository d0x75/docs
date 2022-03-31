*methodo* : split() - Esse método Divide uma string em uma array onde cada palavra é um indice da array:

- Divide uma string em uma lista.
- Você pode especificar o separador, o separador padrão é qualquer espaço em branco.

Nota: Quando maxsplit for usado, a lista conterá o número especificado de elementos mais um. (devido o default ser -1)


- _Sintaxe_ : string.split(separator, maxsplit)
- _Args_ : 

> separator = Este parâmetro é opcional. Especifica o separador a ser usado ao dividir a string. Por padrão, qualquer espaço em branco é um separador
> maxsplit = Este parâmetro é opcional.Especifica quantas divisões fazer. O valor padrão é -1, que é "todas as ocorrências


---

_exemplos_ :


- Exemplo de uso do methodo 'split()' para separar a string modificandoo o separador para o caracter 'x'.


		text = "Eduardo x Esmenia x Empatia"
		y = text.split('x')
		print (y)



- Exemplo de uso methodo 'split()' , para mostrar apenas o primeiro item da lista e usando o separador padrão.

		text = "welcome to the jungle"
		x = text.split()[0]
		print (x)


- Exemplo usando os 2 argumentos possíveis para este methodo. Modificando o separador para '#' e o maxsplit para 1 que no caso vai retornar uma lista com apenas 2 argumentos. ( -1...0,1)


		txt = "apple#banana#cherry#orange"
		x = txt.split("#", 1)
		print(x)


