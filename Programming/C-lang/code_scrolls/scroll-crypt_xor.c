int CryptBuffer(unsigned long long buffer[TAMANHO_BUFF], unsigned long long key){

	unsigned indice;
	for(indice=0;indice<TAMANHO_BUFF;indice++){
		buffer[indice]=buffer[indice]^key;
	}
	return 0;
}