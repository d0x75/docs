select 
id,
coalesce(fin_modalidade_id,0) as 'COALESCE',
fin_modalidade_id as 'DEFAUL',
ifnull(fin_modalidade_id,0) as 'IFNULL',
ide_notafiscal
from nota_cabecalho