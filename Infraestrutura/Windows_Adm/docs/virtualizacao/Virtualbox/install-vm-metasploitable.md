## Setup Metasploitable at VirtualBox :

- Download a vm Metasploitable ( Que é uma VM totalmente vulneravél para fazermos alguns testes )

		https://sourceforge.net/projects/metasploitable/?source=typ_redirect

- Importar nossa máquina Metasploitable para o virtual box, fazendo o seguinte :

1. Abir Virutal box > Criar nova máquina ( Novo )
2. O metasploitable é baseado em Debian
3. Colocar o tamanho da memória  como 512Mb. Pois não usaremos ambiente gráfico
4. Não acrescentar um disco rígido virtual
5. Depois da máquina criada, clicamos na mesma e depois no botao Configurações.
6. Ir na aba Rede e fazer o seguinte procedimento
7. Manter como NAT
8. Ir na aba Armazenamento e fazer o seguinte procedimento ( Criar nosso HD )
9. Clicar no controlador SATA
10. Em seguida clicar no  ícone HD+ > Utilizar um disco rígido existente ) > Selecionar o .vmdk que baixamos do Metasploitable ( É o arquivo com ícone dentro do zip que baixamos ) > Depois disso basta iniciarmos a máquina . ( Login e Password padrões : msfadmin ).