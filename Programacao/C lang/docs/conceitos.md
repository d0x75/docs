## Case sensitive

- O C é sensível ao tipo de caracter utilizado, por padrão se usa apenas letras minúsculas.

## Declarações C


Uma declaração é uma construct da linguagem C que introduz um ou mais identificadores no programa e especifica seu significado e suas propriedades. 


#### identificadores

Existem algumas regras para denominação de identificadores , no caso os nomes que damos as funções,variáveis e rótulos, e são as seguintes regras :

- O primeiro caracter de um identificador deve ser uma letra ou um sublinhado ``_``.
- Do segundo caracter pra frente pode ser número,letra ou sublinhado.
- Somente é válido os primeiros 32 carcteres.
- Letras maiúsculas são diferentes de minúsculas. (case sensitive)

As declarações podem aparecer em qualquer escopo do programa. Cada declaração termina com um ponto e vírgula e consiste
em duas partes distintas:

``
specifiers-and-qualifiers 
declarators-and-initializers ;
``

#### espificicadores e qualificadores

Podemos usar mais de um especificador/qualificador juntos, separados apenas por 'space' e em qualquer ordenação. (a que fizer mais sentido)

- especificadores de tipo :

. void
. algum tipagem padrão da linguagem ( char,short,int,float,double etc...)
. atomic type
. alguma tipagem definida por "typedef"
. struct, union ou enum

- especificadores de classes de armazenamento :

. typedef
. auto
. register
. static
. extern
. thread_local

- qualificadores de tipo :

. const 
. volatile 
. restrict 
. Atomic ( usar a _ antes desse qualificador )

- especificadores após declaração de funções : 

. inline
. Noreturn ( usar a _ antes desse especificador )

- especificadores de alinhamento

. Alignas ( usar a _ antes desse especificador )


#### declaradores e inicializadores :

Os declaradores devem ser separados por vírgula, caso tenha mais de um. 
Os declaradores também podem ser acompanhados por inicializadores. 
As declarações enum, struct e union podem omitir os declaradores e, nesse caso, elas apenas apresentam as constantes de enumeração / tags.

####; : 

O ponto e vírgula é sempre usado para indicar o fim da declaração.


_Exemplo_ :

		int a, *b=NULL; // "int" is the type specifier,
		                // "a" is a declarator
		                // "*b" is a declarator and NULL is its initializer
		const int *f(void); // "int" is the type specifier
		                    // "const" is the type qualifier
		                    // "*f(void)" is the declarator
		enum COLOR {RED, GREEN, BLUE} c; // "enum COLOR {RED, GREEN, BLUE}" is the type specifier
		    
		                                // "c" is the declarator

---

## Compilação C

- É o processo que faz nosso código escrito em uma linguágem de alto nível transformar em um código que o processador consiga digerir. ( código de máquina )

- O processo de compilação, é descer dessa camada de alto nível até o hardware que é o ultimo nível de abstração.

Exemplo prático de uma compilação de um código C:

		int c;
		printf("Hello.\n");
		exit(0);
 
	----

		55
		8b ec
		8b ec 40

- Quando um código C é compilado, teremos apenas os Hexadecimais para fazer a análise. Mais também podemos pegar esses Hexadecimais ( código de máquina ) e transforma-los em em uma línguagem intermediária, que é mais amigável para entendermos ( Assembly ). Para isso faremos o Disassembly. Ex:


		55
		8b ec
		8b ec 40

   ----

		PUSH EBP
		MOV EBP, ESP
		SUB ESP, 0X40
