mysqldump
----------


- Backup Mysql Local

``
mysqldump -u root -psenha erp > c:\diretorio\backup-erp.sql
``

- Backup Mysql Externo

``
mysqldump -u root -psenha -h client.ddns.net erp > c:\diretorio\backup.sql
``

- Backup Mysql Default

``
mysqldump -u root -psenha -x -e --routines -B erp > c:\diretorio\backup-erp.sql
``

- Criar novo banco de dados (procedimento feito antes da restauração) 

``
create database erp default character set utf8 default collate utf8_general_ci;
``

- Restauração de Backup Mysql

``
mysql -u root -psenha --database = erp < C:\backup.sql
``


------


mysqladmin
-----------


- Parar banco de dados remoto via TERMINAL:

``
mysqladmin -u root -psenha -h 192.168.1.2 -P3306 shutdown
``

- Atribuir senha ( para usuários que não tem senha )

``
mysqladmin --user=root password "senha01"
``

- Trocar senha do root

``
mysqladmin --user=root --password=senhatual password "senhanova"
``


------



mysql
------


- Exibir usuários 

``
select user from mysql.user;
``

- Deletar usuários

``
delete from mysql.user where  user = 'root';
``

- Fazer um cálculo ao conectar no mysql

``
mysql --user=root --password=gue55me -e "SELECT 1+1"
``

---


Criar usuário :
----------------

**Criar novo usuário**:

``
create user 'cliente'@'%' identified by 'TESTE123**';
``

**Setar permissões pro novo usuário**:

``
grant all privileges on *.* to 'cliente'@'%';
flush privileges;
``



Backup Mysql Linux
---------------------

``
mysqldump -u root -p -x -e --routines -B erp_name | sed -e 's/DEFINER=`.*`@`.*`\ //g' | gzip > local.sql.gz
``

