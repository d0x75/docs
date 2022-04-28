# PUSH (empurrar/empilhar) - Push Word, Doubleword or Quadword Onto the Stack

Empurra seu operando para o topo da stack. Na verdade primeiramente é decrementado -4 do registrador ESP e depois é colocado o valor do operando no endereço de ESP.



--- 


#### Opcodes :

(Opcodes: FF, 89, 8A, 8B, 8C, 8E, ...

FF /6 - PUSH  - r/m16
FF /6 - PUSH  - r/m32 
FF /6 - PUSH  - r/m64 
50+rw - PUSH  - r16 O 
50+rd - PUSH  - r32
50+rd - PUSH  - r64
6A ib - PUSH  - imm8 
68 iw - PUSH  - imm16 
68 id - PUSH  - imm32 
0E 	  -	PUSH  - CS 
16 	  - PUSH  - SS 
1E 	  - PUSH  - DS 
06 	  - PUSH  - ES 
0F A0 - PUSH  - FS
0F A8 - PUSH  - GS 


---


### Flags :

...
 
---


**Sintaxes :**

push <reg32>
push <mem>
push <con32>


**Exemple :**

``
PUSH EAX
``

Joga no topo da pilha o valor do conteúdo passado como parâmetro para PUSH
Copia de um registrador específico a posição de memória constante para o TOPO DA PILHA.
Essa instrução também decrementa o ponteiro da pilh(ESP) em 2,4 ou 8; depende do tamanho do operando. Então copia o operando para a posição em memória apontada pelo ESP após ter sido decrementeado.