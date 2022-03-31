### if
.........

- Exemplos de como usar o laço condicional IF no Delphi. 

Exemplo 1  :
		
		begin
		editar:=LoginEdit1;
		if LoginEdit1.Text = '123'
		end;
		end.

Exemplo 2  :

		begin
		editar:=LoginEdit1;
		editar:=LoginEdit2;
		if LoginEdit1.Text = '123' then
		begin
		if LoginEdit2.Text = '123'
		then ShowMessage('OK')
		else ShowMessage('Try Again')

		end;
		end;
		end.

