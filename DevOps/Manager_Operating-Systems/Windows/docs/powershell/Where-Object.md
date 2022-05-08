Where-Object
--------------

- Listando objetos usando o "WHERE", para listar apenas "onde" for passado como parâmetro pro Where-Object. Exemplo :

- O alias do Where-Object é = ?


		$TODOS = dir -Recurse -File | Where-Object Name -like "*TESTE*"


- Selecionando objetos com Select-Object combinado com um Where-Object, os 2 comandos vistos anteiormente :


		$TODOS = dir -Recurse -File | Where-Object Name -like "*TESTE*" | Select-Object Name,Length,Extension 



##### Case Practical



- Implementando nosso script, para retornar apenas os arquivos que são setados no Where e no Select.


			dir -Recurse -File | Where-Object Name -like "*TESTE*" | Select-Object Name, { "{0:N2}KB" -f ($_.Length / 1KB) }



- Deixando o Script mais elegante e mais enxuto

``
	$nameExpr = "Name"
	$lengthExpr = { "{0:N2}KB" -f ($_.Length / 1KB) }
	$param = ($nameExpr,$lengthExpr)
	dir -Recurse -File | 
	    ? Name -like "*TESTE*" |
	     Select `
	        $param
``
