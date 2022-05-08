#### nasm


- É um assembler, utilizamos ele para compilar programas escritos em Assembly.

 - Exemplos de uso:

 		nasm -f elf32 -o hellonasm hello.asm ( COMPILAÇÃO DO CÓDIGO ASSEMBLU "hello.asm" que gerou um arquivo Objeto 'helloasm')


- Exemplo de uma compilação e linkEdition de um programa escrito em Assembly:

		 	nasm -f elf32 -o objeto hello.asm
 			ld -melf_i386 -o program objeto




>Source code, que está sendo compilado:

``
section .data
msg: db "Papo binario", 10
len: equ $-msg
section .text
global_start
_start:
mov edx, len
mov ecx, msg
mov ebx, 1
mov eax, 4
int 0x80
mov ebx, 0
mov eax, 1
int 0x80
``