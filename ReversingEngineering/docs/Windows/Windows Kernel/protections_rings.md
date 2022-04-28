Protection Rings
------------------


Níveis de privilégio dos processadores.

- privilégios de execução de código, não é só no Windows mais em qualquer SO.
- separa os códigos ( user X SO )


		SO = ring 0 - kernel land
		USER = ring 3 - user land

- cada aplicação do usuário tem um espaço de memória isolado pra ela no USER LAND.


### Transição de user-mode p/ kernel-mode

- Quando a execução é mudada de Ring 3 p/ Ring 0, isso se da quando uma aplicação de user-mode requisita de algum recurso que só o kernel-mode tem privilegio p/ executar.

- Instruções utilizadas para essa transição:
		
		SYSENTER
		SYSCALL
		INT 0x2e (interrupção INT 2E)

- De certa forma isso ocorre a todo momento, exemplo : Ao salvar um arquivo texto, temos que escrever no disco rígido, então a aplicação necessita de acessar o hardware ; então o controle é transferido para o driver (ring 0) e retorna.

### Kernel mode

- Código do próprio sistema operacional ( e de Drivers também )
- User apps, passam parte do tempo em kernel mode
- Ambiente extremamente volátil ( tá mudando toda hora, e é bem sensível )
- Todo código que roda no Kernel, tem os MESMOS privilégios de acesso.
- Endereços de Memória não são separados igual no user-land que cada processo é separado.
- Programas podem acessar a memória dos outros.
- Ambiente complicado, porém LIVRE ( faz o que quer)
- Não há validações e controles de erros.
- Se houver uma vírgula errada no kernel = TELA AZUL

- Se um malware roda em Kernel Mode, ele consegue alterar programas de segurança.
- Auditorias de SO, não se aplicam ao kernel-mode.
- Rootkits rodam em kernel-mode
- Desenvolver nesse ambiente é mais complicado.



### User mode

- Aplicações no nível de privilegio do usuário.
- Cadas processo tem sua própria memória, recursos e permissão.
- Não pode manipular o Hardware diretamente.
- Código user só pode manipular o kernel com interfaces.
