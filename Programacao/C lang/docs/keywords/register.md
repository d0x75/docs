#### register 


- Usado como prefixo para declaração de variáveis. Ao invés de alocar a variável na memória, a variável é alocada em um registrador

- Em tese, variáveis são um espaço em memória, no qual dados são armazenados/copiados pra lá.

- Ao invés de alocar a variável na memória, a variável é alocada em um registrador. Ou seja, o dado não vai entrar na memória RAM e sim ficar no registrador declarado. 
( Pode variar de arquitetura p/ arquitetura )

- Lembrando que os registradores são considerados uma "memória mais rápida" por fazer parte do próprio processador.

- Resumindo é uma otimização VIA CÓDIGO para declarar uma variável, a declaração é feita assim:

``
register int i = 0;
``
