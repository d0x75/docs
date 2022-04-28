Função incorporada do Python.

---

type() - Esta função apenas retorna o tipo do objeto especificado. 

- PS : 



- _Sintaxe_ : type(object, bases, dict)

- _Args_ : 

>object = Argumento requerido (obrigatório). Se apenas este parâmetro for especificado, a função
type() retornará o tipo deste objeto.

>bases = Argumento opcional. Usado para especificar as classes base.

>dict = Argumento opcional. Especifica o namespace com a definição para a classe.


---


*exemplo* :

- Exemplo básico da utilização da função 'type()', para vermos os tipos de dados declarados :

		a = ('apple', 'banana', 'cherry')
		b = "Hello World"
		c = 33

		x = type(a)
		print(x)
		y = type(b)
		print(y)
		z = type(c)
		print(z)



