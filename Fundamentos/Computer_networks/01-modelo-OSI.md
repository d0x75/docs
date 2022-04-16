Modelo OSI (Open Systems Interconnection)
------------------------------------------

É o modelo tradicional utilizado para separar etapas do processo de comunicação entre redes.

Na prática, realmente o modelo TCP / IP mais compacto no qual a rede do mundo real se baseia; entretanto, o modelo OSI, de muitas maneiras, é mais fácil de se obter uma compreensão inicial.

O Modelo OSI é formado por 7 camadas que são responsáveis pelas informações que são
trasnmitidas , e que vão da camada mais alta ( camada de aplicação ) até a camada mais 
baixa( camada física ).


---


### As 7 Camadas do Modelo OSI

7. Application - Camada de aplicação : 
Fornece opções de redes para aplicativos executados no computador, fornecendo uma interface para os mesmos
transmitirem dados. Após serem fornecidos à camada de aplicativo, eles vão para a camada de apresentação.

		Ex: gerenciamento de redes, webservers ( ex: SMPT,email,DNS..)

6. Presentation - Camada de apresentação : 
Recebe dados da camada de aplicação. Esses dados devem estar em um formato no qual o aplicativo entende, mais
não é um formato padronizado que possa ser compreendido pela camada de aplicação do computador receptor.

A camada de Apresentação traduz os dados em um formato padronizado, além de lidar com criptografias,
compreesão de dados e outras transformações nos dados.Feito isso, os dados são passados para a camada de sessão.

5. Session - Camada de sessão : 
Quando a camada de sessão recebe os dados formatados corretamente da camada de apresentação, ela verifica se consegue estabelecer a conexão com outro computador na rede. Senão puder vai retornar um erro e o processo não
continua. Se uma sessão puder ser estabelecida ; é tarefa da camada de Sessão mantê-la e também cooperar para que com a camada de sessão do computador remoto para sincronizar as comunicações.

A camada de Sessão é particularmente importente pois a sessão que era cria é exclusiva para a comunicação em si.
Isso é o que permite que você faça várias solicitações em diferentes endpoints simultaneamente, sem que os
dados sem misturem.

Então quando a camada de sessão registra com sucesso uma conexão entre o host e o computador remoto, os dados são passados para a camada de transporte.

4. Transport - Camada de Transporte  : 
Essa camada desempenha inúmeras funções importantes.
O seu 1° Objetivo é escolher o protocolo pelo qual os dados serão transmitidos. Os dois protocolos mais comuns
na camada de transporte são :

		TCP (Transmission Control Protocol)
		UDP (User Datagram Protocol);


No TCP a transmissão é baseada em conexão, o que significa que uma conexão entre os computadores é estabelecida
e mantida durante a solicitação.Isso permite uma transmissão confiável, pois a conexão pode ser usada para
garantir que todos os pacotes cheguem ao lugar certo. 

Uma conexão TCP permite que os 2 computadores permaneçam em comunicação constante para garantir que os dados sejam enviados a uma velocidade aceitável e que todos os dados perdidos sejam reenviados.

Com a conexão UDP ....


3. Network - Camada de Rede : 
Desenvolvimento de roteadores , endereçamento de dispositivos IPV4 e IPV6

2. Data Link - Camada de Enlace : 
Equipamentos, ponto de acesso, ( MODEM, SWITCH  etc ..)

1. Physical - Camada Física : É onde de fato está a Placa de rede. A camada que leva a mensagem ao receptor.





