Script que adiciona programas para ser executados na inicialização do sistema:
-------------------------------------------------------------------------------

- Abrir o regedit e seguir o seguinte caminho :


		HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run


- Ao lado direito clicar com o botão direito > Novo > Value String > Colocar o caminho do aplicativo que é pra ser iniciado junto com o windows. Exemplo : 

		"C:\\Windows\\System32\\notepad.exe"
