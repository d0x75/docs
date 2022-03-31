Unpacking UPX for binaries
----------------------------


Quando você utiliza um packer, como o UPX, o EP do programa é desviado para o endereço do que conhecemos como Loader. A função do loader é somente descompactar o executável para a memória e depois chamar o
OEP ( Original Entry Point, O EP veridadeiro que contém o código verdadeiro e descomprimido ). 

- Resumindo segue esse padrão:

		EP -> Loader -> Descomprime o conteúdo do executável para a memória -> Move o EP para o OEP


- A maioria dos arquivos comprimidos com UPX começam com o seguinte código :

		60 PUSHAD

- E terminam com o seguinte código :

		POPAD
		JMP <OEP> 



---


