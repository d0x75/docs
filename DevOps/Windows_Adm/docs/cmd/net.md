###net user

Comando utlizado para ter interaçoes com os usuários do sistema.

net user teste /add
	adicionando o usuário 'teste'


net localgroup administrators teste /add
	atribuindo permissão de adm para o usuário 'teste'

net user teste *
	atribuindo senha para o usuário 'teste'


net user teste *
	altera o password, quando o usuário que é passado como parâmetro ja tem um


net user teste /del
	deleta o usuário 'teste'




----


XMIND


Criando/Alterando credenciais de usuário via cmd
	net user
		listar os usuários
	net user teste /add
		adicionando o usuário 'teste'
	net localgroup administrators teste /add
		atribuindo permissão de adm para o usuário 'teste'
	net user teste *
		atribuindo senha para o usuário 'teste'
	net user teste *
		altera o password, quando o usuário que é passado como parâmetro ja tem um
	net user teste /del
		deleta o usuário 'teste'