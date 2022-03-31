Diretivas de pré-processamento
===============================

**O que são diretivas de préprocessador** :

- Essa é um instrução para o Compilador resolver, e não gera código que entrará no programa
final.

- Antes do começo da maioria dos programas em C, pode conter diretivas de pré processamento.

- Quando vermos uma notação iniciada '#' antes da main(), já entendemos que trata-se de uma diretiva de pré-processamento. 


'#include'
----------

- O #include diz para o compilador que carregue o arquivo passado em '<>' inteiro e colocar
no programa.
- O #include, irá receber um arquivo de cabeçalho como argumento. 
- O arquivo passado como argumento vai fazer parte do programa em si.

- Exemplo de 2 jeitos de passar o parâmetro pro #include :


		#include<stdio.h>
			or
		#include"/usr/include/stdio.h"

- Então podemos concluir que a diretiva #include trás para nosso programa recursos de arquivos de cabeçalho escritos em C . Então conseguimos utilizar em nosso programa, tudo que foi programado no arquivo de cabeçalho que for incluido( como funções, structs etc..).

------


### #define

------

### #if

------

### #else

----

- Others :

if
elif
else
endif	
defined

ifdef
ifndef
define
undef

include
line
error
pragma
