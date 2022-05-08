### set

> Esse comando é bem robusto, mais sua principal funcionalidade é setar variáveis para que possamos programar em batch. Para setar uma variável no bat é simples, basta seguir a seguinte anologia : [nome da variável]=[cadeia de caracteres]

		set nome=Eduado Barbosa da Silva

> Agora para chamar a variável que setamos acima, basta dar um echo com o nome da variável entre % % . Da mesma forma que usamos para chamar uma variável nativa. Lembrando que podemos utilizar a variável criada, apenas na instancia do cmd em que estivermos pois a mesma não é uma variável NATIVA como a %time%,%date% etc..

		echo %nome%

> Vamos atribuir valor a uma variável com a interção do usuário agora. Ou seja, vamos setar uma variável que seu valor será digitado pelo usuário e depois ser guardado nela, para isso utilizaremos o parâmetro   /p. Exemplos:

		set /p nome=0

		set /p "nome = >"

		set /p teste=Digie algo aqui^>

> Também podemos fazer cálculos simples e compostos utilizando variáveis de uma forma bem prática, pois como falamos anteriormente as variáveis no bat não são tipadas . Então basta seguir a anologia citada acima 'nome=conjunto de caracteres'. Mais  para setarmos variáveis que participarão de cálculos usamos o parâmetro /a. Exemplo:

		set /a 10 * 10

- Para utilizarmos o conceito de concatenação de variáveis no Bat, fazemos da seguinte forma:

		set var = edu
		set var2 = ardo
		echo %var%%var2%

> Podemos trabalhar com um conceito de substituição no bat, ou seja podemos substituir dados do valor da variável, no caso a "cadeia de caracteres" que falamos antes.. No exemplo vamos trocar todas as letras 'a' por 'z'. Ex:

		set /p "usuario=Usuario>"
		echo %usuario:a=z%

> Também usamos o conceito de EXTRAÇÃO nas variáveis, para estar extraindo partes da cadeia de caracteres, ou melhor posições da matriz/cadeia de caracteres . As posições própriamente ditas começam da posição 0 e vão seguindo 1,2,3... Ex:

		set /p usuario:a~0,3