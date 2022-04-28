## Como funcionam as ferramentas de rede.

### Networking Tools Ping

- O comando ping é usado quando queremos testar se uma conexão com um recurso remoto é possível. 
- Normalmente, será um site na Internet, mas também pode ser para um computador em sua rede doméstica se você quiser verificar se está configurado corretamente.
- Ping funciona usando o protocolo ICMP, que é um dos protocolos TCP / IP um pouco menos conhecidos que foram mencionados anteriormente.
- O protocolo ICMP funciona na camada Network do Modelo OSI ou na camada de Internet do Modelo TCP/IP.
- Uma das grandes vantagens do ping é que ele é quase onipresente em qualquer dispositivo habilitado para rede.

---

### Networking Tools Traceroute

- O Traceroute pode ser usado para mapear o caminho que sua solicitação segue conforme segue para a máquina de destino.
- A Internet é composta de muitos, muitos servidores e terminais diferentes, todos interligados em rede. Isso significa que, para obter o conteúdo que você realmente deseja, primeiro você precisa passar por vários outros servidores
- O Traceroute permite que você veja cada uma dessas conexões - permite que você veja todas as etapas intermediárias entre o seu computador e o recurso que você solicitou.

---

### Networking Tools WHOIS

- O Whois essencialmente permite que você pergunte para quem um nome de domínio está registrado. 
- Na Europa, os dados pessoais são editados; entretanto, em outros lugares, você pode potencialmente obter uma grande quantidade de informações de uma pesquisa whois.

---

### Networking Tools Dig

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
no entanto, eles ainda podem ser acessados usando os mesmos 13 endereços IP atribuídos aos servidores originais 

---


### Identifying Devices on a Network


- Analogia á como identificar um individuo :

		IP Address = Nome do Individuo
		Mac Address = Impressões digitais do Individuo
		
O endereço MAC (Media Access Control) é um número hexadecimal de doze caracteres (um sistema de numeração de base dezesseis usado na computação para representar números) 
dividido em dois e separado por dois pontos. Esses dois pontos são considerados separadores. Por exemplo : a4:c3:f0:85:ac:2d

Os primeiros seis caracteres representam a empresa que fez a interface de rede e os últimos seis são um número exclusivo.

No entanto, uma coisa interessante com endereços MAC é que eles podem ser falsificados ou "falsificados" em um processo conhecido como Spoofing.
Esse spoofing ocorre quando um dispositivo em rede finge se identificar como outro usando seu endereço MAC. 

---


### TLD Servers ( Top-Level Domain ) 

os servidores de nomes raiz basicamente mantêm o controle dos servidores DNS no próximo nível abaixo, escolhendo um apropriado para redirecionar sua solicitação. 
Esses servidores de nível inferior são chamados de servidores de domínio de nível superior.

Os servidores de Domínio de Nível Superior (TLD) são divididos em extensões. 
Portanto, por exemplo, se você estiver procurando por facebook.com, sua solicitação será redirecionada para um servidor TLD que manipula domínios : **.com** 

E você estiver procurando por bbc.co.uk, sua solicitação será redirecionada para um servidor TLD que lida com domínios : **.co.uk**

---
