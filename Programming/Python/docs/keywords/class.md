class - Esta keyword é usada para criar uma classe.


- Uma classe é como um construtor de objetos, ou um "projeto" para criar objetos.

- Para entender o significado das classes, temos que entender a função __init__() embutida.

- Todas as classes possuem uma função chamada __init__(), que sempre é executada quando a classe está sendo iniciada.

NOTA : A __init__()função é chamada automaticamente toda vez que a classe está sendo usada para criar um novo objeto.

- O parâmetro 'self' é uma referência à instância atual da classe e é usado para acessar as variáveis que pertencem à classe.

- Ele não precisa ser nomeado self, você pode chamá-lo como quiser, mas deve ser o primeiro parâmetro de qualquer função da classe:

NOTA : O parâmetro "self" é uma referência à instância atual da classe e é usado para acessar variáveis que pertencem à classe.

---


*exemplos*:


- Criar uma class, com uma propriedade chamada x :

		class MinhaClasse:
			x = 5
		
- Criar um objeto usando a classe criada acima :

		class MinhaClasse:
			x = 5
		p1 = MinhaClasse()
		print(p1.x)

PS : Os exemplos acima são classes e objetos em sua forma mais simples e não são realmente úteis em aplicações da vida real


- Criar uma classe com o escopo vazio :
("Se por algum motivo a classe não tiver conteúdo , coloque a instrução 'pas's para evitar erro")


		class Person:
		  pass


- Criar uma classe que vai herdar os métodos e propriedades de outra classe :
(A Classe "Estudante" que vai herdar os métodos e propriedades da classe "Escola")


		class Estudante(Escola):


- Criar uma clase, implementando o a função __init__ e usando o parâmetro 'self' para seguir os padrões
da criação da classe  :

		class Pessoa:
			def __init__(self,nome,idade):
				self.nome = nome
				self.idade = idade

		p1 = Pessoa("Eduardo",26)
		print(p1.nome,p1.idade)


- Criar uma classe que alem dos padrões mecionados acima, vai conter um méthodo que criamos dentro da
classe para ser usado :


		class Pessoa:
			def __init__(self,nome,idade):
				self.nome = nome
				self.idade = idade

			def minhaFuncao(self):
				print("Ola meu nome eh " + self.nome)

		p1 = Pessoa("Eduardo",26)
		p1.minhaFuncao()


- Criando uma classe que use o argumento 'self', porém mudando o mesmo de nome. (pode ser qlqr nome)


		class Pessoa:
			def __init__(dudsdev,nome,idade):
				dudsdev.nome = nome
				dudsdev.idade = idade

			def naBala(onetwotree):
				print("Ola " + onetwotree.nome)


		p1 = Pessoa("Eduardo",26)
		print(p1.nome,p1.idade)
		p1.naBala()



- Alterar valores de variaveis da classe, nesse exemplo imprimimos o valor antigo e depois o novo :

		p1 = Pessoa("Eduardo",26)
		print(p1.nome,p1.idade)
		p1.idade = 27
		print(p1.nome,p1.idade)


- Excluir valores de propriedades da classe, nesse exemplo quando tentamos chamar o metodo naBala() após usar o 'del p1.idade' ; Já não iremos conseguir por conta do 'del' que foi executado :


		p1 = Pessoa("Eduardo",26)
		print(p1.nome,p1.idade)
		p1.idade = 27
		p1.naBala()
		del p1.idade
		p1.naBala()