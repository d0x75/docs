Jekyll Anotações:
------------------

## Liquid templates, 

É uma linguagem de templates que o Jekyll utiliza bastante. É estabelecida por 3 componentes principais : 

- objects : Dizem ao Liquid para gerar variáveis predefinidas como conteúdo da página.
É usado chaves duplas para referenciar objetos :

        O Objeto {{ page.title }} exibe a variável page.title

- tags : Criam a lógica e controle de fluxo para o template, são identificados pela
notação _{% and %}_.Exemplo :

        {% if page.show_sidebar %}
        <div class="sidebar">
        sidebar content
        </div>
        {% endif %}

nesse exemplo acima, vai ser exibido o "sidebar content" quando a variável da página show_sidebar for TRUE.


- filters :

Os filtros são alteram a saída de um Liquid Object. Eles são usados para modificar uma saída de dados e devem ser separados por '|'.

        {{ "hi" | capitalize }}

isso vai exibir 'Hi' ao invés de 'hi'.


---

- como utilizar Liquid:

1. Adicionar o FrontMatter no inicio das páginas para fazer com que o Jekyll use o
Liquid nelas.

2. Fazer uma mundaça no arquivo 'index.html' usando um filter para modificar a saída do
texto para caixa baixa. Usando o filtro 'downcase' no caso. Exemplo :
    
        {{ "Hello World!" | downcase }}



------------


## Front Matter

É um fragmento de código YAML colocado entre duas linhas com 3 traços no ínicio do
arquivo. Podemos usar o FrontMatter para definir variáveis para a página. Ex :


    ---
    number: 10
    ---

Podemos chamar variáveis Front Matter no Liquid usando a variável _page_.


    {{page.number}}


## Layouts

- Layouts são modelos que podem ser usados por qualquer página do seu site e envolvem o conteúdo da página. Eles são armazenados em um diretório chamado ``_layouts``

- Para fazer a página como o 'index.html' usar um layout criado, devemos chamar a variável ``layout`` no ``front matter`` por exemplo.


*content* é uma variável especial que retorna o conteúdo renderizado da página na qual é chamada.




## Includes

- As include tags permite que você inclua conteúdo de outro arquivo armazenado na pasta
``_includes``. Esse método é útil para ter um único código fonte que se repete em toda página ou para melhorar a legibilidade.

- Então para incluir um conteúdo padrão em todas as páginas, podemos usar um include no layou default, .. incluindo o seguinte trecho no corpo da página:

        {% include navigation.html %}


## Data Files

- O jekyll permite o carregamento de arquivos YAML,JSON e CSV que devem estar localizados em ``_data``.

- Vamos ver como aramarzar o conteúdo da navegação em um desses arquivos de dados e fará interação sobre ele no include da navegação. Exemplo desses dados de navegação em YAML :

                - name: Home
                link: /

- O jekyll disponibiliza esse arquivo para interagirmos na variavel ``site.data.navigation``, para não termos que mexer em ``_includes`` e alterar o html, podemos fazer interações no dos dados YAML que irá funcionar perfeitamente.



---


## 

.....