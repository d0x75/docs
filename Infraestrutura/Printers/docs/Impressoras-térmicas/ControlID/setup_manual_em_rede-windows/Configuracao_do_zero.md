## Setup das Impressoras térmicas da Control ID do ZERO. ( PrintID e PrintID Touth )

1. Plugar os cabos da impressora e ligar-la. ( Energia + Rede ou USB )

2. A impressora vai entrar na rede com o IP FIXO : 192.168.0.128

	OBS: Caso já tenha algum dispositivo com o IP FIXO da impressora na rede, teremos que identifica-lo e mudar o ip do mesmo
	( Advanced IP Scanner para localizar os IPs da rede )

3. Caso as máquina que vão comunicar com a impressora, estejam numa rede de faixa 0 já estaram comunicando com a
impressora normalmente.

4. Se a faixa de IP da rede local for diferente de 0. , vamos ter que mudar o IP da impressora pela sua Interface Touth ou 
vamos ter que fixar um IP também da faixa 0, como um IP secundário da máquina para caso não tenha o Touth.
Para fazer isso, seguimos os seguintes passos: ( isso apenas para PrintID )

			Verificar o IP da máquina local ( Comando 'ipconfig' via CMD ) .
			Ir em Painel de Controle > Central de Rede e Compartilhamento > Alterar Configurações do Adaptador.
			Clicar com o botão direito na rede Ethernet > Propriedes > TCP IPv4 > Propriedades.
			Fixar o IP da máquina local, que verificamos anteriormente via CMD > Avançado  ( Imagem 0)
			Adicionar > Setar um Endereço de IP válido para a faixa 0 > Adicionar > OK. ( Imagem 1)
			Testar comunicação com a impressora, via CMD : 


5. Testar comunicação com a impressora no IP que atribuimos a ela, ou com IP padrão caso não tenhamos que mudar-lo.

			ping 192.168.0.128


6. Instalação do Driver da impressora:
PrintID : https://www.controlid.com.br/automacao-comercial/printid/#download
PrintID Touth : https://www.controlid.com.br/automacao-comercial/printid-touch/#download


7. Fazer a Instalação da Impressora, seguindo os seguintes passos: ( Imagem 2,3)

			Ir em Dispositivos e Impressoras ou Impressoras e Scanners(win10)
			clicar em 'Adicionar Impressoras'
			clicar na opção 'A impressora que eu quero não esta na lista'
			marcar a flag 'Adicionar uma impressora usando um endereço TCP/IP ou nome de host' > Avançar
			Tipo de Despositivo = Dispositivo TCP/IP.
			Nome do host ou Endereço IP = IP SETADO PARA A PRINT ID, NO PASSO ANTERIOR.

OBS : Caso dê algum problema, tentar instalar a impressora manualmente com o arquivo .inf que vai ter dentro do arquivo zipado do driver da impressora.


----