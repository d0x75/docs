### lsattr



- verificar atributos do arquivo : 


``lsattr file.txt"``




---


a = Append only, permitira apenas acrescentar dados no arquivos. Nunca sobrescrever dados que já estão escritos

c = Compressed, esse atribudo indica que o arquivo será comprimido ao gravar no disco. O kernel comprime antes de gravá-lo, e o descomprime quando é lido.

d = Sem dump, marca o arquivo como não sendo um candidato para backups.

e = Indica que o arquivo está usando extensões para mapear blocos no disco.

i = Imuttable, indica que o arquivo não pode sofrer alterações. ( não pode ser alterado,excluído e nem da do tipo )

s = Secure Deletion, quando o arquivo é apagado, os blocos no disco que ele utilizava são zerados(preenchidos com 0)
Esse atributo não é respeitado pelos sistemas de arquivo ext2 e ext3.

u = Undeletable, Torna o arquivo recurerável mesmo se for excluído.( não disponível em ext2 e ext3 )

A = No Atime Updates, não atualiza a hora/data de acesso.

D = Quando as alterações forem feitas no arquivo, elas serão escritas em disco de imediato.