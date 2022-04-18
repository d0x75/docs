#### gcc ( C compiler )



- Utilizar o GCC para transformar em assembly, um código escrito em C . Será criado um arquivo de extensão '.s' com o código em Assembly certinho (flag -S) Exemplos:

		gcc --no-pie -m32 -S programa.c -o-

		gcc --no-pie -m32 -S programa.c  -o- | grep -vF .

		gcc --no-pie -m32 -S -masm=intel programa.c  -o- | grep -vF .


