# IMUL (Multiplicação de inteiros)

Essa instrução pode ter 2 formatos básicos, uma utiliza 2 operandos e a outra utiliza 3 operandos.

- 2 operandos
Dessa forma o primeiro operando deve ser um registrador, pois vai guardar o resultado da multiplicação entre o 1operando * 2operando.

- 3 operandos
Dessa forma o primeiro operando também deverá ser um registrador, pois irá guardar o resultado da multiplicação entre o 2operando * 3operando. Lembrando que o 3operando nesse caso deverá se um valor Constante.

---


#### Opcodes




---

### Flags :



---


**Sintaxes :**

imul <reg32>, <reg32>
imul <reg32>, <mem>
imul <reg32>, <reg32>, <con>
imul <reg32>, <mem>, <con>

**Exemple :**

``imul eax, [var]``
Multiplique o conteúdo de EAX pelo conteúdo de 32 bits da localização da memória var. Colocar resultado em EAX.


``imul esi, edi, 25``
ESI = EDI * 25
