TEdit - Ofuscar para digitar senhas : 


Ir nas propriedades do TEdit, na opção Fontes > Mudar o 'Name' = Wingdings
Ir denovo nas propriedades do TEdit, na opção Passwordchar > Mudar  #0 para = l ( um 'L' minúsculo mesmo )


---


Fazer um IF com um valor que é atribuído em tempo de execução no TEdit : 


var
  editar: TEdit;



procedure TForm1.LoginClick(Sender: TObject);
begin
editar:=LoginEdit1;
if LoginEdit1.Text = '123' then ShowMessage('OK')
else ShowMessage('Try Again')

end;