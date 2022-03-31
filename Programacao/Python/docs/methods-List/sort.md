*methodo* : sort() - Este método classifica e retorna a lista em ordem crescente por padrão.

- Também podemos criar uma função para decidir o(s) critério(s) de classificação.


- _Sintaxe_ : list.sort(reverse=True|False, key=myFunc)
- _Args_ : 

> reverse = Argumento opcional. reverse=True , classificará a lista de forma decrescente. 
O padrão é reverso=Falso / ascendente.

> key = Argumento opcional. Uma função para especificar os critérios de classificação.


---

_exemplos_ :


- Usando o méthodo 'sort()' de forma básica em uma lista, para retorna-la em ordem crescente.

		idades = [15,20,30,40,10,85,10]
		idades.sort()
		print(idades)

- Usando o méthodo 'sort()' com o argumento 'reverse' para retornar a lista em ordem decrescente

		idades = [15,20,30,40,10,85,10]
		idades.sort(reverse=True)
		print(idades)

- Usando o méthodo 'sort()' com o argumento 'key', e criando uma função para instanciar o argumento key, que fará o 'sort()' retornar a lista ordedana pelo comprimento dos valores :

		def myFunc(e):
		  return len(e) # < 5

		cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
		cars.sort(key=myFunc)
		print(cars)

- Usando o méthodo 'sort()' com o argumento 'key', e criando uma função para instanciar o argumento key, que retorna uma lista de dicionários com base no valor de 'year' do dicionário:

		def myFunc(e):
		  return e['year'] # == 2019

		cars = [
		  {'car': 'Ford', 'year': 2005},
		  {'car': 'Mitsubishi', 'year': 2000},
		  {'car': 'BMW', 'year': 2019},
		  {'car': 'VW', 'year': 2011}
		]

		cars.sort(key=myFunc)
		print(cars)


- Usando o méthodo 'sort()' com os argumentos 'reverse' E 'key', e criando uma função para instanciar o argumento key, que fará o 'sort()' retornar a lista ordenada pelo comprimento novamente, porém com a ordem invertida.. por conta do argumento 'reverse' :


		def myFunc(e):
		  return len(e)

		cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
		cars.sort(reverse=True, key=myFunc)
		print(cars)