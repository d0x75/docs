## TEdit 


> TEdit é um componente que é um campo recebe texto 



#### Ofuscar para digitar senhas no cempo de texto TEdit : 


1. Ir nas propriedades do TEdit, na opção Fontes > Mudar o 'Name' = Wingdings
2. Ir denovo nas propriedades do TEdit, na opção Passwordchar > Mudar  #0 para = l ( um 'L' minúsculo mesmo )


---


- Exemplo prático usando um campo TEdit.. fazendo um IF com um valor disgitado em tempo de execução no TEdit : 



```Pascal
var
  editar: TEdit;

procedure TForm1.LoginClick(Sender: TObject);
begin
editar:=LoginEdit1;
if LoginEdit1.Text = '123' then ShowMessage('OK')
else ShowMessage('Try Again')

end;
```