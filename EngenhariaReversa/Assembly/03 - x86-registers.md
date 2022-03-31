registradores x86-64 
---------------------

Um registrador é uma área física dos chips da CPU para armazenamento de dados, cujo conteúdo pode ser acessado mais rapidamente que qualquer
outro tipo de armazenamento.  São chamados de registradores porque sempre registram ( salvam ) números por tempo não determinado.

**GPRs - General Porpouse Registers** - registradores de uso geral

Ao operar em protect mode, a arquitetura x86 fornece 8 GPRs, que são eles : **EAX, EBX, ECX, EDX, EDI, ESI, EBP, and ESP**.

Apesar do nome ainda segue alguns padrões, por convenção os compiladores armazenam retornos de funções no registrador EAX. Também outra convenção adotada foi que os registradores ESP(stack pointer) e EBP(base pointer), controlam o fluxo da stack.

A CPU conta com diversos registradores além dos registradores de uso geral, e podemos dividi-los da seguinte forma :

- **registradores de uso geral** : são aqueles apresentados á cima, e são os mais usados.
- **registradores Segmentados**  : utilizados para mapear sessões da memória.
- **registradores de Flags**     : o conhecido EFLAGS, registrador de 32bits que representa todas as Flags que podem ser usadas.
- **registradores Instruction pointer** : registrador que aponta para a próxima instrução a ser executada. O registrador EIP no caso.
- **registradores Virtual Memory and Debugging** : registrador usado para controle de mecanismos importantes de baixo-nível.
- **registradores MSRs** : registradores que são específicos de determinado modelo de processador.

---

### registradores de uso geral (GPRs)

- Registradores responsáveis pela execução do programa , para armazenar valores de operações aritméticas, movimentar dados dentre outras coisas. Lembrando que o tamanho padrão de cada registrador x86 de uso geral é de 32 bits, mais em alguns casos podemos quebrar o tamanho desses registradores para 16 bits ou 8 bits, mais quando acontece isso temos a mudança no nome do registrador para ficar evidente. Exemplo :


		EAX = 32 bits (default)
		AX  = 16 bits
		AH  = 8  bits mais significativos  ( da esquerda p/ direita em little-endian )
		AL  = 8  bits menos significativos ( da direita p/ esquerda em little-endian )


> Quando entramos na seara da **x86-64** , o registrador pode chegar no tamanho de 64 bits e também veremos outro nome :

		RAX = 64 bits ( default )
		EAX = 32 bits
		...

- Esquema de todos os GPRs x86 que tem variações de tamanho, e que mudam de nome consequentemente.

		RAX = 64 bits ( 8 BYTES  - QWORD )
		EAX = 32 bits ( 4 BYTES  - DWORD )
		AX = 16 bits ( 2 BYTES  - WORD  )
		AH = 8  bits ( 1 BYTES  - BYTE  )
		AL = 8  bits ( 1 BYTES  - BYTE  )

		RBX = 64 bits ( 8 BYTES  - QWORD )
		EBX = 32 bits ( 4 BYTES  - DWORD )
		BX = 16 bits ( 2 BYTES  - WORD  )
		BH = 8  bits ( 1 BYTES  - BYTE  )
		BL = 8  bits ( 1 BYTES  - BYTE  )

		RCX = 64 bits ( 8 BYTES  - QWORD )
		ECX = 32 bits ( 4 BYTES  - DWORD )
		CX = 16 bits ( 2 BYTES  - WORD  )
		CH = 8  bits ( 1 BYTES  - BYTE  )
		CL = 8  bits ( 1 BYTES  - BYTE  )

		RDX = 64 bits ( 8 BYTES  - QWORD )
		EDX = 32 bits ( 4 BYTES  - DWORD )
		DX = 16 bits ( 2 BYTES  - WORD  )
		DH = 8  bits ( 1 BYTES  - BYTE  )
		DL = 8  bits ( 1 BYTES  - BYTE  )

		RBP = 64 bits ( 8 BYTES - QWORD  )
		EBP = 32 bits ( 4 BYTES - DWORD  )
		BP = 16 bits ( 2 BYTES - WORD   )

		RSP = 64 bits ( 8 BYTES - QWORD  )
		ESP = 32 bits ( 4 BYTES - DWORD  )
		SP = 16 bits ( 2 BYTES - WORD   )

		RSI = 64 bits ( 8 BYTES - QWORD  )
		ESI = 32 bits ( 4 BYTES - DWORD  )
		SI = 16 bits ( 2 BYTES - WORD   )

		RDI = 64 bits ( 8 BYTES - QWORD  )
		EDI = 32 bits ( 4 BYTES - DWORD  )
		DI = 16 bits ( 2 BYTES - WORD   )


### registradores Segmentados

Nesses registradores são armazenados o que conhecemos como seletores, que são *ponteiros* que identificam segmentos na memória que são essenciais para operar em real-mode. Quando operamos em protect-mode que é o modo em que os sistemas operacionais utilizam, a função de cada registrador de segmento fica por conta do sistema operacional definir.  

Lista de registradores de segmento, e sua respectiva função em protect-mode no x86.

- **CS - Code Segment**

O conceito de privilégios no x86 por Ring Levels é codificado no registrador CS e as vezes referido como o nível de privilégio atual ( CPL ) na documentação.

- **SS - Stack Segment**

- **DS - Data Segment**

- **ES - Extra Data Segment**

- **SS - Stack Segment**

- **DS - Data Segment**

- **ES - Extra Data Segment**

- **FS - Data Segment**

No Windows x86, aponta para o TEB ( Thread Environment Block ) da thread atual do processo em execução.

- **GS - Data Segment**


### registradores de Flags (EFLAGS)

Registrador de 32 bits que lida com todas as flags, cada bit no caso é referente a uma flag específica, que por sua vez tem o
dever de controlar e execução e operações da CPU, _ligada 1, desligada 0_.

Lista das flags x86 que tenho documentadas :

- **ZF- zero flag**
Quando uma operação é realizada e o resultado é igual a 0, essa flag terá valor 1. Outros resultados ela fica com valor 0 . Para operações de comparação essa flag é modificada..

- **CF - carry flag**
Quando o resultado for muito grande ou muito pequeno para o operando, a CF recebe o valor 1. Então já saberemos que se colocarmos um valor de 64 bits em um registrador de 32 bits , essa flag vai nos alertar. Já outros resultados é 0 o valor dela.

- **SF - signed flag**
Quando o resultado de uma operação for negativa, essa flag é mudada pra 1, quando for positivo fica com o valor 0 mesmo.

- **TF - trap flag**
Utilizado para debugging. Se for 1 a CPU está em debugging, se for 0 não está.
O processador x86 irá executar somente uma instrução por vez quando essa flag estiver ligada.


### registradores Instruction pointer (EIP)

- **EIP - Instruction Pointer**   

Registrador conhecido como “apontador” do programa. Ele é responsável por nos informar qual a próxima instrução a ser executada no programa (instructions pointer).

Na arquitetura x86, o EIP, também conhecido como instruction pointer ou contador do programa, é um registrador que contém o endereço de memória da próxima instrução que será executada pelo programa. O único propósito do EIP é dizer ao processador o que fazer em seguida.

**Nota sobre o register EIP**

Quando o EIP é corrompido (isto é, ele aponta para um endereço de memória que não contém código legítimo do programa), a CPU não será capaz de trazer código legítimo para ser executado, então o programa que estiver rodando irá dar erro. Quando você controla o EIP você pode controlar o que será executado pela CPU, esse é o motivo pelo qual os atacantes tentam obter o controle do EIP em uma exploração. Normalmente os atacantes têm o código de ataque na memória e então alteram o EIP para apontar para o código do exploit


### Virtual Memory and Debugging

Esses registradores que controlam mecanismos importantes do sistema de baixo nível, como : memória virtual, interrupções, e debugging. Tenho algumas informações sobre alguns destes :

- **CR0  -**  *Controla se a paginação de memória está ativada ou desativada*

- **CR2 -**   *Contém o endereço linear que causou uma falha na página*

- **CR3 -**  *É o endereço base da estrutura de dados da paginação*

- **CR4 -**  *Controle as configurações de virtualização de hardware*

- **DR0 -** 

- **DR1 -**  

- **DR2 -**  

- **DR3 -**  

- **DR6 -** 

- **DR7 -** 

_Apesar de vermos sete registradores de debugging acima, o sistema permite apenas quatro Memory Breakpoints (DR0 a DR3): Os registradores restantes são usados para validar status_.


### Model-specific Registers ( MSRs )

Como o nome indica, esses registradores podem variar entre os processadores da INTEL x AMD.  Cada MSR é identificado por um número de 32 bits, e são lidos e escritos através das instruções assembly : **RDMSR e WRMSR .** Eles são acessíveis somente no **ring 0** e normalmente são usados como contadores especiais ou para implementações complexas em baixo nível**. Exemplo :**

*A instrução assembly **SYSENTER** transfere a execução para o endereço armazenado no IA_32SYSENTER_EIP **MSR (0x176 )**, que normalmente é quem manipula as **syscalls**.*