# SHL (Shift à esquerda)

Essa instrução é usada para deslocar os bits do conteúdo referente ao primeiro operando para esquerda, preenchendo com zeros as posições de bits vazios. O operando pode ser deslocado para 31 posições. O Número de bits a serem deslocados é atribuído pelo 2operando que pode ser uma constante de 8 bits ou o registrador CL.

---


#### Opcodes




---

### Flags :



---


**Sintaxes :**

shl <reg>, <con8>
shl <mem>, <con8>
shl <reg>, <cl>
shl <mem>, <cl>

**Exemple :**

``shl eax, 1``
Multiplique o valor de EAX por 2 (se o bit mais significativo for 0)
