DOS Header 
-----------

A seção "MZ DOS", do cabeçalho EXE compatível com MS-DOS 2,0 até a seção não utilizada logo antes do cabeçalho PE é a
seção do MS-DOS 2,0 e é usada apenas para compatibilidade com MS-DOS.	

O stub do MS-DOS é um aplicativo válido que é executado no MS-DOS. Ele é colocado na frente da imagem EXE. O vinculador
coloca um stub padrão aqui, que imprime a mensagem "este programa não pode ser executado no modo DOS" quando a imagem é
executada no MS-DOS. O usuário pode especificar um stub diferente usando a opção de vinculador/STUB.

No local 0x3C, o stub tem o deslocamento do arquivo para a assinatura do PE. Essas informações permitem que o Windows
execute corretamente o arquivo de imagem, embora tenha um stub do MS-DOS. Esse deslocamento de arquivo é colocado no local
0x3C durante a vinculação.

Após o stub do MS-DOS, no deslocamento do arquivo especificado em offset 0x3C, é uma assinatura de 4 bytes que identifica
o arquivo como um arquivo de imagem de formato PE. Essa assinatura é "PE \ 0 \ 0" (as letras "P" E "e" seguidas por dois
bytes nulos).

Falando de DOS, esse cabeçalho contém informações sobre os requisitos de memória e detalhes dos ajustes (realocações) que
precisam ser feitos quando o programa é carregado.

- DOS_magic = Magic Number, é a assinatura do arquivo PE. Os 2 primeitos bytes sempre vão ser :'MZ'

- O arquivo PE começa com o DOS Header, que sempre ocupa os primeiros 64bytes do arquivo.
- Abaixo a estrutura oficial do DOS Header:



            typedef struct _IMAGE_DOS_HEADER {
            WORD e_magic;
            WORD e_cblp;
            WORD e_cp;
            WORD e_crlc;
            WORD e_cparhdr;
            WORD e_minalloc;
            WORD e_maxalloc;
            WORD e_ss;
            WORD e_sp;
            WORD e_csum;
            WORD e_ip;
            WORD e_cs;
            WORD e_lfarlc;
            WORD e_ovno;
            WORD e_res[4];
            WORD e_oemid; 
            WORD e_oeminfo;
            WORD e_res2[10];
            LONG e_lfanew;} 
            IMAGE_DOS_HEADER,*PIMAGE_DOS_HEADER;


IMAGE_ DOS_ HEADER - Fields
----------------------------


##### e_magic

raw offset : 4D 5A

- É um valor de 2 bytes( WORD ) que identifica um executável válido, esse valor '4D 5A' in raw ou '5A 4D' in memory, é
representado em ASCII pela sigla "MZ" ( A sigla 'MZ' vem de : 'Mark Zbikowsky', que foi um dos idealizadores do MS-DOS ). Esse
magic number  um dos dados que o Windows Loader verifica quando vai carregar um programa. Caso ela não exista ou esteja
modificada, o Windows não reconhece o arquivo como um executável válido e não roda o programa.


##### e_cblp

raw offset : 50 00 / 90 00

- o número de bytes na última página do arquivo.

Especifica o número de bytes realmente usados na última página, com o caso especial de uma página inteira sendo
representada por um valor zero (já que a última página nunca está vazia). Por exemplo, supondo um tamanho de página de 512
bytes, esse valor seria 0 x 000 para um arquivo de 1024 bytes e 0 x 0001 para um arquivo de 1025 bytes (uma vez que contém
apenas um byte válido).


##### e_cp

raw offset : 00 03 / 00 02

Especifica o número de páginas necessárias para conter o arquivo. Por exemplo, se o arquivo contém 1024 bytes e presumimos
que o arquivo tem páginas de 512 bytes, essa palavra conterá 0x0002; se o arquivo contiver 1025 bytes, esta palavra
conterá 0x0003.


##### e_crlc

raw offset : 00 00

Especifica o número de itens de realocação, ou seja, o número de entradas que existem na tabela de ponteiro de realocação.
Se não houver entradas de realocação, esse valor será zero.


##### e_cparhdr

raw offset : 04 00

Especifica o tamanho do cabeçalho executável em termos de parágrafos (blocos de 16 bytes). 
Ele indica o deslocamento da imagem compilada / montada e linkada do programa (o módulo de carregamento) dentro do arquivo executável. 

O tamanho do módulo de carregamento pode ser deduzido subtraindo este valor (convertido em bytes) do tamanho geral do arquivo derivado
da combinação dos valores e_cp (número de páginas do arquivo) e e_cblp (número de bytes na última página). O cabeçalho
sempre abrange um número par de parágrafos.


##### e_minalloc

Especifica o número mínimo de parágrafos extras necessários para serem alocados para iniciar a execução. Isso é ALÉM da memória necessária para manter o módulo de carregamento. Este valor normalmente representa o tamanho total de quaisquer dados não inicializados e / ou segmentos de pilha vinculados ao final de um programa. Esse espaço não é incluído diretamente no módulo de carregamento, uma vez que não há valores de inicialização específicos e isso simplesmente desperdiçaria espaço em disco.

##### e_maxalloc

Especifica o número máximo de parágrafos extras necessários para serem alocados pelo programa antes de iniciar a execução. Isso indica memória ADICIONAL além da exigida pelo módulo de carregamento e o valor especificado por MINALLOC. Se a solicitação não puder ser atendida, o programa receberá a quantidade de memória disponível

##### e_ss

Especifica o valor SS inicial, que é o endereço do parágrafo do segmento da pilha em relação ao início do módulo de carregamento. No momento do carregamento, este valor é realocado adicionando o endereço do segmento inicial do programa a ele, e o valor resultante é colocado no registro SS antes do programa ser iniciado. No DOS, o segmento inicial do programa é o primeiro limite do segmento na memória após o PSP.

##### e_sp

Especifica o valor inicial de SP, que é o valor absoluto que deve ser carregado no registro SP antes que o programa receba o controle. Uma vez que o segmento real da pilha é determinado pelo carregador e este é apenas um valor dentro daquele segmento, ele não precisa ser realocado.

##### e_csum

Especifica a soma de verificação do conteúdo do arquivo executável. É usado para garantir a integridade dos dados no arquivo. Para obter detalhes completos sobre como essa soma de verificação é calculada, consulte http://www.tavi.co.uk/phobos/exeformat.html#checksum.

##### e_ip

Especifica o valor IP inicial, que é o valor absoluto que deve ser carregado no registro IP para transferir o controle para o programa. Como o segmento de código real é determinado pelo carregador e este é apenas um valor dentro desse segmento, ele não precisa ser realocado.

##### e_cs

Especifica o valor CS inicial pré-realocado, relativo ao início do módulo de carregamento, que deve ser colocado no registro CS para transferir o controle para o programa. No momento do carregamento, este valor é realocado adicionando-se o endereço do segmento inicial do programa, e o valor resultante é colocado no registro CS quando o controle é transferido.

##### e_lfarlc

- É um valor de 2 bytes ( WORD ) que armazena o offset( a posição ) onde está localizado o início do DOS-Stub. 

Especifica o endereço do arquivo da tabela de realocação ou, mais especificamente, o deslocamento do início do arquivo para a tabela de ponteiro de realocação. Este valor deve ser usado para localizar a tabela de ponteiros de realocação (em vez de assumir uma localização fixa) porque informações de comprimento variável pertencentes a sobreposições de programa podem ocorrer antes desta tabela, fazendo com que sua posição varie. Um valor de 0x40 neste campo geralmente indica um tipo diferente de arquivo executável, não um tipo DOS 'MZ'.


##### e_ovno

Especifica o número da sobreposição, que normalmente é definido como 0 x 000, porque poucos programas realmente têm sobreposições. Ele
muda apenas em arquivos que contêm programas que usam sobreposições. Consulte http://www.tavi.co.uk/phobos/exeformat.html#overlaynote para obter mais informações sobre sobreposições(overlays).

##### e_res

Especifica palavras reservadas para o programa (conhecidas em winnt.h como e_res [4]), geralmente definidas como zero pelo vinculador.
Nesse caso, apenas use um único reserved1 definido como zero; se não for zero, crie quatro(res[1],res[2],res[3],res[4]).

##### e_oemid

Especifica o identificador do OEM para e_oeminfo.

##### e_oeminfo

Especifica as informações do OEM para um valor específico de e_oeminfo.

##### e_res2

Especifica palavras reservadas para o programa (conhecidas em winnt.h como e_res [10]), geralmente definidas como zero pelo vinculador. Nesse caso, apenas use um único reserved1 definido como zero; se não for zero, crie dez com o valor correto.
(res2[1],res2[2],res2[3],res2[4],res2[5],res2[6],res2[7],res2[8],res[9]).)

##### e_lfanew

- É um valor de 4 bytes ( DWORD ) que fica em uma posição fixa  : offset 0x3C .
Essa DWORD que é sempre presente no offset "0x3c" tem o valor referente ao offset do início do PE Header/COFF Header ( assinatura PE )