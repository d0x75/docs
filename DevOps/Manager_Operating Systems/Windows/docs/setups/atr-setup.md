Setup ATR ( Área de trabalho remota )
---------------------------------------



- Fazer a liberação para acesso remoto via TS no windows:

	Ir em painel de controle > Sistema
	Configuração remota
	Marcar a rádio : Permitir conexões de computadores que estejam executando a área de trabalho remota.


- Entrar no roteador: ( fazer o login , admin + password)

	Ir em configurações > Rede local > Redirecionamento de portas


- Agora terá os campos para preenchermos os dados do redirecionamento de portas:

		nome da regra : TS
		protocolo : TCP/UDP
		porta de origem : 3389
		porta destino : 3389
		IP de origem : 192.168.125.100 ( IP DO SERVIDOR )
		IP de destino : repetir o ip acima
		SALVAR


- Caso o roteador que configuramos o redirecionamento de portas acima, esteje fazendo ponte para outro roteador/equipamento, faremos os seguinte:
	
1. Acessar o roteador
2. Ir em configurações
3. Direcionar porta
4. Clicar no botão Adicionar


- Agora preencheremos os seguintes campos:

		Porta serviço : 3389
		Porta interna : 3389
		Endereço IP : 192.168.0.105 ( IP do servidor que vai receber acesso via TS )
		Protocolo : Todos ( UDP + TCP )
		Estado : Habilitado
		Porta serviço Comum : Podemos setar se a porta a ser utilizada estiver dentre essas portas de serviços padrões.
		SALVAR
