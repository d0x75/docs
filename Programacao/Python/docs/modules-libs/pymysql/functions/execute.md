execute() - Executar uma query

- Este methodo vem do arquivo cursors.py da lib pymysql
- O retorno desse methodo é um 'int' com o número de linhas afetadas.

_Parâmetros_:

- query = (str) Uma string com a query que vai ser executada.
- args = (tuplas,list,dict) - Parâmetros usados opcionalmente com a query


Nota:

Se args for uma lista ou tupla, %s poderá ser usado como um espaço reservado na consulta. Se args for um
dict, %(name)s pode ser usado como um espaço reservado na consulta.


---

*exemplos*:


...



