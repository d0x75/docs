## Diferenças entre os JOINS

		
INNER JOIN : Retorna registros que possuem valores correspondentes em ambas as tabelas.

		select p.id,p.descricao,p.ncm,p.cest,pp.nome,pp.id from produto p
		inner join pessoa pp on pp.id = p.fornecedor_id;

LEFT OUTER JOIN : Retorna todos os registros da tabela da esquerda e os registros correspondentes da tabela da direita.

		select p.id,p.descricao,p.ncm,p.cest,pp.nome,pp.id from produto p
		left outer join pessoa pp on pp.id = p.fornecedor_id;

RIGHT OUTER JOIN : Retorna todos os registros da tabela da direita e os registros correspondentes da tabela da esquerda.

		select p.id,p.descricao,p.ncm,p.cest,pp.nome,pp.id from produto p
		right outer join pessoa pp on pp.id = p.fornecedor_id;


FULL OUTER JOIN : Retorna todos os registros quando há uma correspondência na tabela da esquerda ou da direita.

...



