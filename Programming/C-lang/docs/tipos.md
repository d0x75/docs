C lang - Tipos de dados 
========================


char 
-----


**char = 2^8-1**

( tamanho de dados tipo char : 8 bits / 1 byte )

- O Char é mais utilizado pra receber valores pequenos ou letras específicas de um determinado texto.


1. signed char = 255; ( metade dos bits são positivos e a outra metade nagativos)
2. unsigned char = 255 ( apenas números positivos, uma única sequencia de 0 a 255)

- Formas de declarar variáveis tipo char:

		char a = 10;

		char b = 0xa;

		char c = '\n';


bool
------


( tamanho de dados tipo bool : 8 bits / 1 byte )

- É um novo tipo de variável que foi implementado na versão C99. 

- Esse recurso novo fica está definido no cabeçalho <stdbool.h>, então temos que incluir-lo no inicio do programa.

- Dados booleanos custumam ter apenas dois tipos de valores, false ou true.

- Por padrão tudo que for diferente de 0 será true, e quando for igual a 0 será false.

- Formas de declarar variáveis tipo bool:

		bool b = false;

		bool b1 = true;



int
-----


**int = 2^32-1**

( tamanho de dados tipo int : 32 bits / 4 bytes, caso a arquitetura seja x86-64 o tamanho é dobrado )


- É o tipo utilizado para armazenar valores inteiros(integer). Tem a largura de 4 bytes de tamanho.

- Formas de declarar variáveis tipo int:

		int num = 0xffff;

		int i = INT_MAX;  ( maior tamanho possível para int nessa arquitetura )



short ( short int)
-------------------


( tamanho de dados tipo short : 16 bits / 2 bytes )

- Também é usado para armazenar valores inteiros(integer) com a largura de 2 bytes de tamanho. Então conluídos que o tipo 'short' tem a metade do tamanho tipo int.

- Formas de declarar variáveis tipo short :

		short num = 0;

		short i = USHORT_MAX; ( maior tamanho possível para short nessa arquitetura )



long ( long int)
------------------


( tamanho de dados tipo long : 64 bits / 8 bytes )

- Usado para valores armazenar valores inteiros, com o dobro do tamanho do tipo 'int'.

- Formas de declarar variáveis tipo long :

		long num = 0;

		long i = LONG_MAX; ( maior tamanho possível para long nessa arquitetura )



long long
----------


( tamanho de dados tipo long long : 64 bits / 8 bytes  )


- Para aumentar ainda mais o tamanho de uma variável long, podemos incrementar outras notações 'long', na declaração da variável.

- Também usado para valores armazenar valores inteiros, com o dobro do tamanho do tipo 'int'.

- Esse tipo de 'long long' existe pelo fato de que em algumas arquiteturas de SO como a do MS-Windows , o 'long' tem o tamanho de um 'int' (4 bytes); Mesmo usando um Windows de 64-bits o valor do 'long' deverá caber 32 bits (4 bytes).

- Formas de declarar variáveis tipo long long :

		long long num = 0;

		long long i = LLONG_MAX; ( maior tamanho possível para long long nessa arquitetura )


 
__ int128
------------


( tamanho de dados tipo '__ int128' : 128 bits / 16 bytes )


- Implementado no padrão C99 e funciona apenas para 64 bits.

- Formas de declarar variáveis com tipo = __ int128_t :

			???
		
			
float
-------


**3e2 = 3 * 10^2**

( tamanho de dados tipo float : 32 bits / 4 bytes )


- É a definição utilizada para números reais na computação, seguindo o padrão **IEEE 754**.
		
- Formas de declarar variáveis com tipo float :

			float p = 3.1;

			float f = 1.0;


double
--------


( tamanho de dados tipo double : 64 bits / 8 bytes  )

- Usada também para pontos flutuantes, com precisão Dupla. Consequentemente é o dobro do tamanho da largura do float.

- Formas de declarar variáveis com tipo double :

			double p = 3.1;

			double f = 1.0;


long double
-------------


( tamanho de dados tipo long double : 96 bits / 12 bytes  )

- Usada também para pontos flutuantes.
- O tipo 'long double' não é uma "precisão quadrupla"... 
- O sizeof retorna esses 12 bytes por questão de alinhamento e cache. 
- O 'long double' na realidade tem 10 bytes de tamanho e é conhecido como "precisão estendida".

- Formas de declarar variáveis com tipo long double :

			long double p = 3.1;

			long double f = 1.0;


------


