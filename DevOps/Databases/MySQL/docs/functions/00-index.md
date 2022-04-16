MySQL String Functions
-----------------------


List :


#### ASCII()


Função que retorna o símbolo da tabela ASCII, referente caracter passado como argumento.


Exemple query :

``
SELECT ascii('A');
``



------


MySQL Data Functions
-----------------------


------


MySQL Numeric Functions
-----------------------


------


MySQL Data Functions
---------------------


------


MySQL Advanced Functions
-------------------------


List :


#### COALESCE()


Exemple query :

``
select 
id,
coalesce(fin_modalidade_id,0) as 'COALESCE',
fin_modalidade_id as 'DEFAUL',
ifnull(fin_modalidade_id,0) as 'IFNULL',
ide_notafiscal
from nota_cabecalho
``

- Dica do JR :

Sobre COALESCE E IFNULL:
se vc não transformar o null em algo ele não entra na condição e ferra
tipo vc nao pode comparar um valor null sacou
tipo se null > 0 nao existe
aí nao pega a condição e ferra a sql
