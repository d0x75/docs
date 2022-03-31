Windows Registry
----------------


O Registro do Windows é um banco de dados hierárquico que armazenas configurações de baixo nível para o sistema operacional Microsoft Windows


------



CHAVES DO REGISTRO DO WINDOWS "HKEYS"
--------------------------------------


### HKEY_CLASSES_ROOT

- Uma chave mantida por compatibilidade com versões do windows anteriores a mesma foi substituída pela chave que se encontra em : 

		HKEY_LOCAL_MACHINE > SOFTWARE > Classes


### HKEY_CURRENT_USER

- Chave referente ao usuário que está logado no momento no sistema. Alterações feitas aqui terão efeitos apenas no usuaário que está logado.


### HKEY_LOCAL_MACHINE

- Aqui temos opções que são utilizadas por todos os usuários do computador então qualquer alteração feitas aqui terão efeito em todo o computador EM GERAL.
- Temos também as subchaves : SAM,SOFTWARE,SYSTEM,SECURITY,HARDWARE.


### HKEY_USERS

- Uma chave que armazena a listagem de todos usuários do sistema. Por exemplo, quando fazemos o logoff é essa chave que traz as informações de todos usuário a fazer login


### HKEY_CURRENT_CONFIG

- Atalho para HK_LOCAL_MACHINE e também é mantida para compatibilidades com versões anteriores do windows.







