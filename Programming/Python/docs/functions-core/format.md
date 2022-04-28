Função incorporada do Python.

---

format() - Esta função formata um valor especificado em um formato especificado 



- _Sintaxe_ : format(value, format)

- _Args_ : 

> value = Um valor de qualquer formato.
> format = O formato no qual você deseja formatar o valor. 
Lista de Valores utilizado:

			'<' - Left aligns the result (within the available space)
			'>' - Right aligns the result (within the available space)
			'^' - Center aligns the result (within the available space)
			'=' - Places the sign to the left most position
			'+' - Use a plus sign to indicate if the result is positive or negative
			'-' - Use a minus sign for negative values only
			' ' - Use a leading space for positive numbers
			',' - Use a comma as a thousand separator
			'_' - Use a underscore as a thousand separator
			'b' - Binary format
			'c' - Converts the value into the corresponding unicode character
			'd' - Decimal format
			'e' - Scientific format, with a lower case e
			'E' - Scientific format, with an upper case E
			'f' - Fix point number format
			'F' - Fix point number format, upper case
			'g' - General format
			'G' - General format (using a upper case E for scientific notations)
			'o' - Octal format
			'x' - Hex format, lower case
			'X' - Hex format, upper case
			'n' - Number format
			'%' - Percentage forma

---


*exemplo* :

- Usando a função do Python 'format()', para mudar o valor para o formato Hexadecimal :

		x = format(255, 'x')
		print(x)
