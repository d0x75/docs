Uma instrução **x86** completa, terá o mnemônico da instrução a ser executada, depois o Operador de destino ( *dest* ) onde ficará o resultado da operação, e por último eventualmente podemos ter outro operador conhecido como Operador de origem ( *src* ). Mas também podemos ter instruções com o mnemônico e um operador ou com apenas o mnemônico.

*Exemplos :*

``  
 Mnemônico      Op.dest    Op.src
  MOV            ECX,       0x42
  LEA            EDX,       [EBP-28]
  SUB            ESP,       0x0  
  PUSH           EBP
  XOR            EAX,       EAX
  JMP            0x401014       
``

**Operandos** 

Os tipos de operandos que podemos utilizar são classificamos da seguinte maneira :

``
Valores Imediatos : 0x42, 0x00401828, 0x0C , [EAX+0xf], [0xc0ffe]
Registradores : EAX, ECX, EBP, ESP+1
Offsets de memória : [0x0012F8D4], [ECX], [EBX+0x08], [EBP-0x10*2]
``

Semelhante a outras convenções da linguagem assembly o **x86** usa o Colchetes [ ] para indicar acesso na memória. ( a única exceção é a instrução LEA, que usam [ ] mas na verdade não faz referência a memória)

Quando passamos valores de operandos entre colchetes, como por exemplo : [0xff273] estamos referindo ao valor que se encontra nesse endereço de memória; ou seja esse valor em colchetes é apenas um ponteiro pro valor que será usado.

O conjunto de instruções que o **x86** fornece, são bem flexível em relação a movimentar dados entre a memória e os registradores. Os dados podem ser movidos das seguintes formas :

- *de Imediato para o Registrador*
- *de Registrador para Registrador*
- *de Imediato para a Memória*
- *de Registrador para Memória e Vice-versa*
- *de Memória para a Memória*

*Os primeiros quatro métodos são suportados por todas as arquiteturas modernas, mas o último é específico para x86.*

Um lembrete importante é que o **x86** usa o tamanho de instruções de comprimento variável: no **x86** comprimento da instrução pode variar de 1 a 15 bytes.

Instruções assembly normalmente se enquadram nas seguintes 3 categorias que irei esmiuçar adiante : 
**data movement, arithmetic/logic e control-flow.**



## data movement

## arithmetic/logic

## control-flow

