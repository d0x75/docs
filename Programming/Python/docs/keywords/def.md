def - Essa keyword é usada para criar uma função no python.

*Exemplos*:


- Definir uma função simples, e depois fazer a chamada para a mesma :

		def printzao():
			print("Testando a keyword 'def'.")

		printzao()


- Definir uma função com 1 argumento e depois usar a função definida  :

		def mestats(mname):
			print(mnmae + "Is a Tech")

		mestats("Eduardo")
		mestats("Fernando")
		mestats("Bjorn")

- Uma maneira de pegar dados ou resutados de dentro da função e retornar-los para fora dela, podemos usar o *return*
do Python.


		def retornar():
			return 100

	    a = retornar()
	    print(a)

	    100


- Definir uma função com 2 ou mais argumentos depois usar a função definida  :


		def myname(primeiro,segundo):
			print("Nome completo = " + primeiro + " da " + segundo )

		myname(" Eduardo","Silva")


- Para definir uma função q ue não souber quantos argumentos serão passados para ela, adicione um * antes do nome do parâmetro na definição da função.


		def my_function(*kids):
  		print("The youngest child is " + kids[2])

		my_function("Emil", "Tobias", "Linus")


- Definir uma função que os argumentos enviados não estão da ordem :

		def my_function(child3, child2, child1):
  		print("The youngest child is " + child3)

		my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")


- Para definir uma função com argumentos de keywords e que não souber quantos argumentos serão passados para ela :


		def my_function(**kid):
	  	print("His last name is " + kid["lname"])

		my_function(fname = "Tobias", lname = "Refsnes")


- Definir uma função que tenha um parâmetro com valor Padrão :

		
		def my_function(country = "Norway"):
		  print("I am from " + country)

		my_function("Sweden")
		my_function()
		my_function("Brazil")


- Definir uma função e enviar uma lista como argumento, repare que ela ainda será uma lista após chegar à função:

		
		def my_function(food):
		  for x in food:
		    print(x)

		fruits = ["apple", "banana", "cherry"]

		my_function(fruits)


- Definir uma função que não possua um corpo com sua definição, poderá dar erros. Para evitar erro nessa situação usamos a notação _pass_ :

		def myfunction():
  		pass

 

---





- Para verificar o retorno ou fazer a função retornar algum valor, use a instrução _return_ :


		def my_function(x):
		  return 5 * x

		print(my_function(3))
		print(my_function(5))
		print(my_function(9))