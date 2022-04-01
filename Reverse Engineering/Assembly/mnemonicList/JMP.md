# JMP ( salto )

Transfere imediantamente o fluxo do programa para a localização de memória indicada pelo seu operando.


#### Opcodes

**near jump :** 
**short jump :** 
---



---

### Flags :



---


**Sintaxes :**

jmp <label> 

or

jmp <offset>


**Exemples :**

1.
``jmp MessageBoxA``
Salta para o endereço de memória onde está a função rotulada como MessageBoxA.

2.
``jmp 0x401004``
Salta para o endereço de memmória 0x0401004.
