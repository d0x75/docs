select if(exists(select*from actor where actor.first_name = "PENELOPE"),"B.O EXISTENTE", if(exists (select * from actor where last_name = "GUINESS"),"EXISTE SIM", "NÃO EXISTE"));

select if (exists ( select * from actor where first_name is not null and last_name = "GUINES" ), 'ESSE CARA EXIST', 'ESSE CARA NÃO EXITE';);
  
  select if (500>10, "SIM","NAO")

  select 
id,
coalesce(fin_modalidade_id,0) as 'COALESCE',
fin_modalidade_id as 'DEFAUL',
ifnull(fin_modalidade_id,0) as 'IFNULL',
ide_notafiscal
from nota_cabecalho