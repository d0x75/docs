Endianess
----------

### endianness (ordenação de bytes)

São padrões que os processadores utilizam para a ordenação de bytes em memória, a sua diferenciação é de arquitetura p/ arquitetura.

**little-endiann**

- Utilizado pela arquitetura Intel **x86**, AMD 64.
- Nesse padrão o byte menos significativo é colocado primeiro na memória.
- Exemplo, para encontrar o endereço ip local 127.0.0.1, temos que saber que vai ser informado ao contrário ( de trás p/ frente ). Então encontraríamos 0x100007F.

**big-endiann**

- Utilizado pelo protocolo TCP/IP , RISC, Motorola, Android etc..
- Nesse padrão o byte mais significativo entra primeiramente. na memória, ao contrário do **x86**.
- No exemplo do endereço 127.0.01 , seria equivalente a 0xF7000001