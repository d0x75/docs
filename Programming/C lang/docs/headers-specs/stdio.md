stdio.h
--------

Esse arquivo de cabeçalho C define 3 tipos de variáveis, várias macros e várias funções de I/O ; ambos para serem utilizadas no programa que
tiver esse arquivo de cabeçalho incluso.


- Variáveis definidas em 'stdio.h' :


1. ``size_t``


size_t
--------

As ênfases (minhas) claramente dizem: size_t é um tipo inteiro sem sinal. Em outras palavras, size_t pode muito bem ser equivalente a uint8_t, como também pode ser equivalente a uint64_t, ou outros tipos de característica similar. Portanto, size_t não é garantido de ser equivalente a unsigned int. É permitido, sim, mas é diferente de ser garantido.
Voltando para a pergunta:
[…] porém sempre vejo em livros e códigos usando o tipo size_t em vários lugares que não representam tamanhos.
size_t é normalmente usado pra indexar arranjos (arrays) e fazer contagem em laços (loops). Por quê? Vamos usar um exemplo: ao usar um tipo diferente, como unsigned int, para indexar um arranjo, é possível que a operação de indexação falhe em sistemas 64-bit quando o índice exceder o valor de UINT_MAX, ou se o índice depende de aritmética modular para voltar ao valor zero após incrementar o índice máximo 1.


( tamanho de dados tipo size_t : 32 bits / 4 bytes )

 - Esse é o tipo de dados referente ao retorno do operador 'sizeof'. é definido no header 'stdlib.h', por trás seu tipo é unsigned int.

 - Seu tipo é de fato um : 'unsigned int'


 - Formas de declarar variáveis com tipo size_t :

 		?


2. ``FILE``

3. ``fpos_t``



----



- Macros definidas em 'stdio.h' :


1. ``NULL``

2. ``_IOFBF, _IOLBF and _IONBF``

3. ``BUFSIZ``

4. ``EOF``

5. ``FOPEN_MAX``

6. ``FILENAME_MAX``

7. ``L_tmpnam``

8. ``SEEK_CUR, SEEK_END, and SEEK_SET``

9. ``TMP_MAX``

10. ``stderr, stdin, and stdout``


- Lista de funções que são definidas em 'stdio.h' :


1. ``int fclose(FILE *stream)``

2. ``void clearerr(FILE *stream)``

3. ``int feof(FILE *stream)``

4. ``int ferror(FILE *stream)``

5. ``int fflush(FILE *stream)``

6. ``int fgetpos(FILE *stream, fpos_t *pos)``

7. ``FILE *fopen(const char *filename, const char *mode)``

8. ``size_t fread(void *ptr, size_t size, size_t nmemb, FILE *stream)``

9. ``FILE *freopen(const char *filename, const char *mode, FILE *stream)``

10. ``int fseek(FILE *stream, long int offset, int whence)``

11. ``int fsetpos(FILE *stream, const fpos_t *pos)``

12. ``long int ftell(FILE *stream)``

13. ``size_t fwrite(const void *ptr, size_t size, size_t nmemb, FILE *stream)``

14. ``int remove(const char *filename)``

15. ``int rename(const char *old_filename, const char *new_filename)``

16. ``void rewind(FILE *stream)``

17. ``void setbuf(FILE *stream, char *buffer)``

18. ``int setvbuf(FILE *stream, char *buffer, int mode, size_t size)``

19. ``FILE *tmpfile(void)``

20. ``char *tmpnam(char *str)``

21. ``int fprintf(FILE *stream, const char *format, ...)``

22. ``int printf(const char *format, ...)``

23. ``int sprintf(char *str, const char *format, ...)``

24. ``int vfprintf(FILE *stream, const char *format, va_list arg)``

25. ``int vprintf(const char *format, va_list arg)``

26. ``int vsprintf(char *str, const char *format, va_list arg)``

27. ``int fscanf(FILE *stream, const char *format, ...)``

28. ``int scanf(const char *format, ...)``

29. ``int sscanf(const char *str, const char *format, ...)``

30. ``int fgetc(FILE *stream)``

31. ``char *fgets(char *str, int n, FILE *stream)``

32. ``int fputc(int char, FILE *stream)``

33. ``int fputs(const char *str, FILE *stream)``

34. ``int getc(FILE *stream)``

35. ``int getchar(void)``

36. ``char *gets(char *str)``

37. ``int putc(int char, FILE *stream)``

38. ``int putchar(int char)``

39. ``int puts(const char *str)``

40. ``int ungetc(int char, FILE *stream)``

41. ``void perror(const char *str)``