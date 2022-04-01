# ADD - Adicição de Inteiros

Essa instrução soma os seus 2 operandos e guarda o resultado no operando de destino(seu primeiro operando). No máximo 1 operando por instrução pode ser um memory adress.


---


#### Opcodes




---

### Flags :



---


**Sintaxes :**

add <reg>, <reg>
add <reg>, <mem>
add <mem>, <reg>
add <reg>, <con>
add <mem>, <con>

**Exemples :**

1.
``add eax, 10``
EAX = EAX + 10

2.
``add BYTE PTR [variavel], 10 ``
Adiciona 10 ao único byte armazenado no endereço de memória var
