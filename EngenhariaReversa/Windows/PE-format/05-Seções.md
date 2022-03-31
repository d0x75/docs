PE Sections
=============



- Contém o conteúdo principal do executável. ( código, dados, recursos etc.. )
- Aqui estão os dados das seções que os cabeçalhos estão apontando. ( raw data )
- Podem ser organizadas da forma que o compilador quiser, desde que nos headers haja informações suficientes para acessar-las.

- Aplicações Windows NT típica pode possuir 9 seções predefinidas:

		.text
		.bss
		.rdata
		.data
		.rsrc
		.edata,
		.idata,
		.pdata,
		.debug

- Algumas aplicações não necessitam de todas as seções citadas no exemplo acima.
- Vejamos algumas das principais seções e suas funcionalidades:

**.text ou .CODE** : Seção de código do executável, quando o binário é compilado em Delphi a seção de código costuma ser .CODE ao invés do mais conhecido .text .

**.bss**   :  Dados não inicializados, variáveis estáticas.

**.rdata** : read-only, strings e constantes

**.data**  : as demais variáveis globais.

**.rsrc** : resources são os ícones,cursores,bitmaps,imagens etc. É uma Estrutura de direório em árvores

**.edata** : nomes e endereços exportados pelo PE.

**.idata** : IAT. Funções importadas pelo PE.

**.tls**   : Thread local storage, armazenamento de informações relativa a cada Thread.




## Dicas

quando tem a notação 'virtual' na keyword, como por exemplo virutalAddress,virtualSize etc.. normalmente é relacionado a memória.

quando tem a notação 'raw' na keyword, como por exemplo virtualRawData etc.. normalmente é referente a componentes físicos como o disco rígido, dispositivos I/O etc.

normalmente o Entry Point que fica no cabeçalho opcional está apontando para o inicio da seção de código(.text)

malwares podem esconder código ou até mesmo um  PE completo, na seção resource (.rsc)