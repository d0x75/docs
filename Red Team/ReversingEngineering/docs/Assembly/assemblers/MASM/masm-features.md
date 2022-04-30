Features of MASM
-----------------

### Notas


Usamos a notação <label> para nos referirmos às localizações marcadas no texto do programa. Os rótulos podem ser inseridos em qualquer lugar no texto do código assembly x86 inserindo um nome de rótulo seguido por dois pontos. Por exemplo,

		       mov esi, [ebp + 8]
		começar: xor ecx, ecx
		       mov eax, [esi]


### Keywords que vemos sendo usadas no assembler MASM:

---

**.386**

- Define o conjunto de instruções suportados pelo teu programa. O mínimo pra um EXE de 32-bits é a .386, mas o MASM tem suporte à vários outros conjuntos de instruções como: 

		.386, .486, .586, .686, .mmx, etc


**option casemap:none**

- Ativa o case sensitive, necessário para chamar as funções da API do Windows já que seus nomes são sensíveis ao caso.


**include**

- Inclui as os headers (como se fossem os .h do C) já prontos do MASM para usar as bibliotecas do Windows.


**inbludelib**

- Inclui o código compilado necessário para chamar tais bibliotecas da maneira que o MASM chama. É que quem desenvolve o MASM já escreveu e deixou tudo isso pronto para uso.


**.data**

- Cria uma nova seção de dados no arquivo. O db define um ou mais bytes. À esquerda dele é o nome (como se fosse o nome de uma variável) que você escolhe e à direita os dados em si, no caso, uma sequência de bytes representando uma string terminada em NULL (byte 0x00). Há também o dw (para dword), dd (para double word), etc.

Exemplos de declaração de variável :


``
.data			
var	DB 64  	; Declare um byte, conhecido como localização var , contendo o valor 64.
var2	DB?	; Declare um byte não inicializado, conhecido como localização var2 .
DB 10	; Declare um byte sem rótulo, contendo o valor 10. Sua localização é var2 + 1.
X	DW?	; Declarar um valor não inicializada dois bytes, designado como local X .
Y	DD 30000    	; Declare um valor de 4 bytes, referido como local Y , inicializado em 30000.
``




**.code**

- Inicia uma seção de código. O label .start marca o início dela (o MASM requer o end start no fim).


**invoke**

- Sendo parte da linguagem de alto nível do MASM, permite chamar as funções de acordo com a calling convention definida sem se preocupar em como os parâmetros serão passados, quem vai limpar a pilha, etc. Basicamente te permite programar em Assembly no estilo do C (o compilador trata das convenções). Os parâmetros são passados para a função depois do nome delas, separados por vírgula.


**.model flat, stdcall**

- 'Flat', diz respeito ao modelo de endereçamento de memória linear e vai fazer o compilador gerar EXE de 32-bits.

- 'stdcall', diz respeito à calling convention (como o Assembler vai gerar o código para chamadas de função, limpeza da pilha, passagem de argumentos, etc).


### Exemplo de um programa assembly pra compilar no MASM :

https://github.com/d0x75/win32-PoCs/blob/master/if-usando-masm_hight_lvl.asm