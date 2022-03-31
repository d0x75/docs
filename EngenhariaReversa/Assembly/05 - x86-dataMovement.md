##### Data Movement ( copiando dados )

As instruções operam com valores que são trazidos por registradores ou pela memória RAM. A instrução mais comum para copiar dados entre ambos é a instrução : **MOV ( de mover )**

Agora será mostrado várias formas de mover de dados, que nos deparamos na *reversing* :

- **copia um registrador ou dados imediatos para um registrador.**

``
MOV EDI, ESI
MOV EAX, 0xc0ffe
``

- **copia dados da memória pra um registrador ou de um registrador para um offset de memória.**

``
MOV EBX, [EAX]
MOV [0x401012], ECX
``

- **copia dados, acessando a memória por meio de um registrador base + offset de memória.**

``
MOV EAX,[EBP+8]
MOV [EAX+12], ECX
``

- **copia dados com níveis de granularidade diferentes. ( granularidades = BYTE , WORD , DWORD )**

``
MOV DWORD PTR EAX, [0X410032]
MOV WORD PTR AX, [0xfff930]
MOV BYTE PTR AH, [0xfff930]
``

- **copia dados, acessando a memória para interação com objetos do tipo Array, por meio  de: :
Base address + Index * Scale**

		base address = endereço base de um array global , por exemplo.
		index  = índice de cada elemento do array referente ao base address
		scale = tamanho de cada índice do array ( * 4 = WORD )**

``
MOV EAX, [EBP+ 0xc0ffe * 4]
``

- **copia dados de granularidades diferentes para a memória de forma implícita, por meio dos registradores EDI / ESI. ( destino / origem )**

``
MOVSB
MOVSW
MOVSD
``