### attrib

Com esse comando podemos verificar os Atributos de um arquivo e também setar atributos para o mesmo. Para sabermos como identificamos os tipos de atributos:

		attrib /?

Para apenas verificar quais atributos todos os arquivos do diretório atual usamos:

		attrib /s

Para adicionar ou remover atributos de um arquivo, seguimos a seguinte sintaxe

		attrib +A teste.pdf

		attrib -A teste.pdf

		attrib +H (ocultar diretório/arquivo passado como parâmetro)

		attrib -H = revelar