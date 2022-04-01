#### crunch

Com essa ferramenta é possível criar wordlists personalizadas. Para fazer a personalização da palavra que passarmos como argumento, podemos seguir a tabelinha das regras de personalizar no crunch :


% - Dígitos
^ - Caracteres especiais
@ - Caracteres minúsculos
, - Caracteres maiúsculos

Para utilização do crunch, devemos informar o tamanho do range dos caracteres para a palavra que faremos a wordlist.


Exemplos:

- Gerar uma lista com palavras no tamanho fixo de 10 caracteres, com a palavra base 'eduardo' e 2 personalização de números ( %% ) conforme tabela acima. A lista será salva no arquivo 'wl-edu' .


``
crunch 10 10 -t eduardo%% -o wl-edu
``

- Gerar uma lista com palavras no tamanho fixo de 14 caracteres, com a palavra base 'Gbusiness' , continuada com 5 personalizações de 2 caracteres especiais(^^) e 3 números(%%%).

``
crunch 14 14 -t Gbusiness^^%%% -o wl-gb
``


