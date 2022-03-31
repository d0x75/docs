Get-ExecutionPolicy / Set-ExecutionPolicy
-------------------------------------------


Restrição de execução de scripts .ps1

- Por padrão o powershell não permite a execução de scripts .ps1 dentro do terminal, mais há uma maneira de alterar isso. É seguinte:


- Verificar como está setado a permissão de execução de scripts no meu poweshell. 


		Get-ExecutionPolicy


- Alterar para outras permissões:

		Set-ExecutionPolicy Unrestricted
