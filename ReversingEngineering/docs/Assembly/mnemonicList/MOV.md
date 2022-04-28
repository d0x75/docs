# MOV

Move (mover)

Instrução que normalmente é usada para mover dados entre o processador e a memória. Movimentação de dados de memória para memória não é possível.


---


#### Opcodes :

(Possible Opcodes: 88, 89, 8A, 8B, 8C, 8E, ...)

---


### Flags :

... 

---

**Sintaxes**

mov <reg>, <reg>
mov <reg>, <mem>
mov <mem>, <reg>
mov <reg>, <const>
mov <mem>, <const>


**Exemples :**

1.
``
MOV dest, src
``
Instrução moverá o valor do operador de origem(SRC) para o operador de destino(DEST).

2.
``
mov byte ptr [var], 5
``

Armazena o valor 5 no byte no local var