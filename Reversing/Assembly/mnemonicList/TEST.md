# TEST

Teste lógico

---

#### Opcodes

near jump  :
short jump :


---


### Flags :

ZF ,CF ,OF

 
---


**Exemple :**

``
TEST EAX, EAX
``

Executa uma lógica ( AND ), mas não guarda o valor . Ativa apenas a FLAG Z quando o EAX == 0.
Ou pode zerar a FLAG Z quando EAX for diferente de 0.

As FLAGS CF e OF, sempre serão ativadas por essa instrução.