Comandos do Windbg
------------------


- Pesquisar uma função:

		x ntdll!NtCreateFile

- Limpar o terminal do Windbg

		.cls

- Fazer um disassembly

		uf ntdll!NtCreateFile

- Fazer um disassembly apontando para um endereço de memória.

		uf poi (0x7ffe0300)



Windbg Tricks
----------------


**Ativar o modo VERBOSE** (recomendado sempre deixar ativo):

- View > Verbose output ou 'CRTL + ALT + V'

---
lm
- Existe formas de setar um breakpoint genérico no Windows, para que ele pare sem travar o OS inteiro.

		CTRL + BREAK


----


- Continuar a execução depois de ter feito o breakpoint, é o comando GO :

		kd> g


----


- Listar todos os módulos/drivers carregados no Kernel :

		kd> lm


----


- Procurar o endereço de funções do módulo do kernel(ntoskrnl, usando o prefixo 'nt!' ) :

		kd> x nt!*CreateProcess*


---


- Setar break point no endereço de uma função do kernel, depois de ter localizado seu address.

		kd> bp nt!NtCreateProcessEx



- Listar todos os breakpoint setados no kernel


		kd> bl


- Mostrar o valor de todos os registradores

		kd> r


- Mostrar o valor de registradores específicos

		kd> r eax,ebx

		kd> r esp, eax 


- Limpar Todos os breakpoints do kernel

		kd> bc *


- Setar um break point em uma função do kernel, exibir os registradores esp e ebp no momento da interception e continuar a execução.

		bp nt!NtWriteFile "r esp,ebp; g"


- Vizualizar os memory address da SSDT

		dd poi (KeServiceDescriptorTable)


- Vizualizar os memory address da SSDT, mais de forma amigável.. aparece a função referente ao address

		dds poi (KeServiceDescriptorTable)


- Vizualizar 200 linhas da SSDT

		dds poi (KeServiceDescriptorTable) L200


### Dicas


arquivo boot.ini = gerenciador de boot do windows ( igual o GRUB do linux )


http://windbg.info/doc/1-common-cmds.html

extensão .sys = driver de kernel windows
