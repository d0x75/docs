Modelo OSI (Open Systems Interconnection)
------------------------------------------

**É o modelo tradicional utilizado para separar etapas do processo de comunicação entre redes**.

> Na prática, realmente o modelo TCP / IP mais compacto no qual a rede do mundo real se baseia; entretanto, o modelo OSI, de muitas maneiras, é mais fácil de se obter uma compreensão inicial.

> O Modelo OSI é formado por 7 camadas que são responsáveis pelas informações que são
trasnmitidas , e que vão da camada mais alta ( camada de aplicação ) até a camada mais 
baixa( camada física ).


---

## Encapsulation


>Conforme os dados são transmitidos para cada camada do modelo, mais informações contendo detalhes específicos para a camada em questão são adicionadas ao início da transmissão. Como exemplo, o cabeçalho adicionado pela Camada de Rede incluiria coisas como os endereços IP de origem e destino, e o cabeçalho adicionado pela Camada de Transporte incluiria (entre outras coisas) informações específicas do protocolo sendo usado. A camada de enlace de dados também adiciona uma peça no final da transmissão, que é usada para verificar se os dados não foram corrompidos na transmissão; isso também tem o bônus adicional de maior segurança, já que os dados não podem ser interceptados e adulterados sem quebrar o trailer. 
Todo esse processo é conhecido como encapsulamento; o processo pelo qual os dados podem ser enviados de um computador para outro. 

> Observe que os dados encapsulados recebem um nome diferente em diferentes etapas do processo. Nas camadas 7,6 e 5, os dados são simplesmente referidos como dados. Na camada de transporte, os dados encapsulados são chamados de segmento ou datagrama (dependendo se TCP ou UDP foi selecionado como protocolo de transmissão). Na camada de rede, os dados são chamados de pacote. Quando o pacote é passado para a camada de enlace de dados, ele se torna um quadro e, no momento em que é transmitido pela rede, o quadro já foi dividido em bits.
Quando a mensagem é recebida pelo segundo computador, ele inverte o processo - começando na camada física e avançando até atingir a camada de aplicativo, removendo as informações adicionadas à medida que avançam. Isso é conhecido como desencapsulamento. Assim, você pode pensar nas camadas do modelo OSI como existindo dentro de cada computador com recursos de rede. Embora não seja tão claro na prática, todos os computadores seguem o mesmo processo de encapsulamento para enviar dados e de-encapsulamento ao recebê-los.
Os processos de encapsulamento e desencapsulamento são muito importantes - não apenas por causa de seu uso prático, mas também porque nos fornecem um método padronizado de envio de dados. Isso significa que todas as transmissões seguirão consistentemente a mesma metodologia, permitindo que qualquer dispositivo habilitado para rede envie uma solicitação a qualquer outro dispositivo alcançável e tenha certeza de que será compreendido - independentemente de serem do mesmo fabricante; usar o mesmo sistema operacional; ou quaisquer outros fatores.


---



### As 7 Camadas do Modelo OSI

7. Application - Camada de aplicação : 

> Fornece opções de redes para aplicativos executados no computador, fornecendo uma interface para os mesmos transmitirem dados. Após serem fornecidos à camada de aplicativo, eles vão para a camada de apresentação.

		Ex: gerenciamento de redes, webservers ( ex: SMPT,email,DNS..)

6. Presentation - Camada de apresentação : 

> - Recebe dados da camada de aplicação. Esses dados devem estar em um formato no qual o aplicativo entende, mais não é um formato padronizado que possa ser compreendido pela camada de aplicação do computador receptor.

>-  A camada de Apresentação traduz os dados em um formato padronizado, além de lidar com criptografias, compreesão de dados e outras transformações nos dados.Feito isso, os dados são passados para a camada de sessão.

5. Session - Camada de sessão : 

> - Quando a camada de sessão recebe os dados formatados corretamente da camada de apresentação, ela verifica se consegue estabelecer a conexão com outro computador na rede. Senão puder vai retornar um erro e o processo não continua. Se uma sessão puder ser estabelecida ; é tarefa da camada de Sessão mantê-la e também cooperar para que com a camada de sessão do computador remoto para sincronizar as comunicações.

> - A camada de Sessão é particularmente importente pois a sessão que era cria é exclusiva para a comunicação em si. Isso é o que permite que você faça várias solicitações em diferentes endpoints simultaneamente, sem que os dados sem misturem.

> - Então quando a camada de sessão registra com sucesso uma conexão entre o host e o computador remoto, os dados são passados para a camada de transporte.

4. Transport - Camada de Transporte  : 

> - Essa camada desempenha inúmeras funções importantes.
O seu 1° Objetivo é escolher o protocolo pelo qual os dados serão transmitidos. Os dois protocolos mais comuns na camada de transporte são :

		TCP (Transmission Control Protocol)
		UDP (User Datagram Protocol);


> - No TCP a transmissão é baseada em conexão, o que significa que uma conexão entre os computadores é estabelecida
e mantida durante a solicitação.Isso permite uma transmissão confiável, pois a conexão pode ser usada para garantir que todos os pacotes cheguem ao lugar certo. 

> - Uma conexão TCP permite que os 2 computadores permaneçam em comunicação constante para garantir que os dados sejam enviados a uma velocidade aceitável e que todos os dados perdidos sejam reenviados.
Conexoes UDP...


3. Network - Camada de Rede : 

> Desenvolvimento de roteadores , endereçamento de dispositivos IPV4 e IPV6

2. Data Link - Camada de Enlace : 

> Equipamentos, ponto de acesso, ( MODEM, SWITCH  etc ..)

1. Physical - Camada Física : 

> É onde de fato está a Placa de rede. A camada que leva a mensagem ao receptor.


---

#### Modelo OSI continuação ( outra fonte ) :


### Layer 3 - Network :



- A camada de rede é responsável por localizar o destino de sua solicitação.
- Neste estágio, estamos trabalhando com o que é conhecido como endereçamento lógico (ou seja, endereços IP), que ainda são controlados por software. 
Os endereços lógicos são usados para fornecer ordem às redes e separar-las por categoria e classificar-las
- A forma mais comum de endereçamento lógico é o formato IPV4. ( EX : 192.168.1.1 é um endereço comum para um router doméstico )



### Layer 2 - Data Link (link de dados) :


- A camada de enlace de dados se concentra no endereçamento físico da transmissão.
- Ele recebe um pacote da camada de rede (que inclui o endereço IP do computador solicitante) e adiciona o endereço físico (MAC) do ponto de extremidade de recebimento. 
- Dentro de cada computador habilitado para rede está uma placa de interface de rede (NIC) que vem com um endereço MAC (Controle de acesso à mídia) exclusivo para identificá-la.
- Os endereços MAC são definidos pelo fabricante e literalmente gravados na placa; eles não podem ser alterados - embora possam ser falsificados. Quando as informações são 
enviadas através de uma rede, é na verdade o endereço físico que é usado para identificar para onde exatamente enviar as informações.
Essa camada também desempenha uma função importante ao receber dados, pois verifica as informações recebidas para garantir que não tenham sido corrompidas durante a transmissão, o que pode acontecer quando os dados são transmitidos pela camada 1




### Layer 1 - Physical


- A camada física vai até o hardware do computador. É aqui que os pulsos elétricos que constituem a transferência de dados em uma rede são enviados e recebidos.
- É função da camada física converter os dados binários da transmissão em sinais e transmiti-los pela rede, bem como receber sinais de entrada e convertê-los de volta em dados binários.



---