int CifrarTexto(char *name, unsigned long long key){

	FILE *leitura, *escrita;
	unsigned long long buffer[TAMANHO_BUFF];
	size_t lidos, tamanho;
	char newName[0x500];

	strcpy(newName,name);
	strcat(newName,".ESOJ");
	printf("\nEncriptando arquivo '%s'\n",name);
	printf("Encripted! => '%s'\n",newName);

	if(!(leitura=fopen(name,"rb"))){
		printf("Erro ao abrir arquivo de leitura, #%i, %s\n", errno, strerror(errno));
		return 1;
	}

	if(!(escrita=fopen(newName,"wb"))){
		printf("Erro ao abrir arquivo de escrita, #%i, %s\n", errno, strerror(errno));
		return 2;
	}

	tamanho=sizeof(unsigned long long)*TAMANHO_BUFF;

	while ((lidos=fread((void*)buffer,1,tamanho,leitura))>0){

		CryptBuffer(buffer,key); // USING A FUNCTION FOR CRYPT, this is some exemple.
		fwrite((void *)buffer,lidos,1,escrita);

	}

	fclose(leitura);
	fclose(escrita);
	remove(name);
	return 0;
	
}