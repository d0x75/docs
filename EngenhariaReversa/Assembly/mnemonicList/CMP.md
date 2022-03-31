# CMP (Comparer Two Operands)

Instrução CMP É utilizada para fazer comparação entre 2 operandos e define as Flags do registrador EFLAGs para controlar o fluxo da próxima instrução.

---


#### Opcodes

Opcode	    | Mnemonic		   | Description
---------------------------------------------------------
3C ib		CMP AL, imm8		Compare imm8 with AL.
3D iw		CMP AX, imm16		Compare imm16 with AX.
3D id		CMP EAX, imm32		Compare imm32 with EAX.
80 /7 ib	CMP r/m8, imm8		Compare imm8 with r/m8.
81 /7 iw	CMP r/m16, imm16	Compare imm16 with r/m16.
81 /7 id	CMP r/m32,imm32		Compare imm32 with r/m32.
83 /7 ib	CMP r/m16,imm8		Compare imm8 with r/m16.
83 /7 ib	CMP r/m32,imm8		Compare imm8 with r/m32.
38 /r		CMP r/m8,r8			Compare r8 with r/m8.
39 /r		CMP r/m16,r16		Compare r16 with r/m16.
39 /r		CMP r/m32,r32		Compare r32 with r/m32.
3A /r		CMP r8,r/m8			Compare r/m8 with r8.
3B /r		CMP r16,r/m16		Compare r/m16 with r16.
3B /r		CMP r32,r/m32		Compare r/m32 with r32.


---

### Flags :


As flags CF, OF, SF, ZF, AF, and PF flags são afetadas de acordo com o resultado da operação.



---


**Sintaxe :**

cmp <reg>, <reg>
cmp <reg>, <mem>
cmp <mem>, <reg>
cmp <reg>, <con>

**Exemple :**

Faz a comparação entre um operando de origem x outro operando de origem; e define as EFLAGs de acordo com seu resultado.

``cmp DWORD PTR [0x505000], 10
je 0x401110``
Compare os 4 bytes armazenados no endereço 0x505000 com a constante inteira de 4 bytes '10'. Caso seja igual pulo para o endereço 0x401110.