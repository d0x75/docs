Passo a Passo da Instalação Completa do Iperius Backup
=======================================================

Ativação do Iperius
--------------------

1. Fazer a instalação do software : SetupIperius.exe > Abrir software após instalação.
2. No Iperius, clicar no botão Ativar Programa no canto esquerdo da tela.
3. Copiar o conteúdo do campo 'Computador Código', que vai aparecer no Iperius.
4. Abrir o crack : Iiperiusbackup_4_x_x.exe > Colar o código copiado do Iperius no campo Activation code here > OK.
5. Será gerado um código no campo abaixo, copiamos esse código para o campo 'Ativação de Código' no Iperius > Ativar.


Instalação do Iperius como Serviço
-----------------------------------

1. Clicar em 'Condição de Serviço : Não instalado' no rodapé da tela.
2. Na tela que abrir, clicamos em 'Instalar' > 'Cancelar' > 'Instalar' > 'Sim' > 'Ok'(status da condição de serviço mudou)


Importação do Job já pronto
-----------------------------

1. Fazer a importação da Job, clicando com o botão direito na tela principal do Iperius > Importar Tarefa de Backup > Selecionar o arquivo referente o Job (CLIENTE_MYSQL.ibj)
2. Então nosso job importado, irá aparecer como uma nova tarefa de Backup.


Configuração da Tarefa de Backup
---------------------------------

- Itens:

1. Setar no campo "Conta de Conexão MySQL" = ( Imagen Item-0).
2. Marcar a flag 'Backup dos seguintes bancos de dados:' > Selecionar o banco desejado. 
( Caso tenha mais de 1 banco de dados, colocar uma vírgula e escrever o nome dos demais).
3. Criar uma pasta com o nome BACKUP_MYSQL na raiz do C:\ 
4. No campo 'Executar o arquivo de backup na seguinte pasta' setar o caminho da pasta criada anteriormente.(C:\BACKUP_MYSQL)
5. No campo 'Incluir no backup os seguintes objetos', confirmar se a flag 'Usuários' está DESMARCADA.
6. Na aba 'Opções', verificar se a flag 'Proteger o arquivo zip com a senha:' está DESMARCADA.
7. OK ( Imagem Item-1 ) > Próximo.

- Destinos:

1. Clicar na Opção "Adicionar destino da Nuvem".
2. Clicar campo Account Cloud, para setarmos o seguinte:

	Nome = Farsoft ou Treinamento
	Tipo = Google Drive
	Client ID = Verificar no arquivo de Dados.
	Client Secret = Verificar no arquivo de Dados.
	OK

3. Informar e-mail e senha referente ao drive em que conectamos no passo anterior > Allow > Salvar > Fechar > OK > Próximo.


- Agendamento:


1. Todos os dias, de hora em hora. ( Imagem Agendamento-0) >  Próximo.


- Opções:


1. Manter as configurações padrão.


- Notificação por e-mail :

1. Campo destinatário e-mail = backup@farsoft.com.br
2. Clicar no botão "Adicionar / modificar conta", e informar os seguintes dados:

	Endereço de e-mail = backup@farsoft.com.br
	Servidor SMTP = smtp.zoho.com
	Porta = 465
	Marcar a flag 'O servidor de email de saída(SMTP) requer autenticação' > Preencher user and password do e-mail cadastrado > Ok > Enviar e-mail de teste > Salvar > Próximo.


- Outros Processos:

1. Colocar o arquivo LIMPAR.BAT na raiz do C: > Próximo.
 

- Resumo:

1. no Campo 'Nome da Tarefa', colocar o nome do CLIENTE referente ao backup > OK.


Configurações adicionais
------------------------

1. No Iperius, ir em Início > Configurações Gerais
2. Marcar a flag 'Proteger configuração de alterações não desejadas com a senha:' > Clicar em Definir Senha

	SENHA: nomecliente
	CONFIRMAR SENHA : nomecliente

