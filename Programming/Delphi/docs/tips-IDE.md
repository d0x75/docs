### Dicas de Delphi:

- Para visualizar os Forms do projeto no Delphi	:
		
		Ir até um ícone com "2 quadradinhos", que chama 'View Form' ou SHIFT + F12
		Clicar nesse ícone e escolher o forme que quiser abrir.


TEdit - componente que é um campo recebe texto

TComboBox - componente que cria uma lista de opções pra serem selecionadas por uma seta.

TButton - os botões

TMemo - componento que é um campo que recebe mais de uma linha de texto.





### Códigos em Delphi


Máscara para valores númericos no grid = ###,###,##0.00



---



alt + F11 = lista todas as Units do Projeto. E selecionar a unit que precisamos incluir no nosso projeto.

vai gerar um trecho de código abaixo de 'implementation':

	implementation
	uses telaPrincipal;


- DIca : sempre comentar as variáveis.

- dICA : quando uma Unit X for refereciar a Unit Y, e também a Unit Y refereciar a Unit X .. faça essa referencia em 'implementation'.





---


O Delphi é um ambiente de desenvolvimento de softwares com as seguintes particularidades:

Visual: A definição da interface e até mesmo de parte da estrutura de um aplicativo Delphi pode ser realizada com o auxílio de ferramentas visuais.
Orientada a Objeto: Os conceitos de classe, herança e polimorfismo são abarcados pela linguagem de programação do Delphi, o Object Pascal. Esta não é, no entanto, uma linguagem puramente orientada a objeto como Smalltalk e Eiffel;
Orientada a Eventos: Cada elemento de uma interface de aplicativo é capaz de capturar e associar ações a uma série de eventos;
Compilada: A geração de código em linguagem de máquina acelera a execução dos aplicativos.


---


Se você é iniciante, ou mesmo se você já é um programador com anos de experiência, valem as seguintes dicas de programação:

Planeje antecipadamente seus programas. Pense sobre o que é necessário fazer e quais as ferramentas necessárias. Planejar é essencial para a programação.
Pense como o usuário. Lembre-se que o usuário não é um especialista em informática. Logo, você deve ser mais esperto do que ele.
Pense nos componentes. É comum que programadores inexperientes tentem desenvolver tudo com as próprias mãos, por falta de hábito ou somente “para provar que é possível”. Trata-se de uma perda de tempo, pois podem existir componentes de software prontos que podem fazer o que você precisa.
Aprenda fazendo. Programar é como nadar (e, freqüentemente, mais divertido e seguro). Pode-se assistir várias aulas sobre natação e ler vários livros, mas o fato é que só se aprende fazendo. Bons programadores não são necessariamente gênios, mas sim pessoas com grande experiência que começaram antes de você.


---




### Abrir outra TELA ( Unit ) no Delphi: 


Se você quiser abrir um outro form, primeiramente você deve usá-lo no form em que será chamado.
Nas Uses do Delphi, , informe o nome da unit do outro form. Você pode ir no Menu File, Use Unit, e selecionar a unit do form.
Depois, no evento do botão, informe: Form2.Show ou Form2. ShowModal.
