## Load Balance(TL-ER5120) - TPLink


- Análise de um Load Balance destes desses, pegueis algumas informações básicas :

PS: Load Balance Gigabit Roteador de banda larga



Modelo : TL-ER5120

---


Versão de Firmware:	

	1.0.8 Build 20140212 Rel.36037 
Versão de Hardware:	

	TL-ER5120 v2.0


---


## Setups


Port Forwarding
-----------------

1. Acessar o equipamento
2. Clicar no botão 'Advanced' > 'NAT'
3. Entrar na aba 'Virtual Server'
4. Alimentar os dados para liberação da porta:
	
	Nome = Escolher algum nome.
	Interface = Qual internet(WAN) que deseja liberar a porta.
	External Port = A porta a ser liberada para acesso externo (Ex: 3306)
	Internal Port = Repetir a porta Externa.
	Protocolo = TCP/UDP
	Internal Server IP = IP local da máquina aonde a porta está liberada.

	Clicar no botão 'Add'




Mudar de internet
------------------

1. Acessar o equipamento
2. Clicar no botão 'Advanced' > 'Load Balance'
3. Entrar na aba 'Link Backup'
4. Clicar no botão 'Modify' (ícone de um lápis), feito isso a parte da tela 'General' ficará editavel.
5. Remover a 'Primary WAN' e  'Backup WAN' clicando no X.
6. Clicar no +B para selecionar WAN 1 como Backup, e clicando no +P será a WAN 2 como Principal.
7. Clicar no botão Save.
