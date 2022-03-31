Dicas para utilização do FireBird:
-----------------------------------

- Observações:

	extensão .fdb =  Banco de dados em funcionamento
	extensão .fbk =  Formato do banco de dados após ter sido feito o backup do mesmo. 

Acessar Firebird via cmd:
-------------------------

1. Instalar o Firebird 2.5

2. Colocar o caminho "C:\Program Files\Firebird\Firebird_2_5\bin", nas variáveis de ambiente do sistema.

3. Acessar algum banco de dados firebird, via cmd:

		isql 
		connect "C:\teste\teste.fdb" user sysdba password masterkey;
		

Forma de verificar a versão do Firebird, via cmd:
--------------------------------------------------

		isql  -Z
	
	
Exportar dados do banco de dados para .txt, via cmd :
------------------------------------------------------

		isql
		connect "C:\teste\teste.fdb" user sysdba password masterkey;
		output C:\dados.txt;
		select * from cadastros;
		output;
	

Fazer um backup de banco de dados FireBird, via cmd :
------------------------------------------------------

	gbak -user SYSDBA -pas masterkey localhost:c:\DJSYSTEM\MONITOR\DJPDV.fdb c:\backup-dj.fbk

	
gbak = chamando o binário do firebird responsável pelos backups e restores

-user SYSDBA = setar nome de usuário padrão pra entrar no banco, SYSDBA

-pas masterkey = setar senha padrão pra entrar no banco , masterkey

localhost:c:\djsystem\monitor\djpdv.fdb = endereço na rede e o caminho pra encontrar o banco de dados. ( localhost para quando o banco estiver localmente )

c:\backups\bkp-now.fbk = local onde será criado o arquivo .fbk com o backup do banco.



Fazer a restauração de um banco de dados via cmd:
--------------------------------------------------

	gbak –user SYSDBA –pas masterkey –r -v -o c:\backup.fbk 172.16.20.14:c:\dados.fdb

	gbak -user SYSDBA -pas masterkey -rep -v -o C:\Farsoft\Backup_Farsoft-3697.FBK C:\Farsoft\Database\branco.FDB;
	

gbak = chamando o binário do firebird responsável pelos backups e restores

-user SYSDBA = setar nome de usuário padrão pra entrar no banco, SYSDBA

-pas masterkey = setar senha padrão pra entrar no banco , masterkey

-r OU -rep

-v

-o

c:\backup.fbk = caminho onde está o arquivo com o backup do banco de dados. ( .fbk sempre )

192.168.10.101:c:\djsystem\monitor\dj.fdb = onde o banco de dados será restaurado. ( .fdb sempre )

	
