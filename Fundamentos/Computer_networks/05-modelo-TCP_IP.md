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