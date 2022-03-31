OllyDbg - Tricks
=================


**Variações do OllyDbg**

- OllyDbg 1.10
- OllyDbg 2.01

- Ollydbg Shadow
- Ollydbg CiMs Edition
- Ollydbg UST_2bg



Ollydbg - CallStack
---------------------

- Recurso do Olly que armazena em forma de "logs" as calls que são feitas na execução do software. Podemos utilizar esse recurso para rastrear chamadas que foram feitas sem que a gente soubesse, e ao chegar nessas calls podemos identificar o motivo pelo qual a mesma foi executada... OU NÃO.


---


Ollydbg - IntermodularCalls
-----------------------------


#### Anotações sobre o conteúdo:


- No contexto de Debugger, o dump é um recurso que pode ser apontado para qualquer parte do código ou melhor em qualquer endereço de memória.

- O valor do registrador ESP, sempre será o mesmo valor do endereço do topo da pilha.

- SS = Stack Segment ( Indica que os valores em questão, vão ir direto pra Pilha )

#### Recursos do Olly:

1. Listar todas as chamadas Intermodulares:

		botão direito > Search for > All intermodullar calls 


---


Salvar modificações no arquivo usando o OllyDbg
-------------------------------------------------

1. Botão direito em qualquer lugar da tela.
2. Edit > Copy all modifications to executable.
3. Irá abrir outra tela.
4. Botão direito > Edit > Select All
5. Botão direito > Save file