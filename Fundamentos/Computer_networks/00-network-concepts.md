## Conceitos importantes de Redes (networks)

[Switch](#Switches)

[Maskara de Rede](#Masks)

[Routers](#Routers)

[LoadBalance](#Loads)


---

### Subredes

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

### Switches


- Switches são dispositivos dedicados em uma rede projetados para agregar vários outros dispositivos, 
como computadores, impressoras ou qualquer outro dispositivo com capacidade de rede usando ethernet.


- Os switches são muito mais eficientes do que suas contrapartes menores (hubs / repetidores). 

- Os switches controlam qual dispositivo está conectado a qual porta. Dessa forma, ao receberem um pacote, 
em vez de repeti-lo para todas as portas como um hub faria, ele apenas o envia para o destino pretendido, reduzindo o tráfego na rede.

- Switches e roteadores podem ser conectados um ao outro. 
A capacidade de fazer isso aumenta a redundância (a confiabilidade) de uma rede, adicionando vários caminhos para os dados tomarem.

---

### Routers


 O que é um roteador?
- O trabalho de um roteador é conectar redes e passar dados entre elas.
- O roteamento é o rótulo dado ao processo de dados que trafegam pelas redes. 
O roteamento envolve a criação de um caminho entre as redes para que esses dados possam ser entregues com êxito.

---



---


