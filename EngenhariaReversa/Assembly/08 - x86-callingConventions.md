# Calling conventions ( convenção de chamadas )


As Calling Conventions é uma regra de como deve funcionar o CALL. Ou seja como chamar uma subrotina e retornar. Isso acontece para que programadores consigam compartilhar códigos que podem ser utilizados por outros sem problemas.

Por exemplo , se tivermos analisando algum programa que segue a convenção de chamada 'cdecl' o programador vai ter que seguir um conjunto de regras que rege sobre a conveção 'cdecl'; e o programador não precisara examinar a subrotina para saber como deverá passar os parâmetros, pois isso já está definido na 'clcl'.


---

### Lista de calling conventions mais conhecidas :


``__cdecl`` 

- Essa é a calling convention padrão usada pela linguagem C/C++.
- É baseada na utilização das instruções assembly : _push,pop,call,ret_

- Os parâmetros da subrotina são colocados na pilha
- Os registradores são salvos na pilha com o valor original do momento da CALL.
- As variáveis locais usadas pela subrotina são colocadas na memória da Stack.

Essa conveção de chamada é separada em 2 conjuntos de regras. O primeiro conjunto é empregado pelo Chamador da subrotina e o segundo conjunto de regras é observado redator da subrotina ( o Chamado).

**Regras do Chamador** :

1. Salvar o conteúdo dos registradores EAX,ECX e EDX na pilha, antes de chamar a subrotina. Então caso a subrotina altere o valor desses registradores, teremos o valor original na pilha para ser restaurado antes do RET.

2. Antes das chamadas (CALL) devemos empurrar para a Stack os parâmetros/argumentos na ordem inversa
( do ultimo parâmetro p/ o primeiro). Isso ocorre por que os argumentos vão sendo empilhados na Stack, então o último argumento empurrado em ordem inversa, será o primeiro argumento que estará no topo da Stack.

3. Use a instrução CALL para chamar a subrotina. Essa instrução vai colocar o endereço de retorno no topo dos parâmetros da Stack e desvia o código para o memory adress da subrotina. Dessa maneira a subrotina foi invokada com sucesso e deve seguir as regras abaixo.


Após a chamada CALL, encontramos o valor de retorno no registrador EAX. Para restaurar o estado da máquina normalmente é feito o seguinte:

1. Remova os parâmetros da pilha. Por exemplo caso tenha 10 parâmetros na pilha, limpamos com um simples: ADD ESP,10
2. Restaure o conteúdo dos registradores EAX,ECX,EDX salvos no stack antea da chamada. Os valores dos registradores salvos pelo chamador (ECX e EDX) podem ter sido alterados. Se o chamador os usar após a chamada, seria necessário
salvá-los na pilha antes da chamada e restaurá-los depois dela.


**Regras do Callee** :


1. Colocar o valor de EBP na pilha e copie o valor de ESP para EBP usando as seguintes instruções assembly:

		push ebp
		mov ebp, esp


Essa primeira instrução é para manter o EBP e referenciar-lo na Stack. O base pointer(EBP) é usado por convenção como ponto de referencia para encontrar parâmetros e variáveis locais na Stack.

Empurramos o valor do ponteiro de base(EBP) antigo no início da sub-rotina(PUSH EBP) para que possamos restaurar mais tarde o ponteiro base(EBP) apropriado para o programa quando a subrotina retornar. ( pois o programa não espera que a subrotina altere o EBP).

Depois movemos o valor do ponteiro da pilha(ESP) para EBP para obtermos nosso ponto de referencia para os parâmetros
e variáveis locais.

2. Em seguida, aloque as variáveis locais criando espaço na pilha. Lembre-se de que a pilha diminui, portanto, para liberar espaço no topo da pilha, o ponteiro da pilha deve ser diminuído. O valor pelo qual o ponteiro da pilha é diminuído depende do número e do tamanho das variáveis locais necessárias. Por exemplo, se 3 inteiros locais (4 bytes cada) forem necessários, o ponteiro da pilha precisará ser diminuído em 0x12 para criar espaço para essas variáveis locais (ou seja, sub esp, 0x0c ).




---


``__stdcall``
``__fastcall``