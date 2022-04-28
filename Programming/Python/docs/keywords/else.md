else - Essa keyword é a usada em estruturas condicionais (como if:),e decide o que fazer se a condição for = False.

- Execute uma sequencia de código quando a condição atribuida ao if: for False.
- O 'else:' também pode ser usada em blocos try...except.

---

*Exemplos* :

- Exemplo básico do 'else' sendo usado em conjunto com o if na estrutura condicional if:

		x = 8
		if x >= 10:
			print("MAIOR QUE 10!")
		else:
			print("O numero nao maior que 10!!!")


- Exemplo básico do 'else' dentro de blocos try..except :
		
		# x=10  Quando não declarado entra na except

		try:
		  x < 10
		except:
		  print("Something went wrong")
		else:
		  print("The 'Try' code was executed without raising any errors!")