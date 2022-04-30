IsDebuggerPresent
------------------

Função usada para detectar se o programa está rodando em contexto de debug.

- A função mais simples e conhecida. Provida da kernel32.dll

- Checa o campo IsDebugged na estrutura Process Evironment Block ( PEB )
- Se o retorno == 0 ( não há debugger )
- Se o retorno != 0 ( há debugger )


**Protótipo** :


	BOOL IsDebuggerPresent();



- Exemplo em C:



		if(!IsDebuggerPresent()){
			MessageBoxA(
				NULL,
				"Malware rodando",
				"MALICIUS SOFTWARE",
				0
				);
		}