Stack Operations and Function Invocation
------------------------------------------

É na memória RAM que armazena recursos de funções “functions” dos programas.. como variáveis locais e parâmetros , das mesmas. 
( os endereços da stack crescem de cima para baixo ).

Instruções/Registradores assembly que lidam com a pilha:

- **PUSH** = empilha 
- **POP** = desempilha 
- **POPAD** = desempilha todos registradores da memória. 
- **PUSHA** = empilha 16 bits de cada registrador na memória 
- **POPA** = desempilha 16 bits de cada registrador na memória 
- **CALL** = chamada de função LEAVE = saída
- **ESP** = Contém o endereço de memória que aponta pro topo da pilha. ( stack pointer )
- **EBP** = Por convenção aponta pra base da pilha ( base pointer )

*Nota* :

``
PUSHA coloca na pilha registradores 16-bit na seguinte ordem: AX, CX, DX, BX, SP, BP, SI e DI.
PUSHAD coloca na pilha registradores 32-bit na seguinte ordem: EAX, ECX, EDX, EBX, ESP, EBP, ESI e EDI.
``

---

### Calls

- Utilizamos o mnemônico CALL para IDENTIFICAR uma chamada função do programa.
- A execução do programa é transferida para a função.
- Existem padrões de chamadas de funções que variam de compilador p/ compilador.
- Padrão mais comum : **__cdecl** ou **__stdcall**

##### Prólogo

Está logo no inicio da função , usada para preparar a pilha para o uso da função


		PUSH EBP
		MOV EBP, ESP
		SUB ESP, 0x40


##### Epílogo

É no final da função; vai restaura a pilha e os registradores para o estado anterior da chamada da função. Usamos esse padrão para desfazer a pilha :


		MOV ESP, EBP 
		POP EBP
		RET


##### Stack Frame

É o espaço da pilha reservado para cada função, então teoricamente para cada função que é executada via ( CALL ), é criada uma nova Stack Frame.

Essas pilhas são construídas e destruídas a todo momento no programa, na memória especificamente.


		MOV ESP, EBP
		POP EBP
		RET


##### "Sequencia de instruções" de uma chamada de função:]

1. PUSH nos argumentos da função. ( parâmetros )
2. CALL <endereço funcao>, daí o EIP já é colocado na pilha automaticamente e aponta para o início da função. ( Esse CALL aponta para o endereço da primeira linha da função)
3. Prólogo da função.
4. Função executa.
5. Epílogo da Função = LEAVE.
6. RET ( retira o endereço de retorno e coloca no EIP )
7. O programa continua a execução na linha após a chamada de função.

##### "Sequencia de instruções DETALHADAS" de uma chamada de função:

1. Argumentos são colocados na pilha usando instruções PUSH.
2. A função é chamada com “CALL <memory offset>”. Isso faz com o endereço da instrução atual (isto é, o conteúdo do registrador EIP) seja colocado na pilha. Esse endereço será usado para retornar ao código principalmente quando a função for finalizada. Quando a função se inicia, é atribuído ao EIP o endereço da memória (início da função).
3. Com o uso do prólogo da função (function prologue), espaço é alocado na pilha para variáveis locais e o EBP (base pointer) é colocado na pilha. Isso é feito para salvar o EBP para o código principal que chamou a função.
4. A função executa suas tarefas.
5. Através do uso do epílogo a pilha é restaurada. ESP é ajustado para liberar o espaço utilizado pelas variáveis locais e o EBP é restaurado, assim a o código que chamou a função pode referenciar suas variáveis corretamente. A instrução LEAVE pode ser utilizada como um epílogo porque ela atribui ao ESP o valor do EBP e retira o EBP da pilha.
6. A função retorna chamando a instrução RET. Ela retira o valor de retorno da pilha e coloca no EIP, dessa forma o programa continua sua execução do local original onde a função foi chamada.
7. A pilha é ajustada para remover os argumentos que foram enviados, a menos que eles sejam utilizados novamente mais tarde.

#### Dicas sobre stack

**Identificar valores de offset da stack** :

		[EBP-valor] =  variável local
		[EBP+valor] = parâmetro de função

O RETORNO DAS FUNÇÕES SÃO ARMAZENADOS EM EAX

**Mudanças de Endianness fora do padrão** *memory x raw*

A mudança de endianness é algo que o software/malware deve fazer durante a comunicação com a rede, isso devido aos dados de rede serem o big-endiann e programas x86 utilizarem little-endiann. Dessa forma, o endereço IP 127.0.0.1 será representado como 0x7F000001 em big-endiann (na rede) e 0x0100007F em little-endian (localmente na memória). Como um analista de malware você deve ser conhecedor desses formatos para ter certeza que não irá acidentalmente inverter a ordem dos bytes de importantes indicadores como um endereço IP.

**Algumas convenções ou ocorrências bastante vistas** :

É possível ler dados da pilha sem utilizar as instruções PUSH e POP. Por exemplo, a instrução :


		MOV EAX, SS:[ESP] 


Irá acessar diretamente o topo da pilha, pois já especificamos o **SS : Stack Segment**. Isso é idêntico a POP EAX, exceto que o registrador ESP não é impactado. A convenção utilizada depende do compilador e como ele está configurado.


PUSH EBP-> PRÓLOGO. Empurra pra pilha o base pointer.

		MOV EBP, ESP -> PRÓLOGO. Move o valor da base da pilha pro stack pointer. 
		SUB ESP, 0x08 -> RESERVA ESPAÇO NA PILHA PARA AS VARIÁVEIS LOCAIS DA FUNÇÃO.
		SUB ESP, 0xC = Esse SUB após o prólogo, é pra reservar espaço para as variáveis locais da função. 
		( caso não houver nenhuma variável local, não terá essa instrução)


