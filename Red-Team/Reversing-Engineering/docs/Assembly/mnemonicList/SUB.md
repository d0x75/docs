# SUB - Subtraction (subtração)

Instrução SUB - Substract ( utilizada para operações de subtração )

Essa instrução subtraí o valor do segundo operando do seu primeiro operando e guarda o resultado no operando de
destino(primeiro operando).


---

#### Opcodes :


83 - SUB r/m32, imm8

---


### Flags :

...


---

**Sintaxe :**

sub <reg>, <reg>
sub <reg>, <mem>
sub <mem>, <reg>
sub <reg>, <con>
sub <mem>, <con>

 
**Exemples :**

1.
``sub al, ah``
AL ← AL - AH

2.
``sub eax, 216 ``
Subtrair 216 do valor armazenado em EAX e guardar no próprio EAX o resultado.


004013C2 | ....



Subtrai o valor referente ao segundo operando ( operador de origem ), do primeiro operando ( operador de destino); e armazena o resultado no operando de destino.
Tendo em vista que o operador de destino pode ser : registrador ou um endereço de memória . E o operador de origem pode ser : valor imediato, registrador ou algum
endereço de memória válido. ( Dois operandos referente a memory address não podem ser usados juntos em apenas 1 instrução destas ) ......... 


