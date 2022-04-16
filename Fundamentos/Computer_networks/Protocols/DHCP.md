## DHCP


- É quando um cliente obtem IP,Maskara de rede,Gateway automaticamente, através de um requisição DHCP que é feita na rede. Normalmente essa requisição chega em algum roteador, que normalmente tem um servidor DHCP para fornecer esses dados para quem faz as requisições. Esses dados fornecidos pelo servidor DHCP         
(IP,Mascara,Gateway,DNS) voltam como resposta para a estação que fez a requisição. Quando a resposta chega na estação os dados são coletados por um programa conhecido como o cliente DHCP, é esse cliente DHCP que irá fazer a atribuição do IP,Mascara,Gateway,DNS da estação, conforme os dados da resposta do servidor DHCP.


---

## The DHCP Protocol


- Os endereços IP podem ser atribuídos manualmente, inserindo-os fisicamente em um dispositivo. E também de forma automática e nesse caso, é mais comum,
ser usado um servidor DHCP (Dynamic Host Configuration Protocol).

1. Quando um dispositivo se conecta a uma rede, se ainda não tiver sido atribuído manualmente um endereço IP,
ele envia uma solicitação (DHCP Discover) para ver se algum servidor DHCP está na rede.

2. O servidor DHCP então responde de volta com um endereço IP que o dispositivo pode usar (DHCP Offer).

3. O dispositivo então envia uma resposta confirmando que deseja o endereço IP oferecido (DHCP Request)

4. E por último o servidor DHCP envia uma resposta reconhecendo que isso foi concluído e o dispositivo pode começar a usar o endereço IP (DHCP ACK).

