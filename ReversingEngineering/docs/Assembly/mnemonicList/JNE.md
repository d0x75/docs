# JNE

Jump if not equal

---

### *Opcodes :*

near jump  : 0F 85
short jump : 75


---


### Flags :

ZF = 0

 

**Exemple :**


00401408 | 85C0                                    | TEST EAX,EAX                                                    |
0040140A | 0F85 E5000000                           | JNE crackme#1.4014F5                                            |


Realiza o salto caso ZF seja diferente de 0.