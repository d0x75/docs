- um pouco sobre RE no código do VB  :

Ao contrário do que muitos pensam, aplicativos em VB, se compilados em Native Code, geram códigos normais de assembly, que podem ser abertos em qualquer debugger. A diferença está que além do aplicativo, ele utiliza um "linker", uma dll ( MSVBM60.dll ) que contém todas as funções que o VB utiliza. Assim, quando você faz uma comparação de strings por exemplo, ele chama a função "vbaStrCmp" da MSVBM60.dll. Devido a essa conexão entre o executável e a DLL, eles são normalmente ( quando compilados em Native Code ), mais complicados de se fazer o debug.


O estado do botão vem logo após o valor que define a sua altura, seguido do byte 08 ( SEMPRE ).

 altura do botão no caso é indicada pelo "EF 01" ( na ordem reversa de byte fica 01EFh = 495d ), seguido do byte 08 e de um byte 00. 00 indica que o botão está desabilitado (Enabled = False ), e 01 indica que está ativo ( Enabled = True ).