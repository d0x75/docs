# AND ( Bit a Bit Lógico AND )

Faz a operação lógica especificada nos seus operandos. O resultado é armazenado no local do primeiro operando.

---


#### Opcodes




---

### Flags :



---


**Sintaxes :**

and <reg>, <reg>
and <reg>, <mem>
and <mem>, <reg>
and <reg>, <con>
and <mem>, <con>


**Exemple :**


``and eax, 0fH ``
Zera tudo, exceto os últimos 4 bits de EAX.