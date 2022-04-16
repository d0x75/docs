Colocar aplicativo para ter opção de execução,com o botão direito no windows explorer
---------------------------------------------------------------------------------------

- Seguir os seguintes passos:


1. Ir no até : HKEY_CLASSES_ROOT/Directory/Background/shell

2. Clicar com o botão direito em 'shell' > Novo > Chave > colocar o nome da chave (que irá aparecer no menu de contexto do windows)

3. Clicar com o botão direito na chave criada acima > Novo > Chave > setar nome da chave = command

4. Dentro da Chave 'command', ao lado direito clicamos no 'REG_SZ' com o nome : Padrão > No campo
valor, colocamos o caminho do binário que será aberto através do menu de contexto do windows.  Exemplo :

		"C:\Windows\System32\notepad.exe"


Feito isso, ao clicarmos em qualquer lugar do Windows Explorer, irá aparecer a opção para abrir o
binário que colocamos, com o nome definido no passo 2.