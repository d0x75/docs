### chattr


> Quando encontramos arquivos que são impossíveis de ser deletados . provavelmente será a limitação de atributos referente ao arquivo target. Podemos fazer as
seguintes verificações :

- verificar atributos do arquivo : 

``lsattr file.txt"``

- tirar o atributo de Imutável do arquivo : "

``sudo chattr -i``

- tirar o atributo de Append Only do arquivo : 

``sudo chattr -a``

Feito isso conseguimos deletar o arquivo normalmente : 

``rm file.txt``
