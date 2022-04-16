### ls

Comando utilizado para listar os diretórios e arquivos do local em que estivermos

##### Formas de utilizar :

Utilizando apenas ls , irá apenas aperecer a lista com os nomes das pastas e arquivos :

``ls``

- Quando passamos o parâmetros -a , conseguimos ver os arquivos ocultos ao listar.

``ls -a``

- Faz a listagem exibindo os arquivos e diretórios em colunas e ordenadas em vertical

``ls -c``

- Exibe várias informações/permissões dos arquivos  e diretórios em vertical

``ls -l``

- Mostra os arquivos executáveis com um * na frente do mesmo

``ls -F``

- Mostra os arquivos se baseando no ultimo acesso aos mesmos.

``ls -u``

- Lista os arquivos na ordem inversa

``ls -r``

Fais a listagem normal e acrescenta uma listagem dos diretórios e subdiretórios que estiverem aninhados

``ls -R``

Listar apenas os itens que tenham o nome que começe da letra A até a C

``ls [a-c]*``


---


Sobre arquivos que iniciam com ' - ' , por exemplo '-teste.txt' . Não é possível deletar um arquivo com esse nome com um comando padrão como : "rm -teste.txt" .
Para deletar arquivos nessa situação, temos de fazer de outro jeito :

- "rm ./-teste.txt"
- "rm -- -teste.txt"