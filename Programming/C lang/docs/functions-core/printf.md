- Esta função está definida do arquivo de cabeçalho <stdio.h>

----------


#### printf()


- Função do arquivo de cabeçalho 'stdio.h'
- Formatos de saída(output) da função printf

		%d - formatador para inteiros com sinal - "signed"
		%f - para saída de variáveis ponto flutuante.
		%u - formatador de inteiros sem sinal -  "unsigned"
		%lu - formatador de inteiros 'long int' 
		%llu - formatador de inteiros 'long long int'
		%x - formatador de valores hexadecimais com letras
		%X - formatador de valores hexadecimais com letras 
		%o - fomatador de valores octais
		%lu - formatador de inteiros 'long int'
		%zu - formatador utilizado pelo operador sizeof
		%c - retorno de caracter, correspondente ao valor
		%i - utlizados para inteiros , equivalente ao' %d'
		p% - quer dizer pointer, pega o endereço em memória que o elemento referenciado está

- Exemplo de uso simples do printf :

		printf("Hello World!\n");

- Limitar as casas decimais quando usamos uma variável float no printf() :

%.2f (duas casas decimais)
%.3f (tres casas decimais)
etc..

