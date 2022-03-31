# IDIV (Divisão de inteiros)

Essa instrução divide o valor do inteiro de 64 bits *EDX:EAX* pelo valor do operando utilizado. O resultado do quociente da divisão é armazenado em EAX e o resto em EDX.

---


#### Opcodes




---

### Flags :



---


**Sintaxes :**

idiv <reg32>
idiv <mem>

**Exemples :**

``idiv ebx``
Divide o conteúdo de EDX:EAX pelo conteúdo de EBX. Armazenar o resultado do quociente em EAX e o resto em EDX.

``idiv DWORD PTR [var]`` 
Divide o conteúdo de EDX:EAX pelo valor de 32 bits armazenado na localização da memória var . Armazenar resultado do quociente em EAX e o resto em EDX.