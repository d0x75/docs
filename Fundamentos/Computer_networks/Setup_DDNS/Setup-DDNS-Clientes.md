Passo a Passo SETUP DDNS
=========================

- Configuração de DDNS para o IP EXTERNO nos servidores de banco de dados.

1. Entrar no site do NoIP : https://www.noip.com/
2. Fazer o login, com as credenciais do NoIP.
3. Para criar um novo Host, seguimos os seguintes passos: ( Imagem noIp-0.png )

	Clicar em DNS Dinâmico
	Create hostname
	Informar nome do host
	Clicar no botão 'Create Hostname'

4. Fazer o download do software DucNoIP : 	https://www.noip.com/client/DUCSetup_v4_1_1.exe

5. Após o download, fazer a instalação de forma convencional.

6. Após instalação, fazer o login com o hostname criado anteriormente.

7. Agora faremos o seguinte Setup para escolher o Host:

		Clicar em Edit Hosts.
		Marcar o Host desejado.
		Marcar a flag 'Require a password to modify hosts'
		Clicar no botão 'Save'
		Setar a senha padrão, para acessar o DucNoIp na máquina = xxxx

8. Em seguida faremos um setup para inicialização automática do DucNoIP: ( Imagem noIp-1.png )

		Ir na aba 'File' > 'Preferences'
		Marcar as 2 primeiras flags

	
9. Liberar a porta 3306/3307 no Firewall do Windows. ( Caso tenha um anti-vírus com Firewall, fazer a liberação nele também)

10. Acessar o roteador e fazer os Setups Finais:

		Acessar o equipamento via navegador, pelo Gatway padrão.
		Informar as credenciais para acessar o equipamento.
		

11. Reservar um através do MAC ADDRESS do dispositivo Servidor. ( Imagem VIVO-0.png )

		Clicar em 'Configurações' > 'Rede Local'
		Na parte de Criar Reserva no DHCP, selecionamos o hostname referente ao dispositivo considerado servidor.
		Nessa mesma parte, na aba Endereço IP setamos o IP que ficará reservado para o dispositivo
		Clicar no botão 'Reservar'

12. Liberação das portas padrão, para permitir o acesso externo no servidor: ( Imagem VIVO-1.png )

		Ainda na tela na rede local, clicamos na aba "Redirecionar Portas" e preenchemos as informações.
		Clicar em Adicionar

Observação: No campo IP Interno, colocamos o IP local da máquina do dispositivo considerado o 'Servidor'.