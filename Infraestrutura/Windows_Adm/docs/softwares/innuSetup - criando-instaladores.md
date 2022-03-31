# Criando Instaladores com InnoSetup.

### Conceitos:

- Criar instaladores, dos simples aos mais avançados.

### Preparando o ambiente..

- Fazer o download no (site)[http://www.jrsoftware.org/isdl.php#stable].

- Baixar a versão mais atual.

- Fazer o download do IS TOOL


### Fazer a instalação dos 2 programas que foram baixados.


- Para realizar a instalação basta selecionar o idioma que vai ser escolhido e 'nexts'.


### Criando um instalador simples


#### Abrir o Innu Setup e seguir os seguintes passos:

- Marcar a caixa pra criar um novo arquivo com a 'Wizard', que é a segunda opção.

- Next.

- Colocar o nome da aplicação,a versão,o nome do criador ou da empresa referente e o site referente a empresa ou a pessoa física.

- Informar qual vai ser o diretório em que será criado seu aplicativo e atribuir um nome ao mesmo  > next.

- Agora informaremos o local em que o aplicativo está armazenado e pastas e arquivos que vão precisar conter no instalador também.

- Agora setamos o nome para os atalhos que serão criados do aplicativo e do menu de 'iniciar' do windows.

- Agora, se desejar, você pode informar a documentação do seu aplicativo, bem como mensagem que deve aparecer no início e no fim da instalação.

- Selecionar o(os) idiomas que vão conter no instalador.

- Agora colcoamos a onde vai ser criado o setup(O instalador) que estamos criando e atribúimos o nome do mesmo. Podemos também atribuir uma imgagem.icon para o instalador.

- next > Finish > Yes.

- Salvar o script da criação do instalador que foi criado.



## Observações ao terminar o precedimento.


1.Repare que apesar de ter informado o local onde se deveria registrar as Dll(s) e Ocx(s) o INNO SETUP registrará na pasta que você pediu para residir seu aplicativo. Se você instalar desta maneira irá aparecer aquelas mensagens de erro que nos deixa louco da vida e perguntando; o que fiz de errado? O que devo fazer para corrigir o problema?


2.Bom, para corrigir esse erro você deve informar no script onde as Dll(s) e Ocx(s) devem ser registradas. Para tanto basta mudar o endereço “{app}” para o caminho da pasta system32 que e o seguinte: “C:\\WINNT\system32”. Depois basta clicar em “RUN” para que compilação seja refeita.Pronto, seu aplicativo está pronto para ser distribuído.



