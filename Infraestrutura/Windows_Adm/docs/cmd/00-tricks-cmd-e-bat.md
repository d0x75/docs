Dicas de sobre o prompt do windows e batscript
-------------------------------------------------

### 0x00 - Criar atalho do cmd.exe com um macete bem legal.

Abrir as propriedades do atalho do cmd.exe que criamos.
Propriedades > Advanced > Run as administrador.
Ir em Propriedades >completar o campo "Target" com o seguinte:

``/k cd C:\Users\Usuario\Desktop``

No caso vai ficar assim : ``C:\Windows\System32\cmd.exe /k cd C:\Users\Usuario\Desktop``


---


### 0x01 - Lista de Variáveis Nativas do Windows

- Para cair direto na pasta do usuário do Windows, podemos acionar a variável do perfil do usuário do SO :

		%userprofile%

- Variável que tem como valor armazenado padrão, a data do dia atual.

		echo %date%

- Variável que tem como valor armazenado padrão, a hora atual.

		echo %time%

- Variável local do windows que cai na pasta Appdata.

		echo %appdata%s

- Variável local que armazena o retoro de erros dos programas executados no prompt.

		echo %errorlevel%
