### Comandos/Scripts para *reconhecimento* usando nmap



##### Varredura que mostra todas as portas abertas e versões dos serviços que eventualmente estão rodando nas respectivas portas :


```bash
nmap -sV -p- -Pn 10.10.1.10 -oN ./currentscan.log
```

##### Varredura em rede local que identifica o endereço IP e MAC Address dos dispositivos conectados na rede :


```bash
nmap -sn 10.10.1.1-254 -oN ./currentscan.log
```

##### Varredura para verificar versão do sistema operacional e dos serviços ativos :


```bash
nmap -O -v 10.10.1.10 -oN ./currentscan.log
```


