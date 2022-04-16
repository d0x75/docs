1. As chaves de registros na prática tem a mesma estrutura dos discos locais. Para verlas fazemos o seguinte no ps :

	get-psdrive

2. Acessar a HKEY_LOCAL_MACHINE , fazer o seguinte no PS :

	cd HKLM:\


3. Ir até o diretório e verificar oq tem salvo no diretório do registro do windows que apontarmos com o '-Path'. fazer o seguinte no PS :

	Set-Location -Path HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Run\
	dir

4. Verificar as chaves de registros e criadas dentro da pasta apontada pelo '-Path'. Fazer o seguinte pelo PS :

	Get-Item -Path HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Run\
	



	