ConvertTo-Csv
--------------


- Converter dados para CSV


		$variavel | ConvertTo-Csv



- Converter dados para CSV, sem informações de tipo de arquivo no cabeçalho da planilha csv.


		ConvertTo-Csv -NoTypeInformation



#### Observações: 


- Quando vier um "lixo" no formato de CSV exportado pelo powershell, devemos usar o método -NoTypeInformation do comando que exporta pra CSV.