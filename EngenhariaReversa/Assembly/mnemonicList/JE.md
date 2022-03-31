# JE

Jump if equal

Instrução JE - ( vai realizar um salto caso ZF = 1 )

---

#### Opcodes :

near jump   : 0F 84
short jump : 74

---


### Flags :

ZF = 1

 
**Exemple :**


004013C2 | 74 05| JE crackme#1.4013C9


Realiza o salto caso ZF=1
Na prática vai realizar o salto se a ultima instrução for = 0(true).




--
