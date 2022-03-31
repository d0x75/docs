# function

Functions é referente a funções, que se não a, é uma das mais importantes construções da linguagem C.

Cada programa C começa a execução a partir da função principal ( main() ), que também tem um tipo de retorno que por padrão é 'int' e também pode ter parâmetros.

Variáveis criadas dentro de funções, são variáveis locais apenas para serem usadas dentro
daquele contexto da função. Porém se as variáveis são criadas na função 'main()' elas se tornam variáveis globais, então podem ser usadas dentro de outras funções além da 'main()'.

#### Write functions


1. Declarar O PROTÓTIPO  da função no inicio do programa, antes da função main(). Normalmente as funções declaradas após as diretivas de préprocessador.

2. Usar a função em algum ponto do bloco de códigos da main().

3. Definir a função completa, começa com uma linha igual ao protótipo mais não é encerrado com aquele ';' e também é usado de parâmetros reais há o bloco de código com as instruções
para a função executar.


- Como passar parâmetros para funções :
Existem 2 maneiras diferentes, por VALOR e por REFERÊNCIA.
	
		VALOR = quando passamos diretamente um valor, ou uma variável com um conteúdo.
		REFERÊNCIA = quando passamos o endereço de memória onde está a variável/cónteúdo.














Sintaxe básica :

	int funcName(p1,p2){code;}

	int = TIPO DE RETORNO DA FUNÇÃO
	funName = NOME DA FUNÇÃO
	(p1,p2) = LISTA DE PARÂMETROS , NO CASO APENAS 2.
	{} = INSTRUÇÕES DA FUNÇÃO.



- Se quisermos uma função que some dois números inteiros e retorne um número de ponto flutuante, fazemos assim :


		float funcFloat(int n1, int n2){}
		