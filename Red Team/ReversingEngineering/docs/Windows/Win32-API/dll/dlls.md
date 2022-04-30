DLLs - Dinamic Link Librarys
=============================


- Antes do Windows 2000, as DLLS eram carregadas em um local público que podia ser acessado por qualquer programa. Logo se um programa fosse corrompido iria afetar os demais, devido estarem utilizarem as DLLs de uma forma compartilhada.

- Apatir o Windows 2000, as DLLS começaram a ser carregadas em um local restrito de memória, e ela poderia ser utilizada exclusivamente pelo programa que a carregou. De forma clara: Cada programa possui sua kernel32.dll, user32.dll etc..


- DLLs são uma forma de compartilhamento de código entre aplicações.
- É Um binário PE porém não executa sozinho,normalmente é um PE executável (.exe) quem chama a DLL.
- Exporta funções para outras aplicações.
- Memória compartilhada entre processos, a dll entra no mesmo processo do executável que a chamou.
- Não precisa distribuir DLLs do SO com o EXE.
- Execução dentro de um processo (processo host).
- Atrativo p/ malware, ocultar ações, dificuldade de análise.
- Ter acesso a memória do processo.
- Vários programas conseguem acessar a mesma DLL devido ela estar apenas em 1 local da memória, então esse local de memória fica compartilhado entre processos e quando os programas precisam acessar a DLL, vão até o mesmo local de memória. Isso ocorre pq se cada vez que um programa chamar uma DLL, ter que criar um novo processo pra DLL.. não há memória que aguente.



### Estrutura básica de uma dll

- Internamente são igual aos .EXE
- IMAGE_FILE_HEADER - Characteristics - flag in DLL
- Normalmente possuem mais Exports que os .EXE
- Também é normal haver Imports, devido uma DLL chamar funções outras DLLs.
- DllEntryPoint não é um Export. ( DllEntryPoint , é o "main" da DLL )
- DllEntryPoint é executado automaticamente quando um DLL é carregada.



#### Exports

- podem ter nomes significativos ou não
- enumerar com CFF Explorer ou IDA Pro.


### Executando uma dll

- Requer um processo HOST sendo executado, pra daí sim a dll ser executada.
- Processo host GENÉRICO pro Windows = rundll32.exe
- Via cmd usamos o comando:

		rundll32.exe <path>,<export> [arguments(opcional)]

#### Funcionamento do run32dll.exe :

1. Chama a função 'GetComandLineW' para verificar parâmetros passado pra rundll32.exe .
2. Carrega a DLL passada como argumento com a 'LoadLibraryW' e executa o DLlEntryPoint.
3. Obtém os endereços dos Exports com a 'GetProcAddress'.
4. Chama a função Export, fornecendo os argumentos opcionais.



### Restrição de Processo Host

- algumas dlls apenas se executam em processos específicos.


### Evitando Restrições de Processo Host

- Renomear o rundll32.exe para o nome esperado.
- Injetar a dll no processo desejado.
- RemoteDLL ( usado para injetar dlls , ambiente gráfico )
- Use o Python! ( Livro Gray Hat Python e muito mais )
- Após a Injeção da DLL que o malware executa, analisamos o comportamento de forma dinâmica.



### Debuggin DLL

- LOADDLL.exe , é o processo HOST do OllyDbg e do ImmunityDbg.
- Quando uma DLL é aberta pelo Olly ou Immunity, ja é direcionado automaticamente para o LOADDLL
- O LOADDLL.exe tem o funcionamento parecido com a rundll32.exe
- Funcionamento pareceido com o do rundll32.exe
- Quando aberta no Debugger é setado um breakpoint automaticamente no DllEntryPoint


## COM - Component Object Model


- Método criado pela Microsoft, para possibiliar comunicação entre aplicações do Windows.
- Utilzar códigos(interfaces) de outros programas, se conectando neles através do COM.
- Não executa o processo de outro programa.
- Determinar se o Malware utilizar COM
- COM client , COM server
- Microsoft oferece muitos objetos COM para serem utilizados.



### COM Server Malware

- COM server malicioso para outras aplicações utilizarem ( DLL )
- BHO ( Browser Help Objetcts ) - plug ins para o IE
- Não possuem restrições
- Permite executar e manipular código dentro do IE
- Monitorar tráfego, rastrear uso, se comunicar com a Internet.

- Para verificar os BHO's que estão no internet explorer, bastar ir na seguinte chave do registro:

		HKLM\SOFTWARE\Microsoft\Windowa\CurrentVersion\Explorer\Browser Helper Objects

- Para detectar um BHO fácilmente temos algumas funções que ficam na Exports que nos revela isso :


		DllCanUnloadNow
		DllGetClassObject
		DllInstall
		DllRegisterServer
		DllUnregisterServer





### Dicas


LoadLibraryW(); = função que só de olharmos já sabemos que está carregando uma dll na memória.


Para saber se o malware utiliza COM, verificar se há a presença dos Imports: 


		OleInitialize

		ColInitialize

Esses imports acima são as funçoes que inicia a comunicação via COM.

- Executar um Malware .cpl :

		rundll32.exe shel32.dll,controlrun.dll