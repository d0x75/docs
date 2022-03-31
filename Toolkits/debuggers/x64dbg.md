x64dbg - Tricks
================


Recursos que mais uso :
-------------------------


**Procurar por uma string no executável**:

- Na tela principal do debugger fazer o seguinte:

		Botão direito > Pesquisar por > Todos os Módulos > Referência string

		Botão direito > Pesquisar por > Módulo Atual > Referência string

- Esperar carregar ( pode levar alguns minutos, caso fizermos a buscas em todos os módulos do processo )
- Pesquisar no campo de busca no rodapé da tela.


**Salvar path feito no binário**:

		CTRL + P ou botão direito > Patches


**Encontrar uma sequencia de código ou uma CodeCave como nos exemplos** :

		Exemplo 1 : CTRL + Shift + B

		Exemplo 2 : Botão direito > Pesquisar por > Módulo Atual > Padrão


---



Setups:
---------

**Setar o padrão de uppercase(LETRA MAIÚSCULA) para o disassemble. Com o x64dbg aberto, fazer o seguinte**:
	
	 Options > Preferences > Disasm > Marcar a box [ ]Uppercase > Save


**Habilitar o padrão de colocar o prefixo '0x', na frente dos números hexadecimais. Com o x64dbg aberto, fazer o seguinte**:

	 Options > Preferences > Disasm > Marcar a box [ ]0x prefix for values > Save


**Ter uma tabulação padrão para separar os mnemônicos dos argumentos. Com o x64dbg aberto, fazer o seguinte**:

	Options > Preferences > Disasm > Marcar a box [ ]Tab between mnemonic and arguments > Save

**Setar o debugger para cair sempre no Entry Point, quando começar a debuggar, fazer o seguinte**:

	Options > Preferences > Events > Desmarcar a box [] System Breakpoint*
	Options > Preferences > Events > Marcar a box [] Entry Breakpoint*


---



Plugins:
---------

### Sylla 

- Esse plugin já vem instalado por padrão, e serve para dumpar os dados em memória de um binário.

### multAsm

- Para realizar a instalação desse plugin, fazer o seguinte:

1. Fazer o download do plugin em : https://github.com/x64dbg/x64dbg/wiki/Plugins

2. Dentro do arquivo zipado escolhemos o plugin referente ao debugger que vamos utilizar( no caso o x64dbg x86 ), e colocamos ele no seguinte caminho:

	C:\Users\durev\Downloads\x64dbg\release\x32\plugins
	
3. Fechar o Debugger e abrir novamente.

- Depois de fazer a instalação, verificamos se o plugin está instalado clicando na aba 'Plugins' da parte superior da tela.

- Exemplo de uso ( Para assemblar mais de uma linha de uma vez )

1. Selecionar as linhas a serem assembladas.
2. Botão direito nas linhas selecionadas.
3. Multiline Ultimate Assembler ( última opção )
4. Disassemble Section
5. Escrever o código em Assembly > Assemble