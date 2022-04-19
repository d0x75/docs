ORDER BY
----------

Sintaxe:

	SELECT column1, column2, ...
	FROM table_name
	ORDER BY column1, column2, ... ASC|DESC;

- A instrução ORDER BY é usada para organizar o conjunto de resultados em ordem crescente ou decrescente.
- Por padrão, o ORDER BY classifica os registros em ordem crescente (ASC) mais podemos mudar para decrescente com a notação DESC.


### Exemplos de utilização da instrução ORDER BY

- Filtrando os registros em ordem decrescente, utilizando a notação DESC.

		select nome,uf from pessoa
		order by nome DESC;


- Filtrando os registros em ordem decrescente, utilizando a notação ASC.

		select nome,uf from pessoa
		order by nome ASC;

- Filtrando registros de uma coluna na forma crescente(ASC) e os registros da outra coluna na forma decrescente(DESC):

		select nome,uf from pessoa
		order by uf DESC, nome ASC;