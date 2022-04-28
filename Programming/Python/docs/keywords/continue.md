continue -  essa keyword usada para encerrar a iteração atual em um loop for (ou while) e continuar até a próxima iteração.

- Normalmente é utilizado para validar e eventualmente encerrar a iteração atual do loop, e continuar a execução do loop.

---

*Exemplos* :


- Exemplo simples do uso da keyword 'continue' :

		i = 0
		while i < 9:
		  i += 1
		  if i == 3:
		    continue
		  print(i)



- Exemplo simples do uso desta keyword, dentro de um loop for :


		for i in range(9):
		  if i == 3:
		    continue
		  print(i)