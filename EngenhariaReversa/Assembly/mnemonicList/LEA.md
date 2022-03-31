## LEA - Load Effective Address 
(guarda o endereço do segundo operando, no primeiro operando)

Não é possível trabalhar com endereços de memória com essa instrução.

---


#### Opcodes :



---


### Flags :

... 

---

**Sintaxes :**

lea <reg32>, <mem>


**Exemples :**

1.

``lea edi, [ebx + 4 * esi]``
A quantidade EBX + 4 * ESI é colocada no EDI.

2.
``lea eax, [var]``
O valor em var é colocado em EAX.

3.
``lea eax, [val]``
O valor val é colocado em EAX.