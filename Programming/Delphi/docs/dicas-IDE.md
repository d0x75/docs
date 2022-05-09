Dicas de Delphi:
-----------------


- Para visualizar os Forms do projeto no Delphi	:
		
		Ir até um ícone com "2 quadradinhos", que chama 'View Form' ou SHIFT + F12
		Clicar nesse ícone e escolher o forme que quiser abrir.



### Maskara usada em campos de valores $$ :


- Máscara para valores númericos no grid = ###,###,##0.00


---


### Atalhos importantes :

- alt + F11 = lista todas as Units do Projeto. E selecionar a unit que precisamos incluir no nosso projeto.
vai gerar um trecho de código abaixo de 'implementation':

		implementation
		uses telaPrincipal;


- Dica de código : sempre comentar as variáveis.

- Dica sobre projetos : quando uma Unit X for refereciar a Unit Y, e também a Unit Y refereciar a Unit X .. faça essa referencia em 'implementation'.



### Abrir outra TELA ( Unit ) no Delphi: 


> Se você quiser abrir um outro form, primeiramente você deve usá-lo no form em que será chamado.
Nas Uses do Delphi, , informe o nome da unit do outro form. Você pode ir no Menu File, Use Unit, e selecionar a unit do form. Depois, no evento do botão, informe: Form2.Show ou Form2. ShowModal.


---




