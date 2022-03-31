Cláusula WHERE
---------------

Sintaxe:

	SELECT column1, column2, ...
	FROM pessoa
	WHERE condição;

- A instrução/cláusura WHERE é basicamente utilizada para filtrar registros de tabelas.
- Em suma, é usado para extrair apenas os registros que atendem determinada CONDIÇÃO ESPECÍFICA. ( condição que é setada para WHERE )

- Obs: A cláusula WHERE, não é apenas utilizada na instrução SELECT... Também pode ser utilizada na UPDATE,DELETE etc..


### Operadores possíveis, para interagir com a cláusula WHERE:

	" =	: Igual "	
	" > : Maior que "	
	" <	: Menor que "	
	" >=: Maior que ou igual "
	" <=: Menor que ou igual "	
	" <>: Diferente - não igual	
	" BETWEEN :	Entre um DETERMINADO intervalo ( é usado o operador AND para determinar o intervalo ) "
	" LIKE 	  :	Procura pelo padrão que preenchemos nas aspas após o LIKE "
	" IN	  : Para especificar múltiplos valores que serão possíveis na condição, esses valores são colocados em '()' "

### Exemplos de utilização da cláusula WHERE


- Uma cláusula WHERE que está criando uma condição para que os dados retornados pelo comando SELECT, sejam apenas os registros que na coluna 'uf' estão com o conteúdo = 'MG':

		select id,uf from pessoa
		where uf = "MG";

Nota: Campos numéricos NÃO DEVEM ser informados com ASPAS.

- Utilização da cláusula WHERE com a notação de negação (NOT). Dessa forma, temos um retorno ao inverso do acima.. pois os registros retornados NÃO TEM o conteúdo = "MG" na coluna 'uf'.

		select id,uf from pessoa
		where not uf = "MG";


- Utilização da cláusula WHERE, com "dupla condição". Em suma, além de checar a primeira condição, deverá ter outra condição indicada pela notação AND, que deve ser referente a OUTRA coluna da tabela.

		select uf from pessoa
		where uf = "MG" and genero = 'E';


- Utilização da cláusula WHERE, com outra "dupla condição". Nesse caso, além de checar a primeira condição, deverá ter outra condição indicada pela notação OR, que deve ser referente a MESMA coluna da tabela em questão.

		select * from pessoa
		where uf = "PR" or uf = "GO";