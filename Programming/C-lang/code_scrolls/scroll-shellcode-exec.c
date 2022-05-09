#include<stdio.h>
#include<string.h>


unsigned char shellcode[] = ""; // bytes do shellcode

main()
{
	printf("Shellcode Length:  %d\n", strlen(code));
	int (*ret)() = (int(*)())code;
	ret();
}
