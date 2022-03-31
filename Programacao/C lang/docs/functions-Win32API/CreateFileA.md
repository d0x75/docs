CreateFileA
------------

Função usada para criar arquivos.


**Protótipo** :


		HANDLE CreateFileA(
		  LPCSTR                lpFileName,
		  DWORD                 dwDesiredAccess,
		  DWORD                 dwShareMode,
		  LPSECURITY_ATTRIBUTES lpSecurityAttributes,
		  DWORD                 dwCreationDisposition,
		  DWORD                 dwFlagsAndAttributes,
		  HANDLE                hTemplateFile
		);



- Exemplo em C :


		int main()
			{
				HANDLE h = CreateFile(
				"C:\\err.txt",
				GENERIC_READ | GENERIC_WRITE,
				0,
				NULL,
				CREATE_NEW,
				FILE_ATTRIBUTE_TEMPORARY,
				NULL);

			}