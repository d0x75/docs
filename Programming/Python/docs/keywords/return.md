return - Essa keyword é usada para sair de uma função(def:) e retornar um valor.

- Se houver algum trecho de código no escopo da função, após a chamada no 'return'.. este não será
executado , devido o return sair da função.


*Exemplos*:


- Exemplo simples.. Sair da função e retornar um valor. ( 3+3+3=9 )

		def ret():
		    return 3+3+3

		print(ret())


- Nese caso, observe que há um 'print' após a chamada do 'return'.. que não vai ser executado :

		def ret():
		  return 3+3
		  print("Hello, World!")

		print(ret())