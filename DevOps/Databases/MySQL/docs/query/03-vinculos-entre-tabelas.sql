select 
TABLE_NAME,
COLUMN_NAME,
REFERENCED_TABLE_NAME
from information_schema.KEY_COLUMN_USAGE
where table_schema = :banco 			# colocar o nome do banco de dados
and referenced_table_name = :tabela 	# colocar a tabela que quero achar o relacionamento
ORDER BY TABLE_NAME