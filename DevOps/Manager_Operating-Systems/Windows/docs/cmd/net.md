### net user

**Comando utlizado para ter interaçoes com os usuários do sistema**.


- adicionando o usuário 'teste'

		net user teste /add

- atribuindo permissão de adm para o usuário 'teste'

		net localgroup administrators teste /add

- atribuindo senha para o usuário 'teste'

		net user teste *

- altera o password, quando o usuário que é passado como parâmetro ja tem um

		net user teste *

- deleta o usuário 'teste'

		net user teste /del


----