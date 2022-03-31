SSDT
======



- No kernel do Windows a SSDT tem o nome de : KeServiceDescriptorTable




#### Um metodo para descobrir como a SSDT foi alterada:

1. Chegar na função alterada na SSDT

2. Copiar o offset da função/driver malicioso, que conseguimos listar na SSDT

3. Iniciar a máquina LIMPA, e verificar na SSDT o offset que copiamos no passso anterior.
