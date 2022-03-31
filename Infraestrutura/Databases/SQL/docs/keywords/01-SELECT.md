SELECT *
----------



Sintaxe:

	SELECT column1, column2, ...
	FROM pessoa;

- Essa instrução é utilizada para selecionar dados de um banco de dados.
- Os dados retornados são armazenados em uma TABELA de resultados, chamada de CONJUNTO DE RESULTADOS.


### Exemplos de utilização da instrução SELECT

- Selecionar todos os registros da tabela 'pessoa', vamos utilizar o símbolo ' * ' para isso.

		select * 
		from pessoa

- Selecionar colunas específicas(id e nome) da tabela 'pessoa'.

		select id,nome
		from pessoa


---


SELECT DISTINCT
----------------



Sintaxe:

	SELECT DISTINCT column1, column2, ...
	FROM pessoa;

- A instrução SELECT DISTINCT é usada para retornar apenas valores distintos (diferentes).
- Em suma, caso tenha mais de 1 registro com valores iguais/duplicados, será retornado apenas 1 desses registro.


### Exemplos de utilização da instrução SELECT DISTINCT

- Selecionar todos os Ceps da tabela 'pessoa', sem repitir nenhum Cep.

		select distinct cep from pessoa;

- Faz a mesma seleção do comando anterior, porém retorna apenas a QUANTIDADE de registros ÚNICOS (sem repetir).

		select count(distinct cep)  from pessoa;