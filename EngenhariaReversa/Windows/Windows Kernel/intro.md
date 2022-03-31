O Kernel do Windows
=====================



**arquivo referente ao kernel** :

		ntoskrl.exe

- O kernel Possue 2 componentes principais : Windows Executive e Windows Kernel


Windows Executive
------------------


- Implementa funções exportadas pela ntdll.dll ( system service )
- As funções exportadas para ntdll.dll ficam na memória em uma TABELA memória chamada SSDT :

		A System Dispatch Table (SSDT) = tabela de exports pra NTDLL.dll

- Os dados da SSDT que são exportados seguem um padrão:
		
		código da função = 0x25
		nome da função = NtWriteFile
		endereço da função = 0x77f7fa 

- Os rootkits normalmente alteram essa tabela.

- Composto por subcomponentes : gerenciador de I/O, energia etc.. esses componentes podem ser alcançados:

1. Indiretamente : pela Win32 API

2. Diretamente : por interfaces da Native API ( Rtl , Mm , Ps)

- Windows executive é utilizado pelos Devices Drivers para interface com o user-mode.
- Também exporta funções que somente os drivers podem usar.


Windows Kernel
----------------


- É de fato o Próprio Kernel do Windows.
- Responsável pela gestão de recursos do SO e a distribuição de Threads para a utilização desses recursos
- Faz a Interface com o hardware através da HAL
- Exporta funções para outros programas do Kernel ( Ke ) documentadas no 


#### Devices Drivers


- Função principal : Interface com o dispositivo de Hardware ( HAL )
- EX : Driver do teclado, o HAL lê e interpreta e traduz para o SO na forma de uma estrutura de dados.
- Normalmente são escritos em C ou Assembly. ( .sys ou .ocx )

- Não lidam apenas com o Harware, também interagem com componentes do Kernel.
- O Windows tem diversos drivers que não relacionam diretamente com o HAL.
- Um Driver não precisa necessáriamente ter um Hardware referente, pois pode ser usado para operações dentro do Kernel.
- Device drivers tem a capacidade de conversar com o Hardware e utilizar funções do kernel ou do Windows Executive.

- Ficam "ao lado" do Kernel e do Hardware, e não possui dependencias deles. 
( Não tá dentro do kernel, nem do harware.. mais sim no meio termo)

- Podem optar por usar o Executive ou implementar suas rotinas e exporta-las para o user-mode.
- Lado bom : Windows é bem flexível e plugável rs
- Lado ruim : Drivers defeituosos ou maliciosos



#### Windows Hardware Abstration Layer ( HAL )


- O Kernel também se preocupa com performace e portabilidade.
- A HAL lida com funções que otimizam o uso do Hardware. Como Cache e Ambiente de múltiplos processadores.
- A HAL cuida do código p/ lidar com diferentes arquiteturas.
- A 'hal.dll' é importada pelo Kernel no momento da inicialização do sistema. ( de acordo com a arquitetura do PC )
- Basicamente a HAL faz uma validação antes da inicialização do sistema, para saber de que arquitetura de trata.. para depois deixar tudo arrumado para o kernel se virar após a inicialização do sistema.
- Rootkits lidam pouco com a HAL, pois é muito trabalhoso.



### Kernel Driver no Windows


- Permitem aos desenvolvedores rodar código no kernel.
- São difíceis de análisar pois ficam carregados na memória.
- Aplicações não interagem diretamente com os Drivers. Para ocorrer essa interação foi criado pelo Windows o 'Device Object'.
- Os 'Devices Objects' enviam pedidos para os dispositivos do Kernel (seja físico(hardware) ou componente interno do kernel).
- Dispositivos não são somente físicos.
- Os Drivers criam e destroem os 'Devices Objects'

- Os Drivers devem ser carregados no kernel
- Quando é carregado pelo SO é chamado de cara a função DriveEntry ( semelhante a dll entry point que vimos )
- Nesse momento é criada a tabela com todas as  funções Exportadas pelo Driver ( callback Functions )
- Callback Functions são chamadas pelas apps user-mode.

- 


#### Passos para a criação de Callback Functions:

1. O Windows cria uma estrutura **driver object** e passa para DriverEntry
2. DriverEntry preenche essa estrutura com CallBack Functions.
3. DriverEntry cria um 'device object'
4. Aplicativo user-mode enviar requisições para o 'device object'.


#### Devices Objects

- Componentes que o Driver cria para fazer interface com o User-mode.
- Esses componentes são a ponte entre o Driver x User-mode
- Analogia :

		PEN Drive 8GB ( HARDWARE ) >  USB Flash ( DRIVER ) > D:\ ( DEVICE OBJECT ) > USER-LAND ( aplicação ) 


#### Exemplo de Drivers no Windows

- Aplicação user-mode solicitando leitura de dados em um dispositivo de hardware :

1. Aplicação obtem um handle para um 'Device Object'
2. A aplicação chama a ReadFile no HANDLE informado acima.
3. Kernel processa o pedido e busca ReadFile nas funções de callback do driver.
4. Driver realiza a operação de leitura ( I/O )


- Chamadas de user-mode diretamente p/ kernel-mode são difíceis de rastrear.
- Envolve muito código do SO, para suportar a chamada.



### Os rootkits em modo kernel

- técnica mais utilizada : SSDT ( System Service Descriptor Table ) Hooking.

- SSDT utiliza para buscar chamadas de função no kernel.

- Normalmente a SSDT não é acessada por aplicativos de terceirs.

- **lembrete** : código do kernel só é acessivel para apps user-mode através das instruções SYSCALL e SYSENTER ou o INT 0x2e.

- A transição de user-mode p/ Kernel-MODE é feito na NTDLL.DLL

- versões mais modernas do Windows utilizam a SYSENTER. Exemplo da chamada da NtCreateFile :

		
ntdll.dll

		
		mov eax , 0x25
		mov edx, 0x7ff0300
		call dword ptr [edx]
		return 0x2c

---

CHAVEAMENTO p/ kernel-mode


		mov edx, esp
		sysenter

----


SSDT


		NtCreateDirectoryObject
		NtCreateEvent
		NtCreateEventPair
		NtCreateFile
		NtCreateIoCompletion
		NtCreateJobObject


- Nesse caso o kernel sabe qual função deve chamar, de acordo com o valor passado para EAX antes da chamada da SYSENTER.
- Esse valor passado pra EAX, é referente ao código da funçao em si na tabela SSDT do kernel. 
- Então o Kernel vê qual código foi passado pra EAX, e daí consegue pegar o código referente na sua SSDT.




#### Os rootkits em Kernel Mode

- o rootkit 'hooka' uma das funções da SSDT.
- a SSDT é alterada pelo endereço da função maliciosa.
- No exemplo o off 0x25 ( symbol referente a esse numero hexa ), teria seu ENDEREÇO ALTERADO. Faz total sentido pois vemos que na SSDT tem : código da função (0x25), nome da função (NtCreateFile - nao alterado) e o endereço que no caso foi mudado.


- O endereço levaria uma função para dentro do driver malicioso.
- A ação malicioso geralmente chama a função original e depois remove dos resultados, todos arquivos pertencentes ao rootkit.
- 




### Dicas

HAL - O componente de mais baixo nível que integra o sistema operacional MS-windows.
( Hardware Abstraction Layer )

- Funções que começam com o prefixo 'Ke', são funções que o próprio Windows Kernel exporta.


lm m nt

lm - lista os drivers carregados no kernel


RtlInitUnicodeString - Copia strings para um lugar da memória do kernel, para que sejam utilizadas depois.

MmGetSystemRoutineAddress - equivalente a ProcAddressA() da user32. ( Obtem um nome de uma função e obtem o endereço dela )