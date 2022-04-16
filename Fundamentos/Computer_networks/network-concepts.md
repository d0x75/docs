# Indroduction Networking / Network Fundamentals

## Modelo OSI continuação :


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


##  Encapsulation


- Conforme os dados são transmitidos para cada camada do modelo, mais informações contendo detalhes específicos para a camada em questão são adicionadas ao início da transmissão. Como exemplo, o cabeçalho adicionado pela Camada de Rede incluiria coisas como os endereços IP de origem e destino, e o cabeçalho adicionado pela Camada de Transporte incluiria (entre outras coisas) informações específicas do protocolo sendo usado. A camada de enlace de dados também adiciona uma peça no final da transmissão, que é usada para verificar se os dados não foram corrompidos na transmissão; isso também tem o bônus adicional de maior segurança, já que os dados não podem ser interceptados e adulterados sem quebrar o trailer. 
Todo esse processo é conhecido como encapsulamento; o processo pelo qual os dados podem ser enviados de um computador para outro. 

Observe que os dados encapsulados recebem um nome diferente em diferentes etapas do processo. Nas camadas 7,6 e 5, os dados são simplesmente referidos como dados. Na camada de transporte, os dados encapsulados são chamados de segmento ou datagrama (dependendo se TCP ou UDP foi selecionado como protocolo de transmissão). Na camada de rede, os dados são chamados de pacote. Quando o pacote é passado para a camada de enlace de dados, ele se torna um quadro e, no momento em que é transmitido pela rede, o quadro já foi dividido em bits.
Quando a mensagem é recebida pelo segundo computador, ele inverte o processo - começando na camada física e avançando até atingir a camada de aplicativo, removendo as informações adicionadas à medida que avançam. Isso é conhecido como desencapsulamento. Assim, você pode pensar nas camadas do modelo OSI como existindo dentro de cada computador com recursos de rede. Embora não seja tão claro na prática, todos os computadores seguem o mesmo processo de encapsulamento para enviar dados e de-encapsulamento ao recebê-los.
Os processos de encapsulamento e desencapsulamento são muito importantes - não apenas por causa de seu uso prático, mas também porque nos fornecem um método padronizado de envio de dados. Isso significa que todas as transmissões seguirão consistentemente a mesma metodologia, permitindo que qualquer dispositivo habilitado para rede envie uma solicitação a qualquer outro dispositivo alcançável e tenha certeza de que será compreendido - independentemente de serem do mesmo fabricante; usar o mesmo sistema operacional; ou quaisquer outros fatores.



---


## TCP/IP Model


- O modelo TCP é bem semelhante ao OSI, porém um pouco mais velho. Possuem 4 camadas que são as seguintes : Aplicação, Transporte, Internet e Interface de Rede.

			TCP/IPI
				Application  ( engloba as camdas Application,Presentation e Session do Modelo OSI )
				Transport
				Internet     ( cobra a camada Network do Modelo OSI )
				Network Interface ( engloba as camdas DataLink e Physical do Modelo OSI )
				
				
- Os processos de encapsulamento e desencapsulamento funcionam exatamente da mesma maneira com o modelo TCP / IP e com o modelo OSI. 
Em cada camada do modelo TCP / IP, um cabeçalho é adicionado durante o encapsulamento e removido durante o desencapsulamento.


- Existem diversos protocolos embutidos no padrão TCP/IP ,e falaremos dos principais :

#### TCP ( Transmission Control Protocol - controla o fluxo de dados entre 2 extremidades como vimos anteriormente ) 


o TCP é um protocolo baseado em conexão. Em outras palavras, antes de enviar quaisquer dados via TCP, você deve primeiro formar uma conexão estável entre os dois computadores. 
_O processo de formação dessa conexão é chamado de handshake de três vias_.

- Quando você tenta fazer uma conexão, seu computador primeiro envia uma solicitação especial ao servidor remoto indicando que deseja inicializar uma conexão. 
Essa solicitação contém algo chamado de bit SYN (abreviação de sincronizar), que basicamente faz o primeiro contato ao iniciar o processo de conexão. 
O servidor então responderá com um pacote contendo o bit SYN, bem como outro bit de "reconhecimento", chamado ACK. 
Finalmente, seu computador enviará um pacote que contém o bit ACK sozinho, confirmando que a conexão foi configurada com sucesso. 
Com o handshake triplo concluído com êxito, os dados podem ser transmitidos de forma confiável entre os dois computadores.
Quaisquer dados perdidos ou corrompidos na transmissão são reenviados, levando a uma conexão que parece não ter perdas.


IP  ( Internet Protocol - controla como os pacotes serão endereçados e enviados )



---


## Networking Tools Ping


- O comando ping é usado quando queremos testar se uma conexão com um recurso remoto é possível. 
- Normalmente, será um site na Internet, mas também pode ser para um computador em sua rede doméstica se você quiser verificar se está configurado corretamente.
- Ping funciona usando o protocolo ICMP, que é um dos protocolos TCP / IP um pouco menos conhecidos que foram mencionados anteriormente.
- O protocolo ICMP funciona na camada Network do Modelo OSI ou na camada de Internet do Modelo TCP/IP.
- Uma das grandes vantagens do ping é que ele é quase onipresente em qualquer dispositivo habilitado para rede.



---



## Networking Tools Traceroute



- O Traceroute pode ser usado para mapear o caminho que sua solicitação segue conforme segue para a máquina de destino.
- A Internet é composta de muitos, muitos servidores e terminais diferentes, todos interligados em rede. Isso significa que, para obter o conteúdo que você realmente deseja, primeiro você precisa passar por vários outros servidores
- O Traceroute permite que você veja cada uma dessas conexões - permite que você veja todas as etapas intermediárias entre o seu computador e o recurso que você solicitou.



---


## Networking Tools WHOIS


- O Whois essencialmente permite que você pergunte para quem um nome de domínio está registrado. 
- Na Europa, os dados pessoais são editados; entretanto, em outros lugares, você pode potencialmente obter uma grande quantidade de informações de uma pesquisa whois.



---


## Networking Tools Dig


- Você já se perguntou como um URL é convertido em um endereço IP que seu computador pode entender? 
A resposta é um dos outros protocolos inclusos no TCP / IP chamado DNS (Domain Name System).

- No nível mais básico, o DNS nos permite solicitar a um servidor especial o endereço IP do site que estamos tentando acessar. 

Por exemplo, se fizéssemos uma solicitação para www.google.com, nosso computador primeiro enviaria uma solicitação para um 
servidor DNS especial (que seu computador já sabe como encontrar). O servidor irá procurar o endereço IP do Google e o enviará de volta para nós.

Vamos detalhar um pouco mais :

- Você faz uma solicitação a um site. A primeira coisa que seu computador faz é verificar seu cache local para ver se ele já tem um endereço IP armazenado para o site; se isso acontecer, ótimo. 
- Caso contrário, ele passa para a próxima etapa do processo.

- Supondo que o endereço ainda não tenha sido encontrado, seu computador enviará uma solicitação ao que é conhecido como servidor DNS recursivo.
- Eles serão automaticamente conhecidos pelo roteador em sua rede.

Muitos provedores de serviços de Internet (ISPs) mantêm seus próprios servidores recursivos, mas empresas como Google e OpenDNS também controlam servidores recursivos.
É assim que seu computador sabe automaticamente para onde enviar a solicitação de informações: os detalhes de um servidor DNS recursivo são armazenados em seu roteador.
Este servidor também manterá um cache de resultados para domínios populares; no entanto, se o site que você solicitou não estiver armazenado no cache, o servidor recursivo passará a solicitação para um servidor de nomes raiz.

Antes de 2004, havia exatamente 13 servidores DNS de nomes raiz no mundo. Hoje em dia existem muitos mais; 
no entanto, eles ainda podem ser acessados ​​usando os mesmos 13 endereços IP atribuídos aos servidores originais 



#### TLD Servers ( Top-Level Domain ) 

os servidores de nomes raiz basicamente mantêm o controle dos servidores DNS no próximo nível abaixo, escolhendo um apropriado para redirecionar sua solicitação. 
Esses servidores de nível inferior são chamados de servidores de domínio de nível superior.

Os servidores de Domínio de Nível Superior (TLD) são divididos em extensões. 
Portanto, por exemplo, se você estiver procurando por facebook.com, sua solicitação será redirecionada para um servidor TLD que manipula domínios : **.com** 

E você estiver procurando por bbc.co.uk, sua solicitação será redirecionada para um servidor TLD que lida com domínios : **.co.uk**






---



## Identifying Devices on a Network


- Analogia á como identificar um individuo :

		IP Address = Nome do Individuo
		Mac Address = Impressões digitais do Individuo
		
O endereço MAC (Media Access Control) é um número hexadecimal de doze caracteres (um sistema de numeração de base dezesseis usado na computação para representar números) 
dividido em dois e separado por dois pontos. Esses dois pontos são considerados separadores. Por exemplo : a4:c3:f0:85:ac:2d

Os primeiros seis caracteres representam a empresa que fez a interface de rede e os últimos seis são um número exclusivo.

No entanto, uma coisa interessante com endereços MAC é que eles podem ser falsificados ou "falsificados" em um processo conhecido como Spoofing.
Esse spoofing ocorre quando um dispositivo em rede finge se identificar como outro usando seu endereço MAC. 



---


## PING ( Icmp )


Ping usa pacotes ICMP (Internet Control Message Protocol) para determinar o desempenho de uma conexão entre 
dispositivos, por exemplo, se a conexão existe ou é confiável.

O tempo gasto para os pacotes ICMP viajarem entre os dispositivos é medido por ping, como na captura de tela abaixo. 
Essa medição é feita usando o pacote de eco do ICMP e, em seguida, a resposta de eco do ICMP do dispositivo de destino



---


## Local Area Network (LAN) Topologies


Ao longo dos anos, houve experimentação e implementação de vários projetos de rede. 
Em referência à rede, quando nos referimos ao termo "topologia", estamos na verdade nos referindo ao design ou aparência da rede em questão.
Vamos discutir as vantagens e desvantagens dessas topologias a seguir.


#### Star Topology ( topologia estrela )


- A premissa principal de uma topologia em estrela é que os dispositivos sejam conectados 
individualmente por meio de um dispositivo de rede central, como um switch ou hub.

- Essa topologia é a mais comumente encontrada hoje em dia devido 
à sua confiabilidade e escalabilidade - apesar do custo.

- Qualquer informação enviada a um dispositivo nessa topologia, é enviada por meio do dispositivo central.

EX :

 Farsoft.. UM Switch que distribuí a rede para os computadores. Trata-se de uma TOPOLOGIA ESTRELA neste caso.


#### Bus Topology ( topologia de barramento )



- Esse tipo de conexão depende de uma única conexão, conhecida como cabo de backbone.

- Esse tipo de topologia é semelhante à folha de uma árvore no sentido de que dispositivos (folhas) se originam de onde os galhos estão neste cabo.

- as topologias de barramento são uma das topologias mais fáceis e econômicas de configurar 
devido aos seus gastos, como cabeamento ou equipamento de rede dedicado usado para conectar esses dispositivos.


- Como todos os dados destinados a cada dispositivo trafegam pelo mesmo cabo, eles estão muito rapidamente propensos a se tornarem
 lentos e com gargalos se os dispositivos na topologia estiverem solicitando dados simultaneamente.

- Por último, outra desvantagem da topologia de barramento é que há pouca redundância no local em caso de falhas. ( deu problema no cabo backbone, para tudo!)


#### Ring Topology ( topologia de anel )


- Dispositivos como computadores são conectados diretamente uns aos outros para formar um loop, o que significa
que há pouco cabeamento necessário e menos dependência de hardware dedicado, como em uma topologia em estrela.


#### Switch


- Switches são dispositivos dedicados em uma rede projetados para agregar vários outros dispositivos, 
como computadores, impressoras ou qualquer outro dispositivo com capacidade de rede usando ethernet.


- Os switches são muito mais eficientes do que suas contrapartes menores (hubs / repetidores). 

- Os switches controlam qual dispositivo está conectado a qual porta. Dessa forma, ao receberem um pacote, 
em vez de repeti-lo para todas as portas como um hub faria, ele apenas o envia para o destino pretendido, reduzindo o tráfego na rede.

- Switches e roteadores podem ser conectados um ao outro. 
A capacidade de fazer isso aumenta a redundância (a confiabilidade) de uma rede, adicionando vários caminhos para os dados tomarem.




#### Routers


 O que é um roteador?
- O trabalho de um roteador é conectar redes e passar dados entre elas.
- O roteamento é o rótulo dado ao processo de dados que trafegam pelas redes. 
O roteamento envolve a criação de um caminho entre as redes para que esses dados possam ser entregues com êxito.

---


## Subredes

Network Adress = Este endereço identifica o início da rede real e é usado para identificar a existência de uma rede.
Por exemplo, um dispositivo com o endereço IP de 192.168.1.100 estará na rede identificada por 192.168.1.0

Host Address = Um endereço IP aqui é usado para identificar um dispositivo na sub-rede. 
Por exemplo, um dispositivo terá o endereço de rede de 192.168.1.1

Default Gatewayy = O endereço de gateway padrão é um endereço especial atribuído a um dispositivo na rede que é capaz de enviar informações para outra rede
( routers, swtich , load balance etc.. )


Todos os dados que precisam ir para um dispositivo que não está na mesma rede (ou seja, não está em 192.168.1.0) serão enviados para este dispositivo. 
Esses dispositivos podem usar qualquer endereço de host, mas geralmente usam o primeiro ou o último endereço de host em uma rede (.1 ou .254)

Agora, em redes pequenas, como a doméstica, você estará em uma sub-rede, pois é improvável que você precise de mais de 254 dispositivos conectados ao mesmo tempo.


---


##  The ARP Protocol 


- O Protocolo ARP ( Address Resolution Protocol  ) , é a tecnologia responsável por permitir que os dispositivos se identifiquem em uma rede.
- Simplesmente, o protocolo ARP permite que um dispositivo associe seu endereço MAC a um endereço IP na rede. 
- Cada dispositivo em uma rede manterá um registro dos endereços MAC associados a outros dispositivos.
- Quando os dispositivos desejam se comunicar com outro, eles enviam uma transmissão para toda a rede em busca do dispositivo específico.
- Os dispositivos podem usar o protocolo ARP para encontrar o endereço MAC (e, portanto, o identificador físico) de um dispositivo para comunicação.



---


## The DHCP Protocol


- Os endereços IP podem ser atribuídos manualmente, inserindo-os fisicamente em um dispositivo. E também de forma automática e nesse caso, é mais comum,
ser usado um servidor DHCP (Dynamic Host Configuration Protocol).

1. Quando um dispositivo se conecta a uma rede, se ainda não tiver sido atribuído manualmente um endereço IP,
ele envia uma solicitação (DHCP Discover) para ver se algum servidor DHCP está na rede.

2. O servidor DHCP então responde de volta com um endereço IP que o dispositivo pode usar (DHCP Offer).

3. O dispositivo então envia uma resposta confirmando que deseja o endereço IP oferecido (DHCP Request)

4. E por último o servidor DHCP envia uma resposta reconhecendo que isso foi concluído e o dispositivo pode começar a usar o endereço IP (DHCP ACK).







