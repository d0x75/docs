# 0x00 - Introdução a Arquitetura de Computadores


Resumo e anotações da leitura do livro _Introdução a Arquitetura de Computadores_.



#### Capítulo 1 - Introdução

Pretenções desse capítulo :

- Definir o que é a Arquitetura de Computadores e sua relevância.
- Apresentar a Arquitetura Geral de um computador e suas principais operações.
- Diferencias sistemas digitais de analógicos.
- Apresentar o funcionamento de um transistor e sua relevância para a industria de dispositivos digitais.
- Destacar a Lei de Moore e seu impacto para a evolução da industria de dispositivos eletrônicos digitais.
- Identificar os principais fatos da evolução dos computadores.


---


Entender/Aprender Arquitetura de Computadores é tão importante para um profissional de TI, quanto Anatomia para
profissionais de medicina. Antes de iniciar qualquer coisa em medicina, o Médico precisa saber em detalhes o funcionamento/anatomia do corto humano. Façamos a mesma analogia para área de Informática.


- *Arquiteturas geral* :

Hoje em dia exitem várias arquiteturas de computadores diferentes, para vários destinos diferentes computadores. MAS todos os computadores compartilham de uma Arquitetura Comum entre eles.

1. Todo computador possui uma Unidade Central de Processamento ( CPU ) e uma memória principal ( memória RAM ).

2. Todos os dados que vão ser processados pela CPU em operações lógicas/aritiméticas, precisam estar na memória pricipal.

3. Da memória os dados são transferidos para a CPU, através de fios paralelos de comunicação chamados de 
'Barramento de Dados' (bus de dados)

4. Para a CPU saber o que fazer com os dados vindos do Barramento de Dados, ela precisa que as devidas instruções que também ficam armazenadas na memória sejam trazidas á ela através do 'Barramento de endereço'. Então cada instrução irá informar para a CPU o que ela deve fazer e com quais dados fazer.

5. A memória RAM é organizada por endereços, para que todos os dados e instruções sejam encontrados por esses endereços.

6. Esses endereços são enviados pela CPU para a memória principal através do 'Barramento de Endereços'; então a memória localiza quais são os dados contidos no endereço que ela recebeu, e devolve esses mesmos dados para a CPU via 
'Barramento de dados'

7. A CPU possue uma memória interna, por questões de melhoria de desempenho. chamada Memória CACHE. Todos os dados transferidos da memória pricipal para a CPU, também são salvos na memória Cache. Então dados recentes também ficam na Cache.

8. A CPU também é responsável por enviar sinais de controle á outros dispositivos do computador como periféricos, I/O devices e memórias externas.


---


- *Sistemas Analógicos x Sistemas Digitais*  : O computador é um dispositivo eletrônico digital. Isso significa que ele
armazena,processa e gera dados na forma digital. Por outro lado o computador não consegue usar dados Analógicos ;sem que
esses dados sejam convertidos para Digitais antes de processar-los.




---


*Transistores* :


O Transistor é um componente eletrônico criado em 1950 e que foi reponsável pela revolução da eletrônica em 1960. Toda
funcionalidade interna do computador é executada pela composição de milhões de transistores, desde operações lógicos e
aritiméticas até movimentar e gravar dados na memória ( a excessão de disco rígidos , CD ROMs, dvds E fitas magnéticas ).

O princípio básico dos transistores, foi de usar a a eletrônica ( corrente elétrica, resistência e tensão )para representar
dados e executar operações com esses dados. A forma mais simples que encontraram pra fazer isso é limitar os dados para apenas
dois tipos; no caso Zero e Um ; O sistema binário foi adotado para quebrar esse tabú. O motivo disso é o Transistor
possuir 2 estados. Ou ele está carregado , ou está descarregado .. assim como uma pilha por exemplo. Então isso pode ser
mapeado facilmente como 1(positivo) e 0(negativo).. O revolucionário disso é que foi possível que o estado do transistor
mudasse eletronicamente , e a qualquer momento de forma muito rápida. Assim com 8 transistores em paralelo, consigo formar um
número de 8 bits (1 byte). E posso mudar seu valor alterando suas cargas ou posso ler seus valores e ver qual possue carga e
qual não possue.

Quando menor o transistor , mais dados podem ser armazenados por área. Ao mesmo tempo os transistores guardam menas carga. Isso
torna mais rápido o processo de descarregamento das cargas e torna o processamento e armazenamento muito mais rápidos.

Com a revolução da nanoeletrônica , os transistores ficaram tão , mais tão pequenos que possibilitou a construção de memórias
de 1GB que físicamente são do tamanho de uma unha. ENTÃO UMA MEMÓRIA DE 1GB POSSUI PELO MENOS 8 BILHÕES DE TRANSISTORES.

Os processadores também se tornaram bem velozes com a miniaturização dos transistores. Os processadores atuais trabalham na
frequência de GHz (giga Hertz), ou seja, na casa de bilhões de ciclos por segundo.

Nome de u m transistor comum : "MOSFET" - Metal-Oxide Semiconductor Field-Effect Transistor

Quando o transistor está ativo, ele pode ser visto com o valor 1, e quando inativo, ele pode ser visto com o valor 0. Assim,
temos a menor memória possível de ser construída. Quando quisermos que ela guarde o valor 1, basta desligar a tensão da Porta
e aplicar uma corrente no Dreno. Já quando quisermos que ele armazene o valor 0, precisamos aplicar uma corrente na porta e
Fechar o canal. Então, uma memória de 8 bilhões de bits, pode ser elaborada com 8 bilhões de transistores como esses.

Então já podemos seguir a premissa que os Transistores são usados para a construção de memórias. Memórias feitas a base de
transistores são chamadas também de Memórias de Estado Sólido.


---


*Lei de Moore*


---


*A evolução dos computadores*


ENIAC : primeiro computador criado na história.. tinha cerca 4500 m2 , pesava 30 TONELADAS e consumia 140 KW.



STOPED : 1.8.2 A Arquitetura de von Neumann


