# SHR (Shift à direita)

Essa instrução é usada para deslocar os bits do conteúdo referente ao primeiro operando para direita, 
preenchendo com zeros as posições de bits vazios. O operando pode ser deslocado para 31 posições. O Número de bits a serem deslocados é atribuído pelo 2operando que pode ser uma constante de 8 bits ou o registrador CL.


---


#### Opcodes




---

### Flags :



---


**Sintaxes :**

shr <reg>, <con8> 
shr <mem>, <con8> 
shr <reg>, <cl>
shr <mem>, <cl>

**Exemple :**

``shr ebx, cl``
Armazena em EBX o resultado da divisão do valor de EBX por 2 n onde n é o valor aramzenado no registrador CL.