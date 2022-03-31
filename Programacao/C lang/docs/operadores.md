# C lang - Operadores



### Procedencia entre operadores.




Operadores Aritiméticos
-------------------------


**Adição** : +

**Incremento** : ++

**Subtração** : -

**Decremento** : --

**Multiplicação** : *

**Divisão** : /

**Módulo**  : %

**Potenciação** : **

**Atribuição**:  =
Esse operador é usado para colocar valores em variáveis.

**sizeof**   : Operador que pega em tempo de compilação o tamanho de bytes da varável que é passada como operando para o sizeof. Exemplos:

		sizeof var
		sizeof(var)
		sizeof("teste")

---


Operadores Relacionais e Lógicos
----------------------------------

Diferente dos operadores aritiméticos os seus operandos e seus resultados não são números mais sim valores lógicos, true e false.

- Lógicos :

**Operador AND**  : &&
Usado para duas ou mais condições. Para que a expressão condicional seja True TODAS as condições devem ser verdadeira.
**Operador OR**   : ||
Usado para duas ou mais condições. Para que a expressão condicional seja True AO MENOS UMA
das condições devem ser verdadeira.
**Operador NOT**  : !
Usado para REVERTE o valor lógico de uma expressão. Oq for TRUE vira FALSE e FALSE vira TRUE
Também esse operador é um operador denomidado UNÁRIO devido requerer apenas 1 operando.

- Relacionais:

**Maior que**       : >
**Maior e igual a** : >=
**Menor que**       : <
**Menor e igual a** : <=
**Igual a**         : ==
**Diferente de**    : !=


Operadores Bitwise ( bit a bit)
---------------------------------

**Operador XOR** : ^

Outros operadores
------------------

**usado para buscar o endereço de memória do seu operando** : 

& 