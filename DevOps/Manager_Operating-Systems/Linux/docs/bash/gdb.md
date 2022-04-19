#### gdb - peda (debugger de binarios Linux(ELF))


- abrir um binário usando o debugger Gdb

		gdb ./program

- criar arquivo para setar o disassembly do GDB con o padrão INTEL pois o nativo é padrão AT&T

	 		vim ~/.gdb_init
	 		set disassembly-flavor intel
- Após criar o arquivo gdb_init, executamos o seguinte comando para que fique mais limpa a tela do GDB ao abrir-lo :
		
		alias gdb='gdb -q'


- Fazer o Disassembly da Função main, após ter abrido um binário com o gdb:

		disass main

- Colocar breakpoint em funções ou endereços:

		break main

		break 0x84908

		break *0x84908+16

- Para rodar o binário que esta sendo debugado

		run

- Para verificar o valor de todos os registradores, ou de alguns específicos.. exemplos:

		i r (mostra os valores todos os registradores em tempo real)

		i r eax ebx ecx (mostra os valores dos registradores especificados em tempo real)