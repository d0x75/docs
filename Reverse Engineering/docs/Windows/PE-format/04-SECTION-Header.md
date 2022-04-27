Section Header
================



IMAGE_SECTION_HEADER
------------------------

Name1 - BYTE

- Esse campo é o nome da Seção. 
- Pode estar em branco.
- Não é obrigatório e também não precisa ser igual. ( Exemplos de convenções : .text, .code, .data, .rsc etc..)

PhysicalAddress - DWORD

VirtualSize - DWORD

- Tamanho dos dados da seção em memória.
- Fala pro Windows quanto de memória a seção vai usar.

VirtualAddress - DWORD

- RVA da seção.
- Endereço relativo ao inicio da seção.


SizeOfRawData - DWORD

- Tamanho que os dados da seção ocupam no arquivo em disco.

PointerToRawData - DWORD

- Offset onde se inicia a seção no arquivo em disco.

PointerToRelocations - DWORD
PointerToLineNumbers - DWORD
NumberOfRelocations - WORD
NumberOfLineNumbers - WORD
Characteristics - DWORD


- É importante lembrar que esses são os cabeçalhos das seções, não são as seções em si. São utilizados para acessar as seções.

- Array de estrutura com os headers das seções.
- Section table é conhecida como IMAGE_SECTION_HEADER
