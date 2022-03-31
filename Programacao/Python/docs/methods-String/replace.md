*methodo* : replace() - substitui valores dentro de cadeias de texto.


- O método replace() substitui uma frase especificada por outra frase especificada.

Nota: Todas as ocorrências da frase especificada serão substituídas, se nada mais for especificado. 


- _Sintaxe_ : string.replace(oldvalue, newvalue, count)
- _Args_ : 

> oldvalue = Argumento requerido ( obrigatório ). A String a ser pesquisada na cadeia de texto.
> new value = Argumento requerido ( obrigatório ). String que será colocada no lugar da string 'oldvalue' encontrada.
> count = Argumento opcional. Um número que especifica quantas ocorrências do valor antigo você deseja substituir. O
padrão é todas as ocorrências

---


_exemplos_ :


- Exemplo simples do méthodo 'replace()', alterando o valor citado em uma variável :


		frase = "Ganhei 140 reais em um serviço"
		print(frase.replace('140','1000'))


- Exemplo usando todos os argumentos do méthodo 'replace()', inclusive o 'count' que modifica a quantidade de vezes que
será alterado o valor pesquisado conforme for aparecendo na string. Nesse exemplo será alterado apenas 2x apesar de ter
mais incidências da palavra na string :


		frase = "Ganhei 140 reais em um serviço, Também Fiz 140x uma boa ação e fui para Jundiaí 140x"
		print(frase.replace('140','1000',2))