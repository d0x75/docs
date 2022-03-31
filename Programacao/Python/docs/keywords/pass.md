pass - Uma declaração nula, uma declaração que não fará nada

- A instrução 'pass' é usada como um espaço reservado para código futuro.
- Quando a 'pass' é usada, nada acontece, mas você evita um erro quando o código vazio não é permitido.
- Código vazio não é permitido em loops, definições de função, definições de classe ou em instruções if.

---


*Exemplos*:


- Exemplo usando a keyword 'pass' , para ajustar uma def de uma função que não há dados :

		def myfunction():
		  pass

- Exemplo usando a keyword 'pass' , para ajustar uma declaração de uma classe que não há dados :

		class Person:
		  pass

- Exemplo usando a keyword 'pass' , em uma estrutura if que não há dados após a condicional :

		a = 33
		b = 200

		if b > a:
		  pass
