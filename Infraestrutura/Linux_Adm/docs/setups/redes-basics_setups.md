**NÃO VALIDADO**

## Mudar IP do no Kali linux :


- Adicionar um novo endereço IP no linux :

		ip a add 192.168.1.100 dev eth0

- Deletar um endereço ip no Linux :

		ip a delete 192.168.1.188 dev eth0

- Alterar o IP de uma interface de rede existente.

		vim /etc/network/interfaces

			\/

		auto lo
		iface lo inet loopback

		auto eth0
		iface eth0 inet static

		address 172.16.1.254
		gateway 172.16.1.1
		netmask 255.255.0.0
		network 172.16.0.0
		broatcast 172.16.255.255


Exemplo Prático de um Post :

- CONFIGURANDO PLACA DE REDE PARA IP FIXO NO DEBIAN

Vamos configurar a placa de rede no Debian para colocar IP fixo caso você use uma rede.
Primeiramente abra o terminal e entre como root (utilize o editor que preferir):

# nano /etc/network/interfaces
ou
# vim /etc/network/interfaces

Agora vamos configurar. Lembrando que eth0 é o dispositivo correspondente à minha placa:

auto eth0
   iface eth0 inet static
   address 192.168.1.20
   netmask 255.255.255.0
   gateway 192.168.1.1

Broadcast não é necessário, pois ele é configurado automaticamente.
Obs.: Está é a minha configuração, provavelmente você terá que adaptar para a sua rede.
Se você utiliza uma placa de rede para acesso externo, como eth0, basta modificar "eth0" para "eth1".

Agora vamos reiniciar a conexão de rede:

# /etc/init.d/networking restart

Pronto, configuração feita e é só aproveitar.



