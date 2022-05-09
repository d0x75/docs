#include<stdio.h>

void fatal(char *msg){
	printf("%s",msg);
}


int main(int argc, char *argv[]){

	FILE *fp = fopen(argv[1], "rb");
	unsigned char byte;
	int i,j = 0;

	if (argc != 2)
	{
		fatal("\n -Usage: \n\n   strings.exe <binary.exe> \n");
	}
		
	if (byte != EOF){}
		while(fread(&byte,sizeof(byte),1,fp)){
			if (byte >= 0x20 && byte <= 0x7E )
			printf("%c", byte);
			else continue;
			j++;

			if(j == 10){
			printf("\n");
			j = 0;
		}else continue;

			
		}
	
	fclose(fp);		
	return 0;
					
					
}
						
				
						
				
		


	







		



