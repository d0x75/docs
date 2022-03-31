PEB - Process Evironment Block  
===============================



- É uma estrutra de dados que há nos processos do Windows, que na real são vários campos que são considerados FLAGS e cada uma das flags tem sua respectiva funcionalidade.

- Estrutura mantida pelo SO para cada processo em execução.
- Contém parâmetros e informações de user-mode para os processos.
- Incluem : variáveis de ambiente, lista de módulos carregados, endereços de memória e status do debugger.


- Estrutura PEB:


						typedef struct _ PEB {
							BYTE Reserved1[2];
							BYTE BeingDebugged;
							BYTE Reserved2[1];
							PVOID Reserved3[2];
							PPEB_LDR_DATA Ldr;
							PRTL_USER_PROCESS_PARAMETERS ProcessParameters;
							BYTE Reserved4[104];
							PVOID Reserved5[52];
							PPS_POST_PROCESS_INIT_ROUTINE PostProcessInitRoutine;
							BYTE Reserved6[128];
							PVOID Reserved7[1];
							ULONG SessionId;
						} PEB , *PPEB*;


- Cada campo da estrutura acima é uma FLAG.


- As funções da API do Windows verificam as flags da PEB.
- Instrução que acessa a PEB :

			fs local:[0x30h]