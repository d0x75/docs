Coff Header ( PE Header )
===========================



#### PE Signature :  


		0x50 0x45 0x00 0x00 ou ("PE\0\0")

- Magic number que marca o inicio do Cabeçalho PE.


#### IMAGE_FILE_HEADER :

Machine = Qual a arquitetura do processador em que o binário PE foi compilado. ( WORD - 2bytes ) Ex:
	
		0x01 0x4c = Intel 386

NumberOfSections = Numero de sessões que o executável tem.
TimeDateStamp = Data e hora da compilação do executável.
PointerToSymbolTable = 
NumberOfSymbols =
SizeOfOptionalHeader = Tamanho da próxima sessão, que é o cabeçalho opcional.
Characteristics = Várias informações do arquivo ( se é um executavel/dll , se é x86 ou x86-64 etc.. s)


#### IMAGE_OPTIONAL_HEADER :

Magic = WORD
MajorLinkerVersion = byte
MinorLinkerVersion = byte
SizeOfCode = DWORD
SizeOfInitializedData = DWORD

AddressOfEntryPoint = DWORD

- RVA para a primeira instrução. Packers alteram para a função de unpacking depois reotornam para:

		OEP - Original Entry Point

- Conhecido como EP ou OEP. 
- Endereço da primeira instrução executada pelo programa.

BaseOfCode = DWORD
BaseOfData = DWORD

ImageBase = DWORD

- VA
- Local da memória aonde o binário PE quer ser carregado.

SectionAligment = DWORD
FileAligment = DWORD
MajorOperatingSystemVersion = WORD
MinorOperatingSystemVersion = WORD
MajorImageVersion = WORD
MinorImageVersion = WORD
MajorSubsystemVersion = WORD
MinorSubsystemVersion = WORD
Win32VersionValue = DWORD
SizeOfImage = DWORD
SizeOfHeaders = DWORD
Checksum = DWORD
Subsystem = WORD
DllCharacteristics = WORD
SizeOfStackReserve = DWORD
SizeOfHeapReserve = DWORD
SizeOfHeapCommit = DWORD
LoaderFlags = DWORD
NumberOfRvaAndSizes = DWORD

DataDirectory = IMAGE_DATA_DIRECTORY

- Uma estrutura de diretórios que fica dentro do executável.
- Array com 16 estruturas predefininas importantes para o PE ( IMAGE_DATA_DIRECTORY )

#### IMAGE_DATA_DIRECTORY :

Export Table :
Import Table :
Resource :
Exception :
Security :
Relocation :
Debug :
Copyright :
Globalptr :
TlsTables :
LoadConfig :
BoundImport :
IAT :
DelayImport :
COM :