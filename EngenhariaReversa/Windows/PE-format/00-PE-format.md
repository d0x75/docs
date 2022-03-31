PE Format 	
----------


A sigla PE, vem de "Portable Executable" e é Derivado do Common Object File Format - COFF. A Microsoft criou um padrão para estruturar os binários do SO, que tornou-se capaz de fazer um binário rodar em qualquer versão do Windows.

O formato PE, tem uma estrutura de dados que encapsula informações necessárias para que o Loader do SO consiga identificar que se trata de um binário do Windows na hora de  carregar-lo. Então esse é o formato "padrão" de como deve ser composto um binário do Windows. ( tipos de binários do windows : .EXE,.DLL,.COM,.OCX,.CPL,.NET, kernel drives(.sys) )

				-------------------------
				|Cabeçalho MZ do DOS    |
				-------------------------
				|Fragmento (stub) do DOS|
				-------------------------	
				|PE COFF - PE Header    |
				-------------------------
				|Optional Header        |   
				-------------------------
				|Data Directory         |
				-------------------------
				|Cabeçalho das Seções   |
				-------------------------
				|Section Table          |
				-------------------------	
				|Section 1              |
				-------------------------
				|Section 2 ...          |
				-------------------------
				|Overlay                | 
				-------------------------


## Features

- Um arquivo PE consiste em vários cabeçalhos e seções que informam ao linkeditor como mapear o binário em memória.

- Uma Imagem do Executável, consiste em várias regiões diferentes; cada uma das quais requer proteção de memória diferentes; portanto o início de cada uma dessas seções do binário PE deve estar alinhada com o limite de uma página. Uma das partes do Linker é mapear cada seção para a memória individualmente e atribuir permissões corretas as regiões resultantes, de acordo com o que está informado nos cabeçalhos.

- Os arquivos PE na maioria das vezes são armazenados na memória da mesma forma que eles ficam em disco, mantendo a
estrutura do arquivo praticamente idêntica nos dois casos.

- Há um endereço em que o binário normalmente é carregado por convenção ( ImageBase ). Mais não significa que é obrigatório, uma vez que o PE
pode ser carregado qualquer lugar no espaço de memória do processo do binário.

---

### Offset ( deslocamento )

- Offset do arquivo é na verdade um local dentro daquele arquivo específico.
- Vamos ver sendo usados a partir do ponto de partida do inicio de um arquivo ou de um endereço de memória.

### Módulo

- É a versão do arquivo PE na/em memória. Todo código, dados e recursos do PE na memória.
- Quando o binário é executado ele se torna um módulo na memória.
- o binário é considerado um "executável" no disco. Porém quando entra na memória, passa a ser considerado um Modulo da Memória.

### Processo

- Espaço em memória isolado, que pode ser utilizado para executar um module.

### VA ( virtual adress )

- local onde o PE foi carregado, o primeiro byte do PE inicia aqui.
- endereço de memória aonde o PE foi carregado.
- Pode ser chamado de HModule ( HMODULE - Endereço de Memória aonde o PE foi carregado ).

### RVA ( relative virtual address )

- Endereço em memória relativo ao VA.
- Endereço em memória que é acessado indiretamente pelo VA.
- **RVA = VA – ImageBase**

