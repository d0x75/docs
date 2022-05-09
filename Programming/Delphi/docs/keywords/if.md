### if/else


- **Estrutura de decisão if then else no Delphi** :

> Em Pascal existem duas instruções que realizam tomadas de decisão e desvios de operações:
a instrução de decisão simples if…then; e a instrução de decisão composta if…then…else.


*if ... then :*



- Sintaxe:

		if <condição> then
		<instrução para condição verdadeira>
		<demais instruções>;


```Pascal
if 1=1 then
	ShowMessage('OK')
ShowMessage('CONT')
```


- Sintaxe :

		if <condição> then
			begin
			<instrução para condição verdadeira>;
			instrução para condição verdadeira>;
			<instrução para condição verdadeira>;
			end;
		   <demais instruções>;


```Pascal
if 1=1 then
begin
	ShowMessage('OK');
	ShowMessage('OK2');
end;
ShowMessage('CONT');
```


*if..then..else*


- Sintaxe:

		if <condição> then
		 <instrução para condição verdadeira>
		 else
		<instrução para condição falsa>;
		<demais instruções>;


```Pascal
if 1<>1 then
	ShowMessage('OK')
else
	ShowMessage('ERR');
```



