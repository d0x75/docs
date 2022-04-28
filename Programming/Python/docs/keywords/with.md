with - Essa keyword é usada para simplificar o tratamento de exceções.

- O comando with serve para facilitar a escrita de qualquer bloco de código que envolva recursos que precisam ser "finalizados" (isso é, restaurados, liberados, fechados, etc... ) depois que o bloco for encerrado - e ele permite que isso seja feito de forma automática, com a lógica de finalização dentro do objeto utilizado.

- Então primeira coisa: o código de finalização do with sempre é executado - não importa se um erro ocorreu dentro do bloco do with ou não.

---

*Exemplos* :


- Exemplos práticos do uso do 'with', na hora de tratar abertura de arquivos. JEITO ERRADO :

		f = open("data.txt", "w")
		# codigo usando o arquivo f
		f.close()


- Novamente o uso do 'with',na hora de tratar abertura de arquivos. JEITO CERTO SEM O 'with' :

		try:
		   f = open("data.txt", "w")
		   # codigo usando o arquivo f
		finally:
		   f.close()

- Novamente o uso do 'with',na hora de tratar abertura de arquivos. JEITO CERTO USANDO O 'with':


		with open("data.txt", "w") as f:
		   # codigo usando o arquivo f




