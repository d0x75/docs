*assembly x86 for reverse engineering*

### assembly

O assembly pode ser referenciado como uma _Class of Languages_, pois não é apenas uma linguagem padrão; mas sim uma série de linguagens diferentes com o mesmo intuito. Cada processador de computador possui sua própria linguagem assembly, que normalmente não são idênticas.  

Isso acontece devido o processador ter sido programado em sua própria fábrica para entender determinados bytes como código e executar operações.

### machine code ( código de máquina )

Ás vezes se ouve dizer que o código de máquina é “mais rápido” e “de nível inferior”. Isso é um equívoco; pois o código de máquina e linguagem assembly são duas reações diferentes da mesma coisa. Uma CPU lê os códigos de máquina, que no caso são sequências de bits, que contêm uma lista de instruções para a CPU executar. 

A linguagem assembly é simplesmente uma representação textual dessa sequencia de bits. Nomeamos elementos nessas sequências de código para torná-los legíveis por humanos. Em vez de números binários ou hexadecimais enigmáticos, podemos ver o nome da instrução textual. Exemplo : 

		ADD , MOV, SUB


### opcodes x mnemonics

Neste sentido um microprocessador, ou simplesmente processador é muito mais poderoso. Ao invés de o usuário gravar um programa
nele, o próprio fabricante já o faz, de modo que este microprograma entenda diferentes instruções para realizar diferentes
operações que chegam a ser complexas.. A entrada de dados do processador também é muito mais flexível: ao invés de entradas
binárias, um processador pode receber números bem maiores. O antigo Intel 8088 já possuía um barramento de 8 *bits*, por exemplo.

Isso significa que se um processador receber em seu barramento um conjunto de *bytes* específico, sabe que vai precisar executar
uma operação específica. À estes *bytes* possíveis damos o nome de ***opcodes***. Ao conjunto dos *opcodes* + operandos damos o
nome de **instrução**.

Temos que concordar que criar um programa assim não é nada fácil. Para resolver este problema foi criada uma **linguagem de
programação**, completamente presa à arquitetura do processador (seus *opcodes*, suas instruções), chamada **Assembly**. Com ela,
os programadores poderiam escrever o programa acima praticamente em inglês:

``
MOV EAX, 20
OR EAX, 18
``

De posse de um compilador de Assembly, chamado na época de **assembler**, o resultado da compilação do código-fonte acima é
justamente um arquivo (objeto) que contém os *opcodes* e argumentos corretos para o processador alvo, onde o programa vai rodar.

Quando os desenvolvedores escrevem código em linguagem assembly (uma ocorrência bastante rara nos dias de hoje), eles usam um programa chamado **assembler** para compilar o código escrito na linguagem assembly que é **textual** em código binário, que pode ser decodificado por uma CPU.

Na outra direção e mais relevante para a nossa narrativa de *reversing engineering*, um **disassembler** faz exatamente o oposto. Ele lê os códigos binários ( **opcodes** ) e gera o mapeamento textual para cada opcode nele. Essa é uma operação relativamente simples de executar porque o assembly é simplesmente uma representação textual dos opcodes do binário. Disassemblers são ferramentas fundamentais essenciais para a área.

Esse mapeamento textual que o disassembler gera, é conhecido como **mnemônicos.** Em suma cada opcode é referente a um mnemônico e há também **opcodes** que são referentes a valores imediatos que são usados em conjunto com os **opcodes** que representam os **mnemônicos** em si.

Pelo fato do processador só entender os **opcodes**, cada instrução em assembly que usamos tem seu respectivo opcode, ou seja, é o código que o processador sabe que é referente a instrução a ser executada. 

Exemplo:


		  Instrução | MOV EAX, 0x42
		  Opcodes   | B9 42 00 00 00

			Mnemônicos = MOV EAX, 0x42 / Opcodes = B9 42 00 00 00


**Conclusão sobre opcodes/mnemônicos** :

- Opcodes são códigos que o processador consegue ler e entender.
- Mnemônicos são a representação textual dos opcodes que a CPU lê.
- Cada opcode é referente a uma instrução assembly diferente das outras.



---