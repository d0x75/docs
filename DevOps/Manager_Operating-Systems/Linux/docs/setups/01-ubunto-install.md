## INSTALAÇÃO UBUNTO


1. Bem vindo - Na primeira etapa escolhemos o nosso idioma e clicamos em INSTALAR O UBUNTO ( também podemos clicar em EXPERIMENTAR UBUNTO, para termos uma prévia do SO)

2. Preparando pra instalar o ubunto - Deixar desmarcado as box 'Baixar atualizações enquanto instala o ubunto' e a box que instala softwares de terceiros'CODECS'. ( Também podemos marcar essas boxs, para que não precise atualizar o SO depois de instalado, mais não é muito recomendado pois requer uma internet rázoavel).

3. Tipo de instalação - Nessa etapa podemos particionar nosso HD, para casos de DUALBOOT temos que marcar a RADIO 'Instalar ubunto ao lado do Windows' para ter opções de dualboot. Quando quisermos nos livrar do windows que estava anteriormente instalado e manter apenas o Ubunto, marcamos a RADIO 'Substituir o windows 7 pelo Ubunto'. E por fim temos a 'Opção avançada' que será a utilizada, onde temos informações dos particionamentos do disco rígido e podemos configurar de forma customizadas.

Agora para instalar o Ubunto em uma partição, vamos no 'espaço livre' a ser armazenado e clicamos no sinal de +.

Feito isso irá abrir uma nova telinha com o nome de 'CRIAR PARTIÇÃO', então iremos configurar da seguinte forma:

	Tamanho: Colocamos o tamanho que vai conter a partição de nosso SO ( já vem preenchida por padrão com o tamanho total disponível)
	Tipo para a nova partição: Lógica
	Localização para a nova partição: 
	Usar como: Escolher o sistema de arquivos que iremos utilizar, para o Ubunto client o mais recomendado e o que será utilizado é '"journaling"ext4'
	Ponto de montagem: / ( para instalações padrão) . Também podemos instalar o sistema com a pasta /home SEPARADA.
	Ok
	Se não estiver tudo correto, clicar no botão do rodapé, INSTALAR AGORA.

4. Onde você está? - Escolher localização, onde moramos. (Ex: São paulo ) > Continuar
5. Layout do teclado - O Ubunto detecta automaticamente o layout do teclado, mais também podemos alterar. ( Portugues - brazil)
6. Quem é você? Preencher o nossos dados pessoais, como: nome completo,nome do computador,nome do usuário,senha para o Ubunto.
7. Aguardar a instalação.
8. Depois de inicializar, abrir o terminal e fazer as atualizações via APT-GET e a instalação dos CODECS.
	apt update && apt-upgrade

Post com as configurações necessárias para o Ubunto após a instalação:

https://www.diolinux.com.br/2014/04/deixe-o-ubuntu-1404-lts-perfeito-para-uso.html
