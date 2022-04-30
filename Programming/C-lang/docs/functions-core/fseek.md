- Esta função está definida do arquivo de cabeçalho <stdio.h>

----------


fseek() - Função que a partir do começo ou fim de um arquivo que foi aberto, muda
o fluxo para determinada parte de um arquivo. Essa "determinada" parte é o offset
em disco da parte do arquivo que precisamos chegar(no caso o parâmetro 
long_Offset).

- protótipo : ``int fseek (FILE * fp, long _Offset, int origem);``


*Exemplos*:


---