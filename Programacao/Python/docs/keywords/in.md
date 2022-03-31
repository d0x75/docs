in - essa keyword tem 2 propósitos :

- Verificar se um valor está presente em uma sequência (lista, intervalo, string etc.).
- Usado sempre em conjunto com o for, Para percorrer uma sequência em um loop for:

---

*Exemplos* :


- Usando a keyword como conjunto para fazer um loop for: 


		for x in range(1,10):
			print (x)


- Usando a keyword para verificar um valor em uma lista :


		lista = ['Programacao','Seguranca','RedTeam']

		if 'BlueTeam' in lista:
			print("Contem na lista\n")
		else:
			print("NÃO ENCONTRADO...\n")