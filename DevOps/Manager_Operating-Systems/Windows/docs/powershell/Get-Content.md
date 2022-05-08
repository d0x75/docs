Get-Content
------------

- Exemplo usando 'Get-Content' do powershell do Windows, para converter uma planilha CSV em CSV_UTF8:

		Get-Content 'D:\anp.csv' | Out-File 'D:\anp_utf8.csv' -Encoding UTF8

