Reversing - Termos e Conveções
-------------------------------


**Windows APIs** :

- Funções dispobilizadas pelo SO para as aplicações se comunicarem com o SO.
- Window tem 2 tipos de APIs :
	
1.  Win32 API - user mode
2.  Native API - kernel mode

- Win32 API validam os argumentos e passa para a Native API.
- Native API chama funções internas do kernel.
- Native API possui pouca documentação.


---


**Threads** :

- São fluxos de execução do programa, separados em paralelos. ( um programa pode ter várias threads ) . Cada Thread é responsável por sua tarefa dentro de um mesmo processo.


---


**Tls Callbacks** : 

- Técnica utilizada para execução de código antes do programa chegar no EP - Entry Point

- Trata-se de uma técnica legítima do Windows utilizada para lidar com várias threads. Quando vemos um Software que usa essa funcionalidade de TLS normalmente vai ter também uma seção do EXE que se chama : .tls

- Lembrando que quando o software tem essa funcionalidade de TLS, é possível que código seje executado antes do EntryPoint. Geralmente o código da TLs vai estar na .tls.


---


**Exceptions** :


- Também podem ser usadas para detectar um debugger.
- Gera uma Exception e verifica se foi interceptada pelo debugger(que é o comportamento padrão)
- O debugger não passa diretamente para o processo manipular a Exception.
- Marque no OllyDbg, para passar por todas as Exceptions e não desviar :

		Options > Debugging options > Exceptions


---


**Offset** : endereço de memória das instruções do programa na CPU.

- A menor unidade de medida da computação é o Bit, mais temos outras nomeclaturas conforme o Bit(1 unidade) vai aumentando de tamanho. São elas:

		Nibble : 4 bits
		BYTE   : 8 bits
		WORD   : 2 bytes
		DWORD  : 4 bytes
		QWORD  : 8 bytes

#### Code Cave

- Espaço vazio em alguma seção do executável.

#### CrLf

- Quando falamos de Strings no geral, um dos bytes importante é o '0x0a', conhecido também por '\n', line feed (Lf) ou simplesmente "caractere de nova linha".

- O MS-DOS e o Windows utilizam na verdade dois caracteres para delimitar uma nova linha. Antes do '0x0a', temos um '0x0d', conhecido também por '\r', Carriage Return ou Cr. 

- Daí a origem dessa dupla, que também conhecida por **CrLf**.

		CrLf - Carriage Return and Line Feed

		Cr - Carriage return ( 0x0d )
		Lf - Line feed ( 0x0a )



#### String C

- String que terminam com byte nulo.

#### String UNICODE

- Strings com 2 bytes de largura.


Termos utilizados em intel x86
-------------------------------

### Official Operands

	rel8
	rel16, rel32
	ptr16:16, ptr16:32
	r8
	r16
	r32
	imm8
	imm16
	imm32
	r/m8
	r/m16
	r/m32
	m
	m8
	m16
	m32
	m64
	m16:16, m16:32
	m16&32, m16&16, m32&32
	moffs8, moffs16, moffs32
	Sreg
	m32real, m64real, m80real
	m16int, m32int, m64int
	ST or ST(0)
	ST(i)
	mm
	mm/m32
	mm/m64


### Generalized Operands



<reg32> Qualquer registro de 32 bits ( EAX , EBX , ECX , EDX , ESI , EDI , ESP ou EBP )
<reg16>	Qualquer registro de 16 bits ( AX , BX , CX ou DX )
<reg8>	Qualquer registro de 8 bits ( AH , BH , CH , DH , AL , BL , CL ou DL )
<reg>	Qualquer registro
<mem>	Um endereço de memória (por exemplo, [eax] , [var + 4] ou dword ptr [eax + ebx] )
<con32>	Qualquer constante de 32 bits
<con16>	Qualquer constante de 16 bits
<con8>	Qualquer constante de 8 bits
<con>	Qualquer constante de 8, 16 ou 32 bits


Termos/Conceitos utilizados pela Microsoft
--------------------------------------------


- A Microsoft usa algumas convenções de nomes que precisam ser detalhadas, para o melhor entendimento dos protótipos das funções da API do Windows, abaixo as nomeclaturas usadas normalmente :


WINAPI : Define que a convenção de chamada da função é a '__ stdcall'

_In_ : Define que o parâmetro é de entrada

_Out_ : Define que o parâmetro é de saída (a função vai escrever nele)

_opt_ : O parâmetro é opcional (pode ser NULL)

HANDLE : Um número identificador de um objeto no ambiente Windows. Um handle é um número quidentifica um objeto (arquivo, chave de registro, diretório, etc) 		aberto usado por uprocesso

HWND : Um handle (identificador) da janela

LPCTSTR : Long Pointer to a Const TCHAR STRing

UINT : unsigned int ou DWORD (32-bits)