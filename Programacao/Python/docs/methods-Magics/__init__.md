__init__() - Esta Função Mágica, é o construtor de uma classe.

_Parâmetros_:


Nota: Essa função é executada no momento em que a classe é instanciada em algum objeto.

---

*exemplos*:


- Exemplo de uso básico do método mágico referente a este Doc :



		class Carros:
			def __init__(self,nome,marca):
				self.nome = nome
				self.marca = marca


		# Método mágico é executado aqui, quando instanciamos a classe
		x = Carros('Etios','TOYOTA')

		print(x.nome)
		print(x.marca)

