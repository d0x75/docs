#### cewl

CEWL - Custom wordlist generator . É um programa escrito em ruby que rastreia determinada URL e profundamente segue seus links externos e retorna uma lista de palavras que pode ser associada a uma wordlist. https://github.com/digininja/CeWL

Exemplos de uso:


- Gerar uma lista de palavras que contém na URL passada como parâmetro :

``
cewl www.cortezadelima.com.br
``

- Gerar uma lista de palavras com no máximo 5 caracteres das palavras contidas na URL passada como parâmetro :

``
cewl www.cortezadelima.com.br -m 5
``

- Um comando que gera uma word list ativando o modo Verbose (-v), usando o parâmetro Deep com seu valor padrão (-d), limitando a quantidade de caracteres de cada palavra para no Mínimo 5, e mandando escrever a wordlist gerada no 'arquivot.txt'.
 

``
cewl www.cortezadelima.com.br -v -d 2 -m 5 -w arquivo.txt
``